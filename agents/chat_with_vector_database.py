import os
import openai
import json
import numpy as np
from numpy.linalg import norm
import re
from time import time,sleep
from uuid import uuid4
import datetime
import pinecone

from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain import LLMChain, OpenAI, LLMMathChain
from langchain.memory import ConversationBufferMemory
from pydantic import BaseModel, Field
from langchain.utilities import GoogleSearchAPIWrapper
from subprocess import Popen, PIPE

### DEFINE THE LLM
llm = OpenAI( temperature=0 ) # 1st things 1st, we need an llm
###
### DEFINE PARTS FOR TOOLS // these need to be defined before we build the tools array ###
class ShellSchema( BaseModel ):
    command: str = Field( description="The shell command to execute on a wsl 2 ubuntu linux subsystem for windows 10 followed by a redirect of stderr to dev null." )
    # 2>&1 otherwise we pay for tokens to read a bunch of "Permission Denied" errors!

def shell_function(command: str) -> str:
    process = Popen(command, stdout=PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode()

# search = SerpAPIWrapper() # not sure which search to use
search = GoogleSearchAPIWrapper()
llm_math_chain = LLMMathChain.from_llm( llm=llm, verbose=True)
###
### BUILD THE TOOLS ARRAY  // Now we can build the tools array ###
tools = [
    Tool(
        name="shell",
        func=shell_function,
        args_schema=ShellSchema,
        description="useful for when you need to execute shell commands"
    ),
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math" )]
###
### BUILD THE CHAIN  // Now we can build the chain ###
###
### continue setting up CppMaker from https://python.langchain.com/docs/modules/memory/agent_with_memory
prefix = """Have a conversation with a human, answering the following questions as best you can. You have access to the following tools:"""
suffix = """Begin!"  

{chat_history}
Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt( tools, prefix=prefix, suffix=suffix, input_variables=[ "input", "chat_history", "agent_scratchpad" ])
memory = ConversationBufferMemory( memory_key="chat_history" )
llm_chain = LLMChain( llm=OpenAI( temperature=0 ), prompt=prompt )
agent = ZeroShotAgent( llm_chain=llm_chain, tools=tools, verbose=True )
agent_chain = AgentExecutor.from_agent_and_tools( agent=agent, tools=tools, verbose=True, memory=memory )

### end creating chain.  uncomment some of the following to test it out.
### END BUILDING THE CHAIN // now we can use it in the loop! ###

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8' ) as infile:
        return infile.read()


def save_file(filepath, content ):
    with open(filepath, 'w', encoding='utf-8' ) as outfile:
        outfile.write(content )


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8' ) as infile:
        return json.load( infile )


def save_json(filepath, payload):
    with open(filepath, 'w', encoding='utf-8' ) as outfile:
        json.dump(payload, outfile, ensure_ascii=False, sort_keys=True, indent=2)


def timestamp_to_datetime( unix_time ):
    return datetime.datetime.fromtimestamp( unix_time ).strftime("%A, %B %d, %Y at %I:%M%p %Z")


def gpt3_embedding(content, engine='text-embedding-ada-002' ):
    content = content.encode(encoding='ASCII',errors='ignore' ).decode()  # fix any UNICODE errors
    response = openai.Embedding.create( input=content,engine=engine )
    vector = response[ 'data' ][ 0 ][ 'embedding' ]  # this is a normal list
    return vector


def ai_agent_completion( prompt ):
    print( "getting response from ai agent..." )
    text = agent_chain.run( prompt )
    print( "response received from ai agent." )
    # text = agent_chain.agent.llm_chain.llm.response
    text = re.sub( '[\r\n]+', '\n', text )
    text = re.sub( '[\t ]+', ' ', text )
    filename = '%s_gpt3.txt' % time()
    if not os.path.exists( '/home/adamsl/linuxBash/agents/gpt3_logs' ):
        os.makedirs( '/home/adamsl/linuxBash/agents/gpt3_logs' )

    print( "saving response from ai agent to file...")
    save_file( '/home/adamsl/linuxBash/agents/gpt3_logs/%s' % filename, prompt + '\n\n==========\n\n' + text )
    return text

def ai_completion(prompt, engine='text-davinci-003', temp=0.0, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=[ 'USER:', 'RAVEN:' ]):
    max_retry = 5
    retry = 0
    prompt = prompt.encode(encoding='ASCII',errors='ignore' ).decode()
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response[ 'choices' ][ 0 ][ 'text' ].strip()
            text = re.sub( '[\r\n]+', '\n', text )
            text = re.sub( '[\t ]+', ' ', text )
            filename = '%s_gpt3.txt' % time()
            if not os.path.exists( '/home/adamsl/linuxBash/agents/gpt3_logs' ):
                os.makedirs( '/home/adamsl/linuxBash/agents/gpt3_logs' )
            save_file( '/home/adamsl/linuxBash/agents/gpt3_logs/%s' % filename, prompt + '\n\n==========\n\n' + text )
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            print( 'Error communicating with OpenAI:', oops )
            sleep( 1 )

def load_conversation( results_arg ):  # comes from:  vdb.query( vector = embedded_user_input, top_k = convo_length )
    result = list() # initialize the list that will ultimately be returned
    for matching_unique_id in results_arg[ 'matches' ]:
        filename = '/home/adamsl/linuxBash/agents/nexus/%s.json' % matching_unique_id[ 'id' ]
        # if filename exists, load it and append it to the result list, otherwise skip it
        if not os.path.exists( filename ):
            print ( 'file not found:', filename )
            continue
        else:
            print ( 'file found:', filename )
        info = load_json( filename )
        result.append( info )
    ordered = sorted( result, key=lambda d: d[ 'time' ], reverse=False )  # sort them all chronologically
    messages = [ i[ 'message' ] for i in ordered ]
    return '\n'.join( messages ).strip()

if __name__ == '__main__':
    convo_length = 30
    openai.api_key = open_file( '/home/adamsl/linuxBash/agents/key_openai.txt' )
    pinecone.init( api_key=open_file( '/home/adamsl/linuxBash/agents/key_pinecone.txt' ), environment='northamerica-northeast1-gcp' )
    vdb = pinecone.Index( "debug-memory" )
    ###
    USE_RUN_TEXT = False
    while True:
        ###
        data_for_pinecone_upsert = list()  # initialize the list that will ultimately be upserted to the vector database
        if ( USE_RUN_TEXT == True ):
            temp = input( "using run.txt, ok? <enter> to continue.  ctrl-c to quit" )
            user_input = open_file( '/home/adamsl/linuxBash/agents/run.txt' )
            USE_RUN_TEXT = False
        else:
            user_input = input( '\n\nUSER: ' )
        
        #user_input = open_file( '/home/adamsl/linuxBash/agents/run.txt' )
        timestamp = time()
        timestring = timestamp_to_datetime( timestamp )
        
        print( "getting embedding from user input string..." )
        embedded_user_input = gpt3_embedding( user_input )
        print( "embedded_user_input length:", len( embedded_user_input ))
        ###
        unique_id = str( uuid4())
        metadata = { 'speaker': 'USER', 'time': timestamp, 'message': user_input, 'timestring': timestring, 'uuid': unique_id }
        save_json( '/home/adamsl/linuxBash/agents/nexus/%s.json' % unique_id, metadata ) # <<--- save user input to a .json file on our file system ---<<<
        data_for_pinecone_upsert.append(( unique_id, embedded_user_input ))  # <<--- this data is going to pinecone ---<<<
        ###
        ###  Now we have the user input not only saved to our local file, but it is also placed in the built-in mutable
        ###  sequence ( the list()) that we will ultimately be inserted into the vector database under the same unique_id.
        ###
        results = vdb.query( vector=embedded_user_input, top_k=convo_length )# search for relevant message unique ids in vsd
        conversation = load_conversation( results )  # with these unique ids, which where very cheap to aquire, we load the
                                                     # relevant conversation data from our local file system
        prompt = open_file( '/home/adamsl/linuxBash/agents/prompt_response.txt' ).replace( '<<CONVERSATION>>', conversation ).replace( '<<MESSAGE>>', user_input )
        ###
        # ai_completion_text = ai_completion( prompt )  # <<-- send the prompt created from the template to the model ---<<<
        ###
        print( "getting response from ai agent wit prompt: %s" % prompt )
        input( "ok? <enter> to continue.  ctrl-c to quit")
        ai_completion_text = ai_agent_completion( prompt )  # <<-- send the prompt created from the template to the agent ---<<<
        ###
        timestamp = time()
        timestring = timestamp_to_datetime( timestamp )
        embedded_ai_completion = gpt3_embedding( ai_completion_text )
        unique_id = str( uuid4())
        metadata = { 'speaker': 'RAVEN', 'time': timestamp, 'message': ai_completion_text,
                     'timestring': timestring, 'uuid': unique_id }
        ###
        save_json( '/home/adamsl/linuxBash/agents/nexus/%s.json' % unique_id, metadata ) # <<--- save ai answer to a .json file ---<<<
        ###
        data_for_pinecone_upsert.append(( unique_id, embedded_ai_completion )) # <<--- add ai answer to data to be upserted ---<<<
        vdb.upsert( data_for_pinecone_upsert ) # <<--- upsert the data to pinecone ---<<<
        print( '\n\nRAVEN: %s' % ai_completion_text )  
        
        # just noticed that the unique_id is being used in the upsert and
        # the save_json, so it's being saved twice. How are we referencing both?
        # we "tag" the data here on our file system.  the vector database
        # returns the unique_ids that have relevance.  we use those ids to get the relevant data from
        # our file system.  the unique_id is the "tag" that links the two.