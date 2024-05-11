import os

from dotenv import load_dotenv
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

output_parser=CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="List five {subject} \n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions},
)
model = ChatOpenAI(model='gpt-3.5-turbo-0125', api_key=SECRET_KEY)
chain = prompt | model | output_parser
res=chain.invoke({"subject":"Ice Cream Flavour"})
print(res)
for s in chain.stream({"subject": "ice cream flavours"}):
    print(s)