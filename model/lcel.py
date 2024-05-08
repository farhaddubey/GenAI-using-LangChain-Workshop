import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')
# All discussed till can be combined into one chain. This Chain will take input variables, pass those to a prompt template to create a prompt, 
# pass the prompt to a language model and then pass the output through output_parser.
from langchain_core.prompts.chat import ChatPromptTemplate

chat_model=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)

template = "Generate a list of 5 {text}. \n\n{format_instructions}"

chat_prompt = ChatPromptTemplate.from_template(template)
chat_prompt = chat_prompt.partial(format_instructions=output_parser.get_format_instructions())
chain = chat_prompt | chat_model | output_parser 
chain.invoke({"text": "colors"})


