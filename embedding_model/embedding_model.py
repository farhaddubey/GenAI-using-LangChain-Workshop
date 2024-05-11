# # Embeddings create a vector representation of piece of text.
# Base EMbedding class in Langchain provides two methods. 
# 1.One for Embedding documents. 
# 2.One for Embedding a query.
import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY=os.getenv('OPENAI_API_KEY')
from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(api_key=SECRET_KEY)
embeddings = embeddings_model.embed_documents(
    [
         "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
print(len(embeddings), len(embeddings[0]))

embedded_query=embeddings_model.embed_query("What was the name mentioned in the Conversation?")
embedded_query[:5]
