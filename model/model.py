import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI, OpenAI

llm=OpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)
chat_model=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)

from langchain_core.messages import HumanMessage

text = "What would be the good qualities of a perfect girl friend?"
messages=[HumanMessage(content=text)]
# llm.invoke(text)
print(chat_model.invoke(messages))