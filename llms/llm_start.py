import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

from langchain_openai import OpenAI

llm = OpenAI( api_key=SECRET_KEY)

res=llm.invoke("What are some theories about the relationship between unemployment and inflation?")
print(res)
for chunk in llm.stream("What are some theories about the relationship between unemployment and inflation?"):
    print(chunk, end="", flush=True)
    
