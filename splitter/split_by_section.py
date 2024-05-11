# from langchain_text_splitters import HTMLSectionSplitter

# html_string = """
#     <!DOCTYPE html>
#     <html>
#     <body>
#         <div>
#             <h1>Foo</h1>
#             <p>Some intro text about Foo.</p>
#             <div>
#                 <h2>Bar main section</h2>
#                 <p>Some intro text about Bar.</p>
#                 <h3>Bar subsection 1</h3>
#                 <p>Some text about the first subtopic of Bar.</p>
#                 <h3>Bar subsection 2</h3>
#                 <p>Some text about the second subtopic of Bar.</p>
#             </div>
#             <div>
#                 <h2>Baz</h2>
#                 <p>Some text about Baz</p>
#             </div>
#             <br>
#             <p>Some concluding text about Foo</p>
#         </div>
#     </body>
#     </html>
# """

# headers_to_split_on = [("h1", "Header 1"), ("h2", "Header 2")]

# html_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)
# html_header_splits = html_splitter.split_text(html_string)
# print(html_header_splits)

from langchain.text_splitter import RecursiveCharacterTextSplitter

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
    ("h4", "Header 4"),
]

html_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)

html_header_splits = html_splitter.split_text(html_string)

chunk_size = 500
chunk_overlap = 30
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)

# Split
splits = text_splitter.split_documents(html_header_splits)
print(splits)