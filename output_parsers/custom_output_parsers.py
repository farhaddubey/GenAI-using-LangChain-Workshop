# There are 2 ways to implement a custom parser to structure the model output into a custom format. 
# 1. Using RunnableLambda or RunnableGenerator in LCEL --we strongly recommend this for most use cases. 
# 2. By inheriting from one of the base classes for out parsing --this is the hard way of doing things. 

import os
# Custom Output Parsers using Runnable Lambdas and Generators 
# Output parser of inverting case  
from typing import Iterable

from dotenv import load_dotenv
from langchain_anthropic.chat_models import ChatAnthropic
from langchain_core.messages import AIMessage, AIMessageChunk

load_dotenv()
SECRET_KEY= os.getenv('OPENAI_API_KEY')
model = ChatAnthropic(model_name="gpt-3.5-turbo-0125", api_key=SECRET_KEY)
def parse(ai_message : AIMessage) ->str:
    """Parse the AI message"""
    return ai_message.content.swapcase()
chain = model | parse 
print(chain.invoke("hello"))
# LCEL automatically upgrades the function parse to RunnableLambda(parse) when composed using a | syntax.

# If you don't like that you can manually import RunnableLambda and then runparse = RunnableLambda(parse).
for chunk in chain.stream("Tell me about yourself"):
    print(chunk, end="|", flush=True)
from langchain_core.runnables import RunnableGenerator


def streaming_parse(chunks: Iterable[AIMessageChunk]) -> Iterable[str]:
    for chunk in chunks:
        yield chunk.content.swapcase()


streaming_parse = RunnableGenerator(streaming_parse)
chain = model | streaming_parse
chain.invoke("hello")
for chunk in chain.stream("tell me about yourself in one sentence"):
    print(chunk, end="|", flush=True)