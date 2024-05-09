import os

from dotenv import load_dotenv

load_dotenv()
OPENAI_SECRET_KEY=os.getenv('OPENAI_API_KEY')

# LangChain supports this in two ways:

# Partial formatting with string values.
# Partial formatting with functions that return string values.
from langchain_core.prompts import PromptTemplate

prompt=PromptTemplate.from_template("{foo}{bar}")
partial_prompt=prompt.partial(foo="foo")
print(partial_prompt.format(bar="Hello"))

# We can also initializer the variables with initialized prompt 
prompt=PromptTemplate(
    template="{foo}{bar}", input_variables=["bar"], partial_variables={"foo":"foo"}
)
print(prompt.format(bar="Hey there!"))

from datetime import datetime


def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

prompt = PromptTemplate(
    template="Tell me a {adjective} joke about the day {date}",
    input_variables=["adjective", "date"],
)
partial_prompt = prompt.partial(date=_get_datetime)
print(partial_prompt.format(adjective="funny"))

prompt = PromptTemplate(
    template="Tell me a {adjective} joke about the day {date}",
    input_variables=["adjective"],
    partial_variables={"date": _get_datetime},
)
print(prompt.format(adjective="funny"))