"""
Custom Tool Template - Optional Step

This is a template for creating custom tools that agents can use.
Tools are attached to agents in crew.py (Step 3), not in agents.yaml.

To use a custom tool:
1. Implement your tool class here (extend BaseTool)
2. Import it in crew.py
3. Attach it to an agent: tools=[MyCustomTool()]

Example: If you need a tool to fetch stock prices, create StockPriceTool here,
then attach it to the researcher agent in crew.py.
"""
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    """
    Template for custom tools.
    
    Required attributes:
    - name: Tool name (used by agent to call it)
    - description: What the tool does (agent uses this to decide when to use it)
    - args_schema: Input validation schema
    - _run: Implementation of tool logic
    """
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
