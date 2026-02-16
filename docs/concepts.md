# CrewAI Concepts — Basics

## CrewAI Open-Source Framework

CrewAI is an open-source framework for orchestrating autonomous AI agents. It lets you build multi-agent systems where specialized agents collaborate to accomplish complex tasks. The framework is built around two main high-level concepts: **Flow** and **Crew**. This project focuses on **Crew**.

---

## Crew vs Flow

| Concept | Purpose |
|---------|---------|
| **Flow** | The backbone for the overall application: control flow (conditionals, loops, branching), event-driven execution, and state persistence. Flows act as the "manager" that delegates work to crews and coordinates complex workflows. |
| **Crew** | A team of autonomous agents working together on a set of tasks. A crew performs the heavy lifting—research, analysis, writing—and returns results to the caller (or to a Flow). |

For simpler use cases, you can run a **Crew** directly without a Flow. A **Flow** is useful when you need multiple crews, branching logic, or state management across runs.

This project uses **Crew only**—no Flow—so we run a single crew that executes a fixed sequence of tasks.

---

## Crew: Team of Agents and Tasks

A **Crew** is the core unit of work. It is a team made up of:

1. **Agents** — the team members
2. **Tasks** — the work items
3. **Process** — how tasks are executed (e.g., sequential or hierarchical)

```
┌─────────────────────────────────────────────────────────┐
│                      CREW                                │
│  ┌─────────────────────────────────────────────────┐   │
│  │  AGENTS (the team members)                       │   │
│  │  • researcher, analyst, writer, ...              │   │
│  └─────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────┐   │
│  │  TASKS (the work items)                          │   │
│  │  • research_task, analysis_task, ...             │   │
│  └─────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────┐   │
│  │  PROCESS (how tasks run)                         │   │
│  │  • sequential, hierarchical                      │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## Agent

An **Agent** is an AI team member with:

- **Role** — what they do (e.g., "Senior Financial Researcher")
- **Goal** — what they aim to achieve
- **Backstory** — background that shapes their behavior
- **LLM** — the language model they use (e.g., GPT-4, Llama)
- **Tools** (optional) — capabilities like search, file read, API calls

Agents decide how to complete tasks using their role, goal, backstory, and tools. Each task is assigned to a specific agent.

---

## Task

A **Task** is a concrete piece of work with:

- **Description** — what needs to be done
- **Expected output** — what “done” looks like
- **Agent** — who performs it
- **Context** (optional) — outputs from other tasks used as input
- **Output file** (optional) — where to save the result

Tasks can depend on each other via **context**. For example, the analysis task receives the research task’s output as context.

---

## How It Fits Together

```
Crew
  ├── Agent 1 (researcher)  →  executes  →  Task 1 (research)
  │                                              │
  │                                              ▼
  │                                         output (research doc)
  │                                              │
  ├── Agent 2 (analyst)    ←  receives context  ←┘
  │         │
  │         ▼
  │    Task 2 (analysis)
  │         │
  │         ▼
  └    output (report)
```

The crew executes tasks according to the **process**. With a sequential process, tasks run in order and each task can use prior task outputs as context.

---

## Code Flow in This Project

### 1. Entry Point

`main.py` is the entry point. It builds the crew and kicks it off with inputs:

```python
# main.py
inputs = {'company': 'Tesla'}
result = ResearchCrew().crew().kickoff(inputs=inputs)
```

### 2. Crew Definition

`crew.py` defines the crew using `@CrewBase` and decorators:

```python
# crew.py
@CrewBase
class ResearchCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(config=self.agents_config['researcher'], tools=[SerperDevTool()])

    @agent
    def analyst(self) -> Agent:
        return Agent(config=self.agents_config['analyst'])

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_task'], output_file='output/report.md')

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,    # collected from @agent methods
            tasks=self.tasks,      # collected from @task methods
            process=Process.sequential,
        )
```

### 3. Config Files

Agent and task details live in YAML. Placeholders like `{company}` are filled from `inputs`:

```yaml
# config/agents.yaml
researcher:
  role: Senior Financial Researcher for {company}
  goal: Research the company, news and potential for {company}
  # ...

# config/tasks.yaml
research_task:
  description: Conduct thorough research on company {company}. Focus on: ...
  agent: researcher
```

### 4. Execution Sequence

```
main.run()
    │
    ▼
ResearchCrew().crew().kickoff(inputs={'company': 'Tesla'})
    │
    ├── Load agents from agents.yaml (researcher, analyst)
    ├── Load tasks from tasks.yaml (research_task, analysis_task)
    ├── Substitute {company} → "Tesla"
    │
    ▼
Process.sequential:
    │
    ├── Task 1: research_task
    │       Agent: researcher
    │       Uses: SerperDevTool (web search)
    │       Output: research document
    │
    ▼
    ├── Task 2: analysis_task
    │       Agent: analyst
    │       Context: [research_task output]
    │       Output: writes to output/report.md
    │
    ▼
return CrewOutput (result.raw = final report content)
```

### 5. Data Flow

```
inputs = {'company': 'Tesla'}
         │
         ▼
    ┌─────────────┐
    │ research_task │  researcher uses SerperDevTool
    └──────┬──────┘
           │ research document (raw text)
           ▼
    ┌─────────────┐
    │ analysis_task │  analyst receives research as context
    └──────┬──────┘
           │
           ▼
    output/report.md  +  result.raw (returned to caller)
```

---

## Summary

| Concept | In This Project |
|---------|-----------------|
| **CrewAI** | Open-source framework for multi-agent orchestration |
| **Crew vs Flow** | We use Crew only; Flow is for more complex orchestration |
| **Crew** | Team of agents + tasks + process |
| **Agent** | Researcher and Analyst, defined in `config/agents.yaml` |
| **Task** | research_task and analysis_task, defined in `config/tasks.yaml` |
| **Process** | Sequential — tasks run in order, context flows forward |
| **Code flow** | `main.py` → `ResearchCrew().crew().kickoff()` → tasks execute → report written |
