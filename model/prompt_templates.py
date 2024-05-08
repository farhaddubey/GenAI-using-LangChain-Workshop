# Most LLM Applications don't usually pass input directly into an LLM. Usually they add their input into large piece of text called Prompt Template.
# that provides additional context on the specific task at hand. 
# Prompt Template bundle up all logics for goiing from user input into a fully formatted prompt. 
import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')

from langchain_core.prompts import PromptTemplate

prompt=PromptTemplate.from_template("What's the best AI based {company}?")
prompt.format(company="image generation model")
print(prompt)

# PromptTemplate can also be used to produce a list of messages. In this case, prompt contains each messages role posiotion in chat 
# ChatPromptTemplate is a list of ChatMessageTemplates. Each chat messages contains instructions for how to format the chat message role 
from langchain_core.prompts.chat import ChatPromptTemplate

template="You are a helpful assistant that translates {input_language} to {output_language}."
human_template="{text}"
chat_prompt=ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template)
])
chat_prompt_pr=chat_prompt.format_messages(input_language="English", output_language="French", text="I love Programming")
print(chat_prompt_pr)
