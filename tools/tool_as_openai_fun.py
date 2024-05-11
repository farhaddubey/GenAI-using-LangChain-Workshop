import os

from dotenv import load_dotenv
from langchain_community.tools import MoveFileTool
from langchain_core.messages import HumanMessage
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-3.5-turbo-0125', api_key=SECRET_KEY)
tools = [MoveFileTool()]
functions = [convert_to_openai_function(t) for t in tools]
functions[0]
message =model.invoke(
    [HumanMessage(content="move file foo to bar")], functions=functions
)
print(message)
# print(message.additional_kwargs['function_calling'])