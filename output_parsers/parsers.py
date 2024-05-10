# # # Output parser are reasonable for taking the output of an LLM and transforming it to a more suitable format. That's very useful when we are using 
# # # LLMs to generate any form of structured data. 
# # # Besideds having a large collection of output parsers, One distinguishing benefit of output parsers is that many of them support streaming. 
# # # Language models output text. But many times we want to get more structured information then just texts back. This is useful when output parsers 
# # # come in   
# # # Output parsers are actually classes that help structure language model responses. There are two main methods an output parser must implement:
# # "Get Format Insturctions"
# # "Parse"
# # "Get format instructions": A method which returns a string containing instructions for how the output of a language model should be formatted.
# # "Parse": A method which takes in a string (assumed to be the response from a language model) and parses it into some structure.
# "Parse with prompt": A method which takes in a string (assumed to be the response from a language model) and a prompt (assumed to be the prompt that generated such a response) and parses it into some structure. The prompt is largely provided in the event the OutputParser wants to retry or fix the output in some way, and needs information from the prompt to do so.

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field, validator
from langchain_openai import OpenAI

model = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.0)
# Defining my desired data structure. 
class Joke(BaseModel):
    setup: str = Field(description="Question to setup a joke")
    punchline: str  =Field(description="Answer to resolve the joke")
    @validator("setup")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly Formatted Question")
        return field
# Set up a parser + Injecting instructions into the prompt template 
parser = PydanticOutputParser(pydantic_object=Joke)
prompt=PromptTemplate(
    template="Anser the query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

prompt_and_model = prompt | model
output = prompt_and_model.invoke({"query":"Tell me a joke"})
print(parser.invoke(output))
parser.invoke(output)
chain = prompt | model | parser
chain.invoke({"query":"Tell me a joke."})
# The SimpleJsonOutputParser for example can stream through partial outputs: 
json_prompt = PromptTemplate.from_template(
    "Return a json object with an answer 'key' that answers the following questions: {question}"
)
from langchain.output_parsers.json import SimpleJsonOutputParser

json_parser = SimpleJsonOutputParser()
json_chain = json_prompt | model | json_parser
print(list(json_chain.stream({"question": "who invented the microscope?"})))
print(list(chain.stream({"query":"Tell me a joke."})))
