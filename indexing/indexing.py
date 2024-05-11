from langchain.indexes import SQLRecordManager, index
from langchain_core.documents import Document
from langchain_elasticsearch import ElasticsearchStore
from langchain_openai import OpenAIEmbeddings

# Initializing the Vector store and Setting up the embeddings..
collection_name="test_index"
embedding = OpenAIEmbeddings()
vectorstore = ElasticsearchStore(
    es_url="http://localhost:9200", index_name="test_index", embedding=embedding
)
namespace=f"elasticsearch/{collection_name}"
record_manager = SQLRecordManager(
    namespace, db_url="sqlite://record_manager_cache.sql"
)
# We need create a schema before using the record manager 
record_manager.create_schema()
#Now indexing some text docuemts
doc1 = Document(page_content="Kitty", metadata={"source":"kitty.txt"})
doc2 = Document(page_content="doggy", metadata={"source":"doggy.txt"})
# Indexing into an empty vectorstore
def _clear():
    """Hacky Helper method to clear content. See the `full` mode section to understand why it works."""
    index([], record_manager, vectorstore, cleanup="full", source_id_key="source")
_clear()
index(
    [doc1, doc1, doc1, doc1, doc1],
    record_manager, 
    vectorstore,
    cleaning=None,
    source_id_key="source"
)
_clear()
res1=index([doc1, doc2], record_manager, vectorstore, cleanup=None, source_id_key="source")
print(res1)
res2=index([doc1, doc2], record_manager, vectorstore, cleanup=None, source_id_key="source")
print(res2)
# "incremental" deletion mode  
_clear()
index(
    [doc1, doc2], 
    record_manager, 
    vectorstore,
    cleanup="incremental",
    source_id_key="source"
)
# Indexing again should result in both documents getting skipped. 
index(
    [doc1, doc2],
    record_manager,
    vectorstore,
    cleanup="incremental",
    source_id_key="source"
)
index([], record_manager, vectorstore, cleanup="incremental", source_id_key="source")
change_doc_2=Document(page_content="puppy", metadata={"source":"doggy.txt"})
index(
    [change_doc_2],
    record_manager,
    vectorstore,
    cleanup="incremental",
    source_id_key="source"
)
# "full" deletion mode 
_clear()
all_docs=[doc1, doc2]
index(all_docs, record_manager, vectorstore, cleanup="full", source_id_key="source")
# Say some one deleted the 1st doc 
del all_docs[0]
all_docs
# Using full mode will clean up the deleted content as well  
from langchain_text_splitters import CharacterTextSplitter

doc1 = Document(
    page_content="Kitty kitty kitty kitty kitty", metadata={"source":"kitty.txt"}

)
doc2 = Document(page_content="doggy doggy the doggy", metadata={"source":"doggy.txt"})
new_docs =CharacterTextSplitter(
    separator="t", keep_separator=True, chunk_size=12, chunk_overlap=2
).split_documents([doc1, doc2])
_clear()
index(
    new_docs,
    record_manager,
    vectorstore,
    cleanup="incremental",
    source_id_key="source"
)


