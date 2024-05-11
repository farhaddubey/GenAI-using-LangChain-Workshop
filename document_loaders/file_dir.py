from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import \
    AzureAIDocumentIntelligenceLoader

# loader = DirectoryLoader('../', glob='**/*.md')
# docs = loader.load()
# len(docs)

# To show a progress bar We have to use the tqdm library. & set the show_progress parameter to True 
# loader = DirectoryLoader('../', glob="**/*.md", show_progress=True)
# docs = loader.load()

# loader = DirectoryLoader('../', glob="**/*.md", use_multithreading=True)
# docs = loader.load()

file_path="<filepath>"
endpoint="<endpoint>"
key="<key>"
loader = AzureAIDocumentIntelligenceLoader(
    api_endpoint=endpoint, api_key=key, file_path=file_path, api_model="prebuilt-layout"
)

documents = loader.load()