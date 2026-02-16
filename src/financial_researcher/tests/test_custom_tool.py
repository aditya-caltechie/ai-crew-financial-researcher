"""Unit tests for custom tool."""
import pytest
from pydantic import ValidationError

from financial_researcher.tools.custom_tool import MyCustomTool, MyCustomToolInput


class TestMyCustomToolInput:
    """Tests for MyCustomToolInput schema."""

    def test_requires_argument(self):
        """MyCustomToolInput requires 'argument' field."""
        schema = MyCustomToolInput(argument="test value")
        assert schema.argument == "test value"

    def test_argument_validation(self):
        """MyCustomToolInput validates argument is required."""
        with pytest.raises(ValidationError):
            MyCustomToolInput()


class TestMyCustomTool:
    """Tests for MyCustomTool."""

    def test_tool_has_expected_attributes(self):
        """MyCustomTool has name, description, and args_schema."""
        tool = MyCustomTool()
        assert tool.name == "Name of my tool"
        assert "Clear description" in tool.description
        assert tool.args_schema == MyCustomToolInput

    def test_run_returns_expected_output(self):
        """MyCustomTool._run returns the example output string."""
        tool = MyCustomTool()
        result = tool._run(argument="any value")
        assert result == "this is an example of a tool output, ignore it and move along."
