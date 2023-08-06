#
# Plan and execute agent
#
# mabybe later? https://python.langchain.com/docs/use_cases/graph/tot
#
from langchain.chat_models import ChatOpenAI
from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain.llms import OpenAI
from langchain import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain import LLMMathChain
from langchain.tools import Tool
from pydantic import BaseModel, Field
from subprocess import Popen, PIPE
from dotenv import load_dotenv

load_dotenv()

class ShellSchema(BaseModel):
    command: str = Field(description="The shell command to execute")

def shell_function(command: str) -> str:
    process = Popen(command, stdout=PIPE, shell=True)
    output, _ = process.communicate()
    return output.decode()

search = SerpAPIWrapper()
llm = OpenAI(temperature=0)
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
tools = [
    Tool(
        name="shell",
        func=shell_function,
        args_schema=ShellSchema,
        description="Executes shell commands."
    ),
    Tool(
        name = "Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
]
model = ChatOpenAI(temperature=0)

planner = load_chat_planner(model)

executor = load_agent_executor(model, tools, verbose=True)

agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

# Run Example
agent.run( "please list the contents of the current directory." )