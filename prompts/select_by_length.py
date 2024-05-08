import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)


from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

#Example of Pretent task of creating antonyms 
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\n Output: {output}",
)
example_selector = LengthBasedExampleSelector(
    examples=examples ,#our defined examples library to choose from 
    example_prompt=example_prompt , #PromptTemplate being used to format the examples 
    max_length=25 ,  #the functions used to get the length of a string, which is used to determine which examples to inlcude 
)
dynamic_prompt = FewShotPromptTemplate(
    # We provide an Example Selector instead of examples 
    example_selector=example_selector,
    example_prompt=example_prompt, 
    prefix="Give me the antonym of every input", 
    suffix="Input:{adjectie}\nOutput",
    input_variables=["adjective"]
)
print(dynamic_prompt.format(adjective="big"))

# An example with long input, so it selects only one example.
long_string = "big and huge and massive and large and gigantic and tall and much much much much much bigger than everything else"
print(dynamic_prompt.format(adjective=long_string))


# You can add an example to an example selector as well.
new_example = {"input": "big", "output": "small"}
dynamic_prompt.example_selector.add_example(new_example)
print(dynamic_prompt.format(adjective="enthusiastic"))