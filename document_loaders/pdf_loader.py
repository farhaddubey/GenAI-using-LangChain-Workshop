from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./Resume.SDE.Final.FarhadDubey.pdf")
pages = loader.load_and_split()
print(pages[0])

import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
docs = faiss_index.similarity_search("What are the languages", k=2)
for doc in docs:
    print(str(doc.metadata["page"])+":", doc.page_content[:300])
    