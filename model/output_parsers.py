import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')
# Output Parsers convert the raw output of a language model that can be downstream. Few Output Parser are:
# Convert text from LLM to JSON
# Convert a chat message into just a string 
from langchain.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()
output_parser.parse("Hi, Bye")