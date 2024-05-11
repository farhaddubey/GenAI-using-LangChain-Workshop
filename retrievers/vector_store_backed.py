from langchain_community.document_loaders import TextLoader

loader = TextLoader("../../state_of_the_union.txt")
import os

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings(model='gpt-3.5-turbo-0125', api_key=SECRET_KEY)
db = FAISS.from_documents(texts, embeddings)
retriever = db.as_retriever()
docs = retriever.invoke("what did he say about ketanji brown jackson")
print(docs)

retriever = db.as_retriever(search_type="mmr")
docs = retriever.invoke("what did he say about ketanji brown jackson")
retriever = db.as_retriever(
    search_type="similarity_score_threshold", search_kwargs={"score_threshold": 0.5}
)

docs = retriever.invoke("what did he say about ketanji brown jackson")
retriever = db.as_retriever(search_kwargs={"k": 1})
docs = retriever.invoke("what did he say about ketanji brown jackson")
len(docs)