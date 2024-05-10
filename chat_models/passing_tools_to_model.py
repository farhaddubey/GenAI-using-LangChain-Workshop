import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

# If we're using model generated tools invocations to actually call tools and want to pass the tool results back to the model, we can do using 
# Tool Message 
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY, temperature=0)
@tool
def add(a:int, b:int)->int:
    """Adds a and b
    
    Args:
        a: first int
        b: second int
    """
    return a+b
@tool
def multiply(a:int, b:int)->int:
    """Substact a and b"""
    return a*b
tools = [add, multiply]
llm_with_tools=llm.bind_tools(tools)
query = "What is 3 * 12? Also, what is 11 + 49?"
messages=[HumanMessage(query)]

ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:
    selected_tool = {"add":add, "multiply":multiply}[tool_call["name"].lower()]
    tool_output = selected_tool.invoke(tool_call["args"])
    messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))
print(messages)

# Tool Schemas can also be defined using Pydantic Class 
from langchain_core.pydantic_v1 import BaseModel, Field

# Note that the docstrings here are crucial, as they will be passed along
# to the model along with the class name.
# class add(BaseModel):
#     """Add two integers together."""

#     a: int = Field(..., description="First integer")
#     b: int = Field(..., description="Second integer")


# class multiply(BaseModel):
#     """Multiply two integers together."""

#     a: int = Field(..., description="First integer")
#     b: int = Field(..., description="Second integer")


# tools = [add, multiply]
# Binding tool Schemas 
# We can use the bind_tools() method to handle converting multiply to a tool and binding it to the model(ie. passing it each time the model is invoked )
# llm_with_tools=llm.invoke(tools)
# tool_choice ="any" is supported by OpenAI, MistralAI, FireworksAI and Groq 
# always_multiply_llm=llm.bind_tools([multiply], tool_choice='multiply')
# always_call_tool_llm=llm.bind_tools([add, multiply], tool_choice='any')
# Reading tool calls from model output 
# If tool call are included in a LLM messages, they are attached to the corresponding AIMessage or AIMessageChunk (when streaming) as a list of 
# ToolCall objects in the .tool_calls attribute.
query = "What is 3 * 12? Also, what is 11+ 49?"
# print(llm_with_tools.invoke(query))
# print(llm_with_tools.invoke(query).tool_calls)

# from langchain_core.output_parsers.openai_tools import PydanticToolsParser

# chain = llm_with_tools | PydanticToolsParser(tools=[multiply, add])
# chain.invoke(query)
