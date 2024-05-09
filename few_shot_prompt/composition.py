# String  Prompt Composition 
from langchain_core.prompts import PromptTemplate

prompt = (
    PromptTemplate.from_template("Tell me a joke about {topic}")
    +", make it funny" +
    "\n and in {language}"
)
print(prompt)

print(prompt.format(topic="Science", language="Hindi"))

import os

from dotenv import load_dotenv
# from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-3.5-turbo-0125', api_key=SECRET_KEY)
# chain= LLMChain(llm=model, prompt=prompt)
chain.run(topic="sports", language="hindi")


# Using Pipeline Prompt 
# LangChain includes an abstraction PipelinePromptTemplate, which can be useful when you want to reuse parts of prompts. A PipelinePrompt consists of two main parts:

# Final prompt: The final prompt that is returned
# Pipeline prompts: A list of tuples, consisting of a string name and a prompt template. Each prompt template will be formatted and then passed to future prompt templates as a variable with the same name.
from langchain_core.prompts.pipeline import PipelinePromptTemplate
from langchain_core.prompts.prompt import PromptTemplate

full_template = """{introduction}

{example}

{start}"""
full_prompt = PromptTemplate.from_template(full_template)

introduction_template = """You are impersonating {person}."""
introduction_prompt = PromptTemplate.from_template(introduction_template)

example_template = """Here's an example of an interaction:

Q: {example_q}
A: {example_a}"""
example_prompt = PromptTemplate.from_template(example_template)

start_template = """Now, do this for real!

Q: {input}
A:"""
start_prompt = PromptTemplate.from_template(start_template)

input_prompts=[
    ("introduction", introduction_prompt),
    ("example", example_prompt),
    ("start", start_prompt)
]
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_prompt, pipeline_prompts=input_prompts
)
pipeline_prompt.input_variables
print(pipeline_prompt.format(
    person="Elon Musk",
     example_q="What's your favorite car?",
        example_a="Tesla",
        input="What's your favorite social media site?",

))