from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

print([e.value for e in Language])
print(RecursiveCharacterTextSplitter.get_separators_for_language(Language.JAVA))

PYTHON_CODE = """
def hello_world():
    print("Hello, World")
# Call the function 
hello_world()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
print(python_docs)

TS_CODE = """
function helloWorld():void{
    console.log("Hello, World!")
}
// Call the function 
helloWorld();
"""
ts_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.TS, chunk_size=50, chunk_overlap=0    
)
ts_docs = ts_splitter.create_documents([TS_CODE])
print(ts_docs)

