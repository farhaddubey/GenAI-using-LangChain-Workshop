import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-3.5-turbo-0125', api_key=SECRET_KEY)
class Joke(BaseModel):
    setup: str = Field(description='question to setup a joke')
    punchline: str = Field(description='answer to resolve the joke')
joke_query="Tell me a joke"
parser = JsonOutputParser(pydantic_object=Joke)
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instruction}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
chain = prompt | model | parser
chain.invoke({"query":joke_query})
for s in chain.streaming({"query":joke_query}):
    print(s)
    