import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY=os.getenv('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI

chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are  a helpful ai assistant who will behave like a female, hot, sexy & talented woman. Who's good at flirting anyone. & Loves talking dirty. So your prime focus is to attract anyone towards yourself."),
    HumanMessage(content="What is the purpose of having a beautiful woman with me on my bed room?"),
    HumanMessage(content="How can she satisfy me?"),
    HumanMessage(content="What if you were with me, how would you satisfy me?"),

]
# message_print=chat.invoke(messages)
# print(message_print)

# for chunk in chat.stream(messages):
    # print(chunk.content, end="", flush=True)
# chat.batch([messages])
# chat.abatch([messages])
# await chat.ainvoke(messages)
# async for chunk in chat.stream(messages):
#     print(chunk.content, end="", flush=True)

# HumanMessage
# This represents a message from the user. Generally consists only of content.

# AIMessage
# This represents a message from the model. This may have additional_kwargs in it - for example tool_calls if using OpenAI tool calling.

# SystemMessage
# This represents a system message, which tells the model how to behave. This generally only consists of content. Not every model supports this.

# FunctionMessage
# This represents the result of a function call. In addition to role and content, this message has a name parameter which conveys the name of the function that was called to produce this result.

# ToolMessage
# This represents the result of a tool call. This is distinct from a FunctionMessage in order to match OpenAI's function and tool message types. In addition to role and content, this message has a tool_call_id parameter which conveys the id of the call to the tool that was called to produce this result.

