"""Unit tests for crew module."""
import pytest
from crewai import Agent, Crew, Process, Task

from financial_researcher.crew import ResearchCrew


class TestResearchCrew:
    """Tests for ResearchCrew."""

    def test_researcher_returns_agent(self):
        """researcher() returns an Agent instance with tools."""
        crew_instance = ResearchCrew()
        agent = crew_instance.researcher()
        assert isinstance(agent, Agent)
        assert agent.role is not None
        assert len(agent.tools) > 0

    def test_analyst_returns_agent(self):
        """analyst() returns an Agent instance without tools."""
        crew_instance = ResearchCrew()
        agent = crew_instance.analyst()
        assert isinstance(agent, Agent)
        assert agent.role is not None

    def test_research_task_returns_task(self):
        """research_task() returns a Task instance."""
        crew_instance = ResearchCrew()
        task = crew_instance.research_task()
        assert isinstance(task, Task)
        assert task.description is not None

    def test_analysis_task_returns_task(self):
        """analysis_task() returns a Task with output_file set."""
        crew_instance = ResearchCrew()
        task = crew_instance.analysis_task()
        assert isinstance(task, Task)
        assert task.output_file == "output/report.md"
        assert task.description is not None

    def test_crew_returns_crew_instance(self):
        """crew() returns a Crew instance with sequential process."""
        crew_instance = ResearchCrew()
        crew = crew_instance.crew()
        assert isinstance(crew, Crew)
        assert crew.process == Process.sequential
        assert len(crew.agents) == 2
        assert len(crew.tasks) == 2
