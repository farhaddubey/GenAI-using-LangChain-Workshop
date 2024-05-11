import os

from dotenv import load_dotenv

SECRET_KEY=os.getenv('OPENAI_API_KEY')
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS, faiss
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

raw_documents = TextLoader('state_of_the_union.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db = FAISS.from_documents(documents, OpenAIEmbeddings)
print(db)
query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)
print(docs[0].page_content)