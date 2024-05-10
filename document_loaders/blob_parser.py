# BaseBlobParser:
# A BaseBlobParser is an interface that accepts a blob  and outputs a list of document objects. 
# A blob is a representation of data that lives either in memory or in files. Langchain Python has a Blob primitive which is inspired by the Blob
# Web API 
from typing import Iterator

from langchain_core.document_loaders import BaseBlobParser, Blob
from langchain_core.documents import Document


class MyParser(BaseBlobParser):
    """A simple parser that creates a document from each line."""
    def lazy_parse(self, blob: Blob) -> Iterator[Document]:
        """Blob is parsed into document line by line"""
        line_number = 0
        with blob.as_bytes_io() as f:
            for line in f:
                line_number +=1
                yield Document(
                    page_content=line, 
                    metadata={"line_number":line_number, "source":blob.source}
                )
blob = Blob.from_path("./meow.txt")
parser=MyParser()
print(list(parser.lazy_parse(blob)))

blob = Blob.from_path("./meow.txt", metadata={"foo":"bar"})
print(blob.encoding)
print(blob.as_bytes())
print(blob.as_string())
print(blob.as_bytes_io())
print(blob.metadata)
print(blob.source)

from langchain_community.document_loaders.blob_loaders import \
    FileSystemBlobLoader

blob_loader = FileSystemBlobLoader(path=".", glob="*.mdx", show_progress=True)
parser = MyParser()
for blob in blob_loader.yield_blobs():
    for doc in parser.lazy_parse(blob):
        print(doc)
        break
from langchain_community.document_loaders.generic import GenericLoader

loader = GenericLoader.from_filesystem(
    path=".", glob="*.mdx", show_progress=True, parser=MyParser()
)

for idx, doc in enumerate(loader.lazy_load()):
    if idx < 5:
        print(doc)

print("... output truncated for demo purposes")

from typing import Any


class MyCustomLoader(GenericLoader):
    @staticmethod
    def get_parser(**kwargs: Any) -> BaseBlobParser:
        """Override this method to associate a default parser with the class."""
        return MyParser()
    
loader = MyCustomLoader.from_filesystem(path=".", glob="*.mdx", show_progress=True)

for idx, doc in enumerate(loader.lazy_load()):
    if idx < 5:
        print(doc)

print("... output truncated for demo purposes")