from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(file_path="A:/Downloads/wholesale-trade-survey-december-2023-quarter-csv.csv")
data = loader.load()
print(data)