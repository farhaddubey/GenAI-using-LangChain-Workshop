with open("hello.txt") as f:
    state_of_the_union=f.read()
from langchain_text_splitters import CharacterTextSplitter

textSplitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=1000,
    length_function=len,
    is_separator_regex=False
)
texts = textSplitter.create_documents([state_of_the_union])
print(texts[0])

metadatas = [{"document":1}, {"document":2}]
documents = textSplitter.create_documents(
    [state_of_the_union, state_of_the_union], metadatas=metadatas
)
print(documents[0])
