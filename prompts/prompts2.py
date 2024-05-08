import os

from dotenv import load_dotenv

load_dotenv()
SECRET_KEY_OPENAI=os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=SECRET_KEY_OPENAI)

# MessagePlaceholder
# LangChain also provides MessagePlaceholder, which gives you full control of what messages to be rendered during formatting. 
from langchain_core.prompts import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    MessagesPlaceholder, PromptTemplate)

human_prompt = "Summarize our conversations so far in {word_count} words."
human_message_template=HumanMessagePromptTemplate.from_template(human_prompt)
chat_prompt=ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name="conversation"),    human_message_template])

from langchain_core.messages import AIMessage, HumanMessage

human_message=HumanMessage(content="What's the best way to learn programming")
ai_message = AIMessage(content="""
            1. Choose Programming language. 
            2. start with the basics 
            3. Practice, practice, practice 
""")
chat_msg=chat_prompt.format_prompt(conversation=[human_message, ai_message], word_count="10").to_messages()
print(chat_msg)

