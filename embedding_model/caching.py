# Caching 
# Embeddings can be stored or temporarily cached to avoid needing to recompute them. 
# Caching embeddings can be done using a CacheBackedEmbeddings. The cache backed embedder is a wrapper around an embedder that caches embeddings in a key-value store. The text is hashed and the hash is used as the key in the cache.

# The main supported way to initialize a CacheBackedEmbeddings is from_bytes_store. It takes the following parameters:

# underlying_embedder: The embedder to use for embedding.
# document_embedding_cache: Any ByteStore for caching document embeddings.
# batch_size: (optional, defaults to None) The number of documents to embed between store updates.
# namespace: (optional, defaults to "") The namespace to use for document cache. This namespace is used to avoid collisions with other caches. For example, set it to the name of the embedding model used.

from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS, faiss
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

underlying_embeddings = OpenAIEmbeddings()
store = LocalFileStore("./cache/")
cache_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, store, namespace=underlying_embeddings.model
)
print(list(store.yield_keys()))

raw_documents = TextLoader("./state_of_the_union.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db =FAISS.from_documents(documents, cache_embedder)
print(db)
list(store.yield_keys())[:5]
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import InMemoryByteStore

store = InMemoryByteStore()

cached_embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, store, namespace=underlying_embeddings.model
)
