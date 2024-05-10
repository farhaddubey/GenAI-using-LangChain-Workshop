import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
#     print(gathered.tool_calls)
# print(type(gathered.tool_calls[0]["args"]))
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# When tools are called in a streaming context, message chunks will be populated with tool call chunk objects in a list via the .tool_call_chunks attribute. A ToolCallChunk includes optional string fields for the tool name, args, and id, and includes an optional integer field index that can be used to join chunks together. 

#  Fields are optional because portions of a tool call may be streamed across different chunks (e.g., a chunk that includes a substring of the arguments may have null values for the tool name and id).

# Because message chunks inherit from their parent message class, an AIMessageChunk with tool call chunks will also include .tool_calls and .invalid_tool_calls fields. These fields are parsed best-effort from the message's tool call chunks.
# async for chunk in llm_with_tools.astream(query):
#     print(chunk.tool_call_chunks)

# first = True
# async for chunk in llm_with_tools.astream(query):
#     if first:
#         gathered = chunk
#         first = False
#     else:
#         gathered = gathered + chunk

#     print(gathered.tool_call_chunks)
# first = True
# async for chunk in llm_with_tools.astream(query):
#     if first:
#         gathered = chunk
#         first = False
#     else:
#         gathered = gathered + chunk



@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b
llm=ChatOpenAI(model='gpt-3.5-turbo-0125', api_key=SECRET_KEY)

tools = [add, multiply]
llm_with_tools = llm.bind_tools(tools)
query="How to please wife?"
messages = [HumanMessage(query)]
ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:
    selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
    tool_output = selected_tool.invoke(tool_call["args"])
    messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))

messages
llm_with_tools.invoke(messages)
# For most models it's important that the ToolCall and ToolMessage ids line up, so that each AIMessage with ToolCalls is followed by ToolMessages with corresponding ids.

# For example, even with some special instructions our model can get tripped up by order of operations:
print(llm_with_tools.invoke(
    "Whats 119 times 8 minus 20. Don't do any math yourself, only use tools for math. Respect order of operations"
).tool_calls)

from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

examples = [
    HumanMessage(
        "What's the product of 2 and 3 plus 1", name="Farhad Dubey"
    ),
    AIMessage(
        "", 
        name="knights",
        tool_calls=[
            {"name":"mulitply", "args":{"x":317253, "y":128472}, "id":"1"}
        ],
    ),
    ToolMessage("23123123", tool_call_id="1"),
    AIMessage(
        "",
        name="example_assistant",
        tool_calls=[{"name":"add", "args":{"x":12313, "y": 23123}, "id":"1"}],
    ),
   ToolMessage("16505054788", tool_call_id="2"),
    AIMessage(
        "The product of 317253 and 128472 plus four is 16505054788",
        name="example_assistant",
    ),
]
system="""You are bad at math but expert using calculator."""
few_shot_prompt=ChatPromptTemplate.from_messages(
    [
        ("system", system),
        *examples,
        ("human","{query}"),
    ]
)
chain = {"query": RunnablePassthrough()} | few_shot_prompt | llm_with_tools
chain.invoke("what's 119 times 8 minus 2").tool_calls