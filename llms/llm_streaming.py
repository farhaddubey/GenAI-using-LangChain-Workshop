from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0, max_tokens=500)
for chunk in llm.stream("Write me about the sexual desire and fantasy of females?"):
    print(chunk, end="", flush=True)
    