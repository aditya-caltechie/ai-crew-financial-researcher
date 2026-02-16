# src/financial_researcher/crew.py
"""
Crew Implementation - Step 3 of Implementation Guide

This file wires together agents and tasks defined in config/agents.yaml and config/tasks.yaml.
It attaches tools to agents and defines the execution process (sequential or hierarchical).

Implementation Order:
1. Define agents in config/agents.yaml
2. Define tasks in config/tasks.yaml
3. Implement crew logic here (this file)
4. Create entry point in main.py
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class ResearchCrew():
    """
    Research crew for comprehensive topic analysis and reporting.
    
    The @CrewBase decorator enables automatic loading of:
    - agents_config from config/agents.yaml
    - tasks_config from config/tasks.yaml
    """

    @agent
    def researcher(self) -> Agent:
        """
        Researcher agent - loads configuration from config/agents.yaml['researcher']
        
        Tools attached:
        - SerperDevTool: Enables web search for real-time company news, financials, and market data.
          This tool is called during research_task execution. Results are passed to the Analyst
          as context. Requires SERPER_API_KEY environment variable.
        """
        return Agent(
            config=self.agents_config['researcher'],  # Loads from config/agents.yaml
            verbose=True,  # Enable detailed logging
            tools=[SerperDevTool()],  # Attach web search tool
        )

    @agent
    def analyst(self) -> Agent:
        """
        Analyst agent - loads configuration from config/agents.yaml['analyst']
        
        No tools attached - this agent focuses on analysis and writing using only its LLM.
        It receives research_task output as context (defined in config/tasks.yaml).
        """
        return Agent(
            config=self.agents_config['analyst'],  # Loads from config/agents.yaml
            verbose=True  # Enable detailed logging
        )

    @task
    def research_task(self) -> Task:
        """
        Research task - loads configuration from config/tasks.yaml['research_task']
        
        This task is assigned to the researcher agent and will execute first in sequential process.
        Output will be used as context for analysis_task.
        """
        return Task(
            config=self.tasks_config['research_task']  # Loads from config/tasks.yaml
        )

    @task
    def analysis_task(self) -> Task:
        """
        Analysis task - loads configuration from config/tasks.yaml['analysis_task']
        
        This task is assigned to the analyst agent and will execute second in sequential process.
        It receives research_task output as context (defined in tasks.yaml).
        Output is written to output/report.md.
        """
        return Task(
            config=self.tasks_config['analysis_task'],  # Loads from config/tasks.yaml
            output_file='output/report.md'  # Override or set output file location
        )

    @crew
    def crew(self) -> Crew:
        """
        Creates and returns the research crew.
        
        Process.sequential means tasks execute in order:
        1. research_task (researcher agent)
        2. analysis_task (analyst agent, receives research_task output as context)
        
        For hierarchical process, use Process.hierarchical and configure manager_llm or manager_agent.
        """
        return Crew(
            agents=self.agents,  # Auto-collected from all @agent methods above
            tasks=self.tasks,    # Auto-collected from all @task methods above
            process=Process.sequential,  # Tasks run in order, context flows forward
            verbose=True,  # Enable detailed execution logging
        )