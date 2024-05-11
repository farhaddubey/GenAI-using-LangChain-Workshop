from langchain.globals import set_llm_cache
from langchain_openai import OpenAI

# To make the caching really obvious, lets use a slower model.
llm = OpenAI(model_name="gpt-3.5-turbo-instruct", n=2, best_of=2)
from langchain.cache import InMemoryCache, SQLiteCache

# set_llm_cache(InMemoryCache())
# print(llm.predict("Tell me a joke"))

set_llm_cache(SQLiteCache(database_path="lang.db"))
print(llm.predict("Tell me a joke"))