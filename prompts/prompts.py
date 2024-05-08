# PromptTemplates are predefined recipes for generating prompts for large language model .
# LangChain provides tooling to create Prompts 
# We should use prompt template to create a template for a string prompt. 
# By default, PromptTemplate uses Python's str.format syntax for highlighting. 
import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)

from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjactive} joke about {content}"
)
formatted_prompt=prompt_template.format(adjactive="funny", content="girls")
# print(formatted_prompt)
# llm.invoke(prompt_template) 

# ChatPromptTemplate is used for chat models/or a list of chat models
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

chat_template=ChatPromptTemplate.from_messages(
    [
        ("system", "Your a extreamly, flirty, shameless ai bot. Your name is {name}"),
        ("human", "Hello, How are you doing?"), 
        ("ai", "I'm well, thanks!"),
        ("human", "{user_input}")
    ]
)
messages = chat_template.format_messages(name="Knights", user_input="what is your name? Can we make friendship with each other.")
# print(messages)
# print(llm.invoke(messages))
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "Your a extreamly, flirty, shameless, attitudeful, human like talented ai bot."
                "You please humans by your words and seduce by your flirts."
            )
        ),
        HumanMessagePromptTemplate.from_template("{text}"),
    ]
)
messages=chat_template.format_messages(text="I don't like eating tasty things")
# print(messages)
# print(llm.invoke(messages))

# Message Prompts 
# Langchain Provides different types of MessagePromptTemplate. commonly used are-
# AIMessagePromptTemplate 
# SystemMessagePromptTemplate 
# HumanMessagePromptTemplate
# that creates AI, System & Human message differently. ChatMessagePromptTemplate allows user to specify the role name. 

from langchain_core.prompts import ChatMessagePromptTemplate

prompt = "May the {subject} be with you"
chat_message_prompt=ChatMessagePromptTemplate.from_template(role="Jedi", template=prompt)
print(chat_message_prompt.format(subject="force"))

