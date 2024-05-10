# # We use the term tool calling interchagnebaly with function calling. Although function calling is meant to refer sometimes  as invocation of a 
# # single function, 
# # We treat all models as though they can return multiple tool or function calls in each message. 

# # Tool calling allows a model to response to a given prompt by generating output that matches user-defined schema. 
#  The model is coming up with the arguments to a tool, and actually running the tool (or not) is up to the user - for example, if you want to extract output matching some schema from unstructured text, you could give the model an "extraction" tool that takes parameters matching the desired schema, then treat the generated output as your final result.
# A tool call includes a name, arugment dictionary, and an optional identifier. The argument dictionary is structured {argument_name: argument_value}
# Tool calling is extreamlly useful for building tool-using chains and agents and for gettiing structured outputs from models more generally. 

# Parsed Structure 
[
  {
    "text": "<thinking>\nI should use a tool.\n</thinking>",
    "type": "text"
  },
  {
    "id": "id_value",
    "input": {"arg_name": "arg_value"},
    "name": "tool_name",
    "type": "tool_use"
  }
]
# Different Providers adopt different schemas for providing tool schema. Like the above is content block. 
# Open AI uses JSON Object. 
{
  "tool_calls": [
    {
      "id": "id_value",
      "function": {
        "arguments": '{"arg_name": "arg_value"}',
        "name": "tool_name"
      },
      "type": "function"
    }
  ]
}

# Requesting ie. passing tools to models 
# For a model to invoke tool, We need to pass schemas to it when making a chat request. 
from langchian_core.tools import tool


@tool
def add(a:int, b:int) ->int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

@tool
def substract(a:int, b:int) -> int:
    """Substract a and b
    Args:
        a:first int
        b:second int
    """
    return a-b

tools = [add, multiply, substract]

# We can equivalently define the schemas using Pydantic. Pydantic is useful when tool inputs are more complex.
from langchain_core.pydantic_v1 import BaseModel, Field


class add(BaseModel):
    """Add twoo integers together."""
    a:int = Field(..., description="First integer")
    b:int = Field(..., description="Second Integer")
class multiply(BaseModel):
    a:int = Field(..., description="First integer")
    b:int =Field(..., description="second integer")
tools =[add, multiply]

