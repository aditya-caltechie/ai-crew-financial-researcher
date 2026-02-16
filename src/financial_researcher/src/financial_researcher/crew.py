# src/financial_researcher/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class ResearchCrew():
    """Research crew for comprehensive topic analysis and reporting"""

    @agent
    def researcher(self) -> Agent:
        # SerperDevTool: enables the Researcher to query the web in real time. Used so the agent
        # can fetch current company news, financials, and market data (not in the LLM's training
        # cut-off). The agent calls this tool during the research_task; results are passed to the
        # Analyst as context. Requires SERPER_API_KEY in the environment.
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['analysis_task'],
            output_file='output/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the research crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )