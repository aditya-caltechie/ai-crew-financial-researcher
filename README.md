# Financial Researcher

A multi-agent AI application that performs comprehensive financial research and reporting on companies using the [CrewAI](https://github.com/joaomdmoura/crewai) open-source framework. Two specialized agents collaborate: a **Researcher** gathers data via web search, and an **Analyst** synthesizes it into a structured markdown report.

**CrewAI** is a Python framework for orchestrating autonomous AI agents. It lets you define agents (with roles, goals, and tools), chain them into tasks, and run them as a Crew. Agents collaborate by passing context between tasks and can use tools like web search, making CrewAI well-suited for multi-step research, analysis, and automation pipelines.

Unlike the **OpenAI SDK** (a low-level API client you orchestrate manually), CrewAI provides built-in agent, task, and crew abstractions. Compared to **LangGraph** (graph-based state machines for complex control flow) and **AutoGen** (conversation-centric multi-agent chat), CrewAI is simpler and more task-oriented: you define roles and outputs, and the framework runs the pipeline. It’s a good fit when you want structured multi-step workflows without building orchestration from scratch.

---

## Purpose

This project demonstrates how to build an AI-powered research pipeline with CrewAI. It automates the workflow of:

1. **Research** — Gathering information on a company (status, performance, challenges, news, outlook)
2. **Analysis** — Creating a professional report with executive summary, key insights, and market outlook

Use it to quickly produce research reports on any public company for due diligence, market analysis, or learning.

### Quick reference

| Task        | Directory                  | Command                          |
|-------------|----------------------------|----------------------------------|
| Install deps| `src/financial_researcher/` | `uv sync`                        |
| Run project | `src/financial_researcher/` | `uv sync` then `crewai run`      |
| Run tests   | `src/financial_researcher/` | `uv sync --extra dev` then `uv run pytest tests/` |

---

## Features

- **Multi-agent orchestration** — Sequential pipeline with specialized agents
- **Web search integration** — Serper API for real-time company data and news
- **Structured output** — Markdown reports saved to `output/report.md`
- **Config-driven design** — Agents and tasks defined in YAML for easy customization
- **Multiple LLM support** — Researcher uses OpenAI; Analyst uses Groq (configurable)

---

## Architecture

The application uses a **Crew** of two agents:

| Agent      | Role                      | Tools          | LLM                      |
|-----------|---------------------------|----------------|--------------------------|
| Researcher | Senior Financial Researcher | SerperDevTool  | openai/gpt-4o-mini       |
| Analyst   | Market Analyst & Report writer | —              | groq/llama-3.3-70b-versatile |

Tasks execute sequentially: the Analyst receives the Researcher’s output as context before writing the report.

For detailed architecture, flow diagrams, and concepts, see [docs/](docs/).

---

## Prerequisites

- **Python** 3.10–3.12
- **CrewAI** (install via project)
- **API keys** (see [Configuration](#configuration))

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-crew-financial-researcher
```

### 2. Install dependencies with uv sync

The CrewAI project lives in `src/financial_researcher/`. **All commands below must be run from that directory.**

```bash
cd src/financial_researcher
uv sync
```

**What `uv sync` does:** Creates a virtual environment (if needed), installs dependencies from `pyproject.toml`, and generates/updates the lock file. Run it whenever you clone the repo or change dependencies.

---

## Configuration

Create a `.env` file in `src/financial_researcher/` with your API keys:

```env
# Required for the Researcher agent (OpenAI)
OPENAI_API_KEY=sk-...

# Required for the Analyst agent (Groq)
GROQ_API_KEY=gsk_...

# Required for web search (Serper)
SERPER_API_KEY=...
```

| Variable         | Used by   | Purpose                          |
|------------------|-----------|----------------------------------|
| `OPENAI_API_KEY` | Researcher | LLM for research                 |
| `GROQ_API_KEY`   | Analyst   | LLM for report writing           |
| `SERPER_API_KEY` | Researcher | Web search via SerperDevTool     |

Get keys from: [OpenAI](https://platform.openai.com/api-keys) | [Groq](https://console.groq.com/) | [Serper](https://serper.dev/)

---

## Usage

### How to run the project

**Working directory:** Always run from `src/financial_researcher/`.

```bash
cd src/financial_researcher
uv sync                    # if not already done
crewai run
```

### Customize the target company

Edit `src/financial_researcher/src/financial_researcher/main.py`:

```python
inputs = {
    'company': 'Apple'  # Change to any company name
}
```

---

## Running tests

**Working directory:** Same as the project — run from `src/financial_researcher/`.

### Step 1: Install dev dependencies

Tests require `pytest` and `pytest-mock`. Install them with:

```bash
cd src/financial_researcher
uv sync --extra dev
```

**What `uv sync --extra dev` does:** Installs the base dependencies plus the `[dev]` optional group (pytest, pytest-mock). Run this once before running tests.

### Step 2: Run the tests

```bash
cd src/financial_researcher
uv run pytest tests/
```

---

## Output

- **Console** — The full report is printed to stdout
- **File** — Saved to `src/financial_researcher/output/report.md`

---

## Project Structure

```
ai-crew-financial-researcher/
├── README.md
├── docs/
│   ├── architecture.md    # Architecture, flow diagrams
│   ├── concepts.md        # CrewAI concepts (Crew, Agent, Task)
│   └── execution.md       # Execution logs
└── src/financial_researcher/
    ├── src/financial_researcher/
    │   ├── crew.py        # Crew, agents, tasks definition
    │   ├── main.py        # Entry point
    │   ├── config/
    │   │   ├── agents.yaml
    │   │   └── tasks.yaml
    │   └── tools/
    │       └── custom_tool.py
    ├── output/
    │   └── report.md      # Generated report
    ├── knowledge/         # Optional knowledge sources
    └── pyproject.toml
```

---

## Documentation

| Document        | Description                                      |
|-----------------|--------------------------------------------------|
| [AGENTS.md](AGENTS.md) | Contributor map: layout, components, run commands |
| [docs/architecture.md](docs/architecture.md) | Architecture, flow diagram, components           |
| [docs/concepts.md](docs/concepts.md)         | CrewAI basics: Crew, Flow, Agent, Task           |
| [docs/execution.md](docs/execution.md)       | Example execution and results                    |

---

## Create a New CrewAI Project

To scaffold a new CrewAI project from scratch:

```bash
crewai create crew my_project_name
```

---
