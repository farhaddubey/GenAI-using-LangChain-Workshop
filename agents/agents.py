import os

from dotenv import load_dotenv

load_dotenv()
TAVILY_SECRET_KEY=os.getenv('TAVILY_API_KEY')

from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()
res=search.invoke("What is the weatherr is Australia?")
print(res)

# Retriever 
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader =  WebBaseLoader("https://docs.smith.langchain.com/overview/")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(
    chunk_size = 1000, chunk_overlap=200
).split_documents(docs)
vector = FAISS.from_documents(documents, OpenAIEmbeddings)
retriever = vector.as_retriever()
res1= retriever.invoke("How to upload a dataset")[0]
print(res1)

