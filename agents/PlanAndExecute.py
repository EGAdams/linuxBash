#
# Plan and execute agent
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
    command: str = Field( description="The shell command to execute on a wsl 2 ubuntu linux subsystem for windows 10 followed by a redirect of stderr to dev null." )

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
        description="useful for when you need to execute shell commands"
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
agent.run( "My Windows 10 hard drive is maxed out in Task Manager. Your shell Tool that you have access to is located on my Windows 10 WSL 2 Ubuntu subsystem for Linux, so if you need to use the shell, feel free to use Ubuntu Linux style commands. Just remamber to send all the errors out to dev null whenever you execute commands so that we minimize the output of the command.  The /mnt/c mount (or C: Drive Linux mount) has got plenty of free space, it's just that the Task Manager is reporting 97 to 100 percent usage.  Can you find out how we can get this usage percentage down?" )