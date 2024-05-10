# It's often crucial ie. very important for LLMs to return structured output. 
# That' cause often times the output of the LLMs are used in downstream applications, where specific arguments are required. 
# Components that constructs the LLM's output arae:
# Prompting 
# functionCalling 
# Tool calling  is similar like function calling but it allows to call multiple functions at once
# JSON mode

# LLMs to return structure output, a common interface to LangChain model: .with_structured_output has been used .

# By invoking this method (and passing in a JSON schema or a Pydantic model) the model will add whatever model parameters + output parsers are necessary to get back the structured output. There may be more than one way to do this (e.g., function calling vs JSON mode) - you can configure which method to use by passing into that method.

import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY=os.getenv('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI

chat =ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY)

from langchain_core.pydantic_v1 import BaseModel, Field


class Joke(BaseModel):
    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
# OpenAI exposes few different ways to get structured output.
model=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY, temperature=0)
# structured_llm=model.with_structured_output(Joke)
# print(structured_llm.invoke("Tell me a big joke about Cat"))

structured_llm2=model.with_structured_output(Joke, method="json_mode")
structured_llm2.invoke("Tell me a joke about cats, response in setup and punchline keys")
