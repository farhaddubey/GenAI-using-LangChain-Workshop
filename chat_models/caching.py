# Caching is benefitial for two reasons:
#     1. It can save your money by reducing the no. of API calls that is made to the LLM provide. 
#     2. It can also speed up the application by reducing the no. of API calls. 
import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY=os.getenv('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI

llm =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache

set_llm_cache(InMemoryCache())
# print(llm.predict("tell me a joke"))

# We can do the same thing with a SQLite cache
from langchain_community.cache import SQLiteCache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))
print(llm.invoke("tell me a joke")
)