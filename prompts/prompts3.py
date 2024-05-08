import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)

from langchain_core.prompts import PromptTemplate

# LCEL 
# PromptTemplate & ChatPromptTemplate implement the Runnable Interface the basic building block of Langchain Expression Language(LCEL). This means 
# they support invoke, ainvoke, stream, astream, batch, abatch, astream_log calls. 
# PromptTemplate accepts a dictionary (of the prompt variables) and returns a StringPromptValue. A ChatPromptTemplate accepts a dictonary and 
# returns ChatPromptValue 
prompt_template = PromptTemplate.from_template(
    "Tell me a {adjactive} joke about {content}"
)
prompt_value = prompt_template.invoke({"adjactive":"funny", "content":"chicken"})
print(prompt_value)
print(prompt_value.to_string())
print(prompt_value.to_messages())  

