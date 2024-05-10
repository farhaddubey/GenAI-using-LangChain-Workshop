from langchain_community.document_loaders import TextLoader

loader = TextLoader('./hello.txt')
res = loader.load()
print(res)

# Document: Contains texts and metadata 
# BaseLoader: Use to convert raw data into documents.
# Blob: A representation of binary data that's located either in a file or in a memory. 
# BaseBlobLoader: Logic to parse a blob to yield Document object. 

# lazy_load: Used to load documents one by one lazily 
# load: Used to load all documents into memory eagerly
# list(self.lazy_load()) 
from typing import AsyncIterable, Iterator

from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document


class CustomDocumentLoader(BaseLoader):
    """An example document loader that reads a file line be line."""
    def __init__(self, file_path: str) -> None:
        """Initialize the loader with a file path."""
        self.file_path = file_path
    def lazy_load(self) ->Iterator[Document]: #Does not take any arguments 
        """A lazy loader that reads a file line by line."""
        with open(self.file_path, encoding="utf-8") as f:
            line_number = 0
            for line in f:
                yield Document(
                    page_content=line, 
                    metadata={"line_number":line_number, "source":self.file_path}
                )
                line_number+=1
    # alazy_load is OPTIONAL 
    async def alazy_load(self)->AsyncIterable[Document]:
        import aiofiles
        async with aiofiles.open(self.file_path, encoding="utf-8") as f:
            line_number = 0
            async for line in f:
                yield Document(
                    page_content=line, 
                    metadata={"line_number":line_number, "source":self.file_path}
                )
                line_number+=1
with open("./meow.txt", "w", encoding="utf-8") as f:
    quality_content = "meow meow🐱 \n meow meow🐱 \n meow😻😻"
    f.write(quality_content)

loader = CustomDocumentLoader("./meow.txt")
for doc in loader.lazy_load():
    print()
    print(type(doc))
    print(doc)
## Test out the async implementation
async for doc in loader.alazy_load():
    print()
    print(type(doc))
    print(doc)