# "semantically related" means could depend on the type of text. 
# At a high level, text splitters work as following:

# Split the text up into small, semantically meaningful chunks (often sentences).
# Start combining these small chunks into a larger chunk until you reach a certain size (as measured by some function).
# Once you reach that size, make that chunk its own piece of text and then start creating a new chunk of text with some overlap (to keep context between chunks).
# That means there are two different axes along which you can customize your text splitter:

# How the text is split
# How the chunk size is measured
from langchain_text_splitters import (HTMLHeaderTextSplitter,
                                      RecursiveCharacterTextSplitter)

html_string = """
<!DOCTYPE html>
<html>
<body>
    <div>
        <h1>Foo</h1>
        <p>Some intro text about Foo.</p>
        <div>
            <h2>Bar main section</h2>
            <p>Some intro text about Bar.</p>
            <h3>Bar subsection 1</h3>
            <p>Some text about the first subtopic of Bar.</p>
            <h3>Bar subsection 2</h3>
            <p>Some text about the second subtopic of Bar.</p>
        </div>
        <div>
            <h2>Baz</h2>
            <p>Some text about Baz</p>
        </div>
        <br>
        <p>Some concluding text about Foo</p>
    </div>
</body>
</html>
"""
headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"), 
    ("h3", "Header 3"),
]
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text(html_string)
print(html_header_splits)

url = "https://plato.stanford.edu/entries/goedel/"
headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"), 
    ("h3", "Header 3"),
    ("h4", "Header 4")
]
html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
html_header_splits = html_splitter.split_text_from_url(url)

chunk_size =500
chunk_overlap = 30
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)
splits = text_splitter.split_documents(html_header_splits)
print(splits[80:85])
