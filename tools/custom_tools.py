# When constructing your own agent, you will need to provide it with a list of tools that it can use. Beside the actual function that is called, the Tool consist of several components. 
# name (str), is required and must be unique within a set of tools provided to an agent. 
# description (str), is optional but recommended, as it's used by an agent to determine tool use. 
# args_schema (Pydantic BaseModel), is optional but recommended, can be used to provide more information (e.g., few-shot examples) or validation for expected parameters.
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool

# @tool decorator 
# This @tool decorator is the simplest way to define a custom tool. The decorator uses the function name as the tool name by default, but this can be overridden by passing a string as the first argument. Additionally, the decorator will use the function's docstring as the tool's description - so a docstring MUST be provided.
# doc string of function is used as the doc stringof tool hence __doc__ string is essential 

@tool
def search(query: str)->str:
    """Look up things online."""
    return "Langchain"
print(search.name)
print(search.description)
print(search.args)
@tool
def multiply(a:int, b:int)->int:
    """Multiply two numbers"""
    return a*b
print(multiply.name)
print(multiply.description)
print(multiply.args)
class SearchInput(BaseModel):
    query: str = Field(description="should be used search query")

@tool("search-tool", args_schema=SearchInput, return_direct=True)
def search(query: str)-> str:
    """Look up things online """
    return "Langchain"
# Subclass Base Tool 

# You can also explicitly define a custom tool by subclassing the BaseTool class. This provides maximal control over the tool definition, but is a bit more work.

from typing import Optional, Type

from langchain.callbacks.manager import (AsyncCallbackManagerForToolRun,
                                         CallbackManagerForToolRun)


class SearchInput(BaseModel):
    query :str = Field(description="should be a search query")
class CalculatorInput(BaseModel):
    a: int =Field(description="First Number")
    b: int = Field(description="Second Number")
class CustomSearchTool(BaseModel):
    name = "custom_search"
    description = "useful for when you need to answer questions about current events."
    args_schema : Type[BaseModel] = SearchInput

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        return "LangChain"

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")

class CustomCalculatorTool(BaseTool):
    name = "Calculator"
    description = "Useful when you need to answer question about math"
    args_schema: Type[BaseModel] = CalculatorInput
    return_direct: bool = True

    def _run(
        self, a: int, b: int, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        return a * b

    async def _arun(
        self,
        a: int,
        b: int,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Calculator does not support async")
search = CustomSearchTool()
print(search.name)
print(search.description)
print(search.args)
multiply = CustomCalculatorTool()
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.return_direct)
def search_function(query: str):
    return "LangChain"


search = StructuredTool.from_function(
    func=search_function,
    name="Search",
    description="useful for when you need to answer questions about current events",
    # coroutine= ... <- you can specify an async method if desired as well
)
print(search.name)
print(search.description)
print(search.args)
class CalculatorInput(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


calculator = StructuredTool.from_function(
    func=multiply,
    name="Calculator",
    description="multiply numbers",
    args_schema=CalculatorInput,
    return_direct=True,
    #
)
print(calculator.name)
print(calculator.description)
print(calculator.args)
from langchain_core.tools import ToolException


def search_tool1(s: str):
    raise ToolException("The search tool1 is not available.")
search = StructuredTool.from_function(
    func=search_tool1,
    name="Search_tool1",
    description="A bad tool",
)

search.run("test")
search = StructuredTool.from_function(
    func=search_tool1,
    name="Search_tool1",
    description="A bad tool",
    handle_tool_error=True,
)

search.run("test")
def _handle_error(error: ToolException) -> str:
    return (
        "The following errors occurred during tool execution:"
        + error.args[0]
        + "Please try another tool."
    )


search = StructuredTool.from_function(
    func=search_tool1,
    name="Search_tool1",
    description="A bad tool",
    handle_tool_error=_handle_error,
)

search.run("test")