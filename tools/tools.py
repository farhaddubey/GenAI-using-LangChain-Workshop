# # Tools are interfaces that an agent, chain or llm can use to interact with the world.
# # Tools combine of a few things: 
# 1. The Name of the tool 
# 2. A description of what the tool is 
# 3. JSON schema of what the inputs to the tool are 
# 4. the function to call 
# 5. Whether the result of a tool should be returned directly to the user 
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
tool = WikipediaQueryRun(api_wrapper=api_wrapper)
print(tool.name)
print(tool.description)
print(tool.args)
tool.run({"query":"langchain"})
# This tool can be run or called with a dictionary or a single input. 
tool.run("langchain")
# Now we'll be customizing the default tools  
from langchain_core.pydantic_v1 import BaseModel, Field


class WikiInputs(BaseModel):
    """Inputs to the Wikipedia tool."""
    query: str = Field(
        description="query to look up in wikipedia, should be 3 or less words."
    )
tool=WikipediaQueryRun(
    name="wiki-tool",
    description="look up things in wikipedia",
    args_schema=WikiInputs,
    api_wrapper=api_wrapper,
    return_direct=True
)
print("\n")
print(tool.name)
print(tool.description)
print(tool.args)
