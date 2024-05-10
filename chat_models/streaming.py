# Streaming 

import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY=os.getenv('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI

chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

from langchain_community.chat_models import ChatAnthropic
from langchain_core.messages import HumanMessage, SystemMessage

for chunk in chat.stream("Write me a song about goldfish in the moon?"):
    print(chunk.content, end="", flush=True)

