import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-0125").bind(logprobs=True)
msg = llm.invoke(("human", "How are you today?"))
print(msg.response_metadata)
print(msg.response_metadata["logprobs"]["content"][:5])
# !pip install -qU langchain-community wikipedia

from langchain_community.callbacks.manager import get_openai_callback

with get_openai_callback() as cb:
    result = llm.invoke("Tell me a joke")
    print(cb)

# from langchain.agents import (AgentExecutor, create_tool_calling_agent,
#                               load_tools)
# from langchain_core.prompts import ChatPromptTemplate

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You're a helpful assistant"),
#         ("human", "{input}"),
#         ("placeholder", "{agent_scratchpad}"),
#     ]
# )
# tools = load_tools(["wikipedia"])
# agent = create_tool_calling_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(
#     agent=agent, tools=tools, verbose=True, stream_runnable=False
# )    
