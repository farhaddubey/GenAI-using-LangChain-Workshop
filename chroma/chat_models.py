import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI, OpenAI

llm=OpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)
chat_model=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)

# FewShotChatMessagePromptTemplate 
# The goal of few shot message prompt template are to dynamically select examplese based on an Input, and then format the example in a final prompt 
# to provide the model 
# The basic component of a template are : examples and example_prompt 
# examples: A list of dictionary examples to include in final prompt 
# example_prompt: Converts each message into 1 or more message through it's format message prompt. Common example would be 1 Human & 1 AI or 1 AI or
# 1 functional call 
from langchain_core.prompts import (ChatPromptTemplate,
                                    FewShotChatMessagePromptTemplate)

examples = [
    {"input":"2+2", "output":"4"}, 
    {"input":"2+3", "output":"5"}
]
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}")
    ]
)
few_shot_prompt=FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt, 
    examples=examples
)
# print(few_shot_prompt.format())
final_prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a wondroud wizard of math"),
        few_shot_prompt, 
        ("human","{input}")
    ]
)
# from langchain_anthropic import ChatAnthropic

# chain = final_prompt | ChatAnthropic(temperature=0.0)
# chain.invoke({"input":"What's the square of a triangle?"})
# print()
# ChatAnthropic is Deprecated 


# Dynamic Few Shot Prompting 
# Sometimes we may want to condition which examples are shown based on input. For this examples can be replaced by example_selector. 
# To review the dynamic few shot prompt template would look like:
# example_selector
# example_prompt
# example_selector: responsible for selecting few shot examples (and the order in which they are returned) for a given input. These implement the 
# BaseSelectorInterface. A common example is SemanticSimilarityExampleSelector 
# example_prompt: convert each example into 1 or more messagees through it's format_message method. A common example would be to convert each 
# example into one humna message and one AI message. 

from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

examples = [
    {"input": "2+2", "output":"4"},
    {"input": "2+3", "output":"5"},
    {"input": "2+4", "output":"6"},
    {"input": "What did the cow say to the moon", "output":"Nothing at all"}
]
to_vectorize = ["".join(examples.values()) for example in examples]
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas = examples)
example_selector=SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=2
)
example_output=example_selector.select_examples({"input":"horse"})
print(example_output)

# Now We'll be creating prompt template 
from langchain_core.prompts import (ChatPromptTemplate,
                                    FewShotChatMessagePromptTemplate)

few_shot_prompt =FewShotChatMessagePromptTemplate(
    input_variables=["input"],
    example_selector=example_selector,
    example_prompt=ChatPromptTemplate.from_messages(
        [("human","{input}"), ("ai", "{output}")]
    )
)
print(few_shot_prompt.format(input="What's 3+3"))
final_prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are very good mathematician"), 
        ("human", "{input}")
    ]
)
print(few_shot_prompt.format(input="what;s up?"))
# Now LLM can also be connnected with Few Shot Prompt Template 
