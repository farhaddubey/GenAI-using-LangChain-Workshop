# A retriever is an interace that returns documents given an unsturctured query. 
import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

template = """Answer the question based on the following context:
{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI(model='gpt-3.5-turbo-0125' , api_key=SECRET_KEY)

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

chain = (
    {"context":  format_docs, "question":RunnablePassthrough()}
    | prompt | model | StrOutputParser()
)
print(chain.invoke("What did the president say about technology?"))