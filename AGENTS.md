## AGENTS — Project overview (ai-crew-financial-researcher)

This document is a **contributor-oriented map** of this repo: where things live, what each module does, and the common dev/run commands.

---

### Repository layout

```
ai-crew-financial-researcher/
├── README.md
├── AGENTS.md                 # This file
├── .gitignore
├── pyproject.toml            # Root deps (if any; may use workspace)
├── uv.lock
├── docs/
│   ├── architecture.md       # Architecture, flow diagrams, components
│   ├── concepts.md           # CrewAI concepts (Crew, Agent, Task)
│   └── execution.md          # Example execution logs
└── src/financial_researcher/ # CrewAI project root
    ├── pyproject.toml        # CrewAI project config + dependencies
    ├── uv.lock
    ├── main.py               # Entrypoint: run crew
    ├── crew.py               # Crew definition (agents, tasks, process)
    ├── config/
    │   ├── agents.yaml       # Agent roles, goals, backstories, LLMs
    │   └── tasks.yaml        # Task descriptions, expected outputs, context
    ├── tools/
    │   └── custom_tool.py    # Template for custom tools (not used by default)
    ├── knowledge/            # Optional knowledge sources
    │   └── user_preference.txt
    └── output/
        └── report.md         # Generated report (created on run)
```

Notes:

- The **CrewAI project** lives under `src/financial_researcher/`. Run `crewai run` from that directory.
- The package is installable via `pip install -e .` or `uv sync` inside `src/financial_researcher/`.
- Reports are written to `src/financial_researcher/output/report.md`.

---

### Key components (where to start reading)

- **Entrypoint (run crew)**: `src/financial_researcher/main.py`
  - Sets `inputs = {'company': 'Tesla'}` (customize here)
  - Instantiates `ResearchCrew().crew()` and calls `kickoff(inputs=inputs)`
  - Prints `result.raw` and reports that output was saved to `output/report.md`

- **Crew definition**: `src/financial_researcher/crew.py`
  - `ResearchCrew` (with `@CrewBase`): defines agents and tasks via decorators
  - **Agents**: `researcher` (SerperDevTool) and `analyst` (no tools)
  - **Tasks**: `research_task` (research company) → `analysis_task` (write report; uses `context: [research_task]`)
  - **Process**: `Process.sequential`

- **Agent config**: `src/financial_researcher/config/agents.yaml`
  - `researcher`: role, goal, backstory, LLM `openai/gpt-4o-mini`
  - `analyst`: role, goal, backstory, LLM `groq/llama-3.3-70b-versatile`
  - Placeholders like `{company}` are filled from `kickoff(inputs=...)`

- **Task config**: `src/financial_researcher/config/tasks.yaml`
  - `research_task`: description, expected output, assigned to `researcher`
  - `analysis_task`: description, expected output, assigned to `analyst`, `context: [research_task]`, `output_file: output/report.md`

- **Custom tools**: `src/financial_researcher/tools/custom_tool.py`
  - `MyCustomTool` template; extend for new agent capabilities
  - Not used by default; attach in `crew.py` if needed

---

### Configuration & environment variables

Create a `.env` in `src/financial_researcher/` (or export vars). Required keys:

| Variable         | Used by   | Purpose                          |
|------------------|-----------|----------------------------------|
| `OPENAI_API_KEY` | Researcher | LLM (gpt-4o-mini)               |
| `GROQ_API_KEY`   | Analyst   | LLM (llama-3.3-70b-versatile)   |
| `SERPER_API_KEY` | Researcher | Web search via SerperDevTool    |

Example:

```bash
export OPENAI_API_KEY="sk-..."
export GROQ_API_KEY="gsk_..."
export SERPER_API_KEY="..."
```

---

### Running locally

#### Install dependencies

From `src/financial_researcher/`:

```bash
uv sync
# or: pip install -e .
```

#### Run the crew (recommended)

From `src/financial_researcher/`:

```bash
crewai run
```

#### Run via Python

```bash
cd src/financial_researcher
python -m financial_researcher.main
```

Or, after install:

```bash
financial_researcher
```

#### Change target company

Edit `inputs` in `src/financial_researcher/main.py`:

```python
inputs = {'company': 'Apple'}  # or any company name
```

---

### Common pitfalls

- **`crewai run` fails / wrong directory**: Run from `src/financial_researcher/`, not the repo root. CrewAI expects the project root (where `pyproject.toml` has `[tool.crewai]`) as the working directory.

- **`ModuleNotFoundError` / missing package**: Install inside `src/financial_researcher/` with `uv sync` or `pip install -e .`. Use `uv run ...` or the project’s venv when running Python scripts.

- **Missing API keys**: Ensure `OPENAI_API_KEY`, `GROQ_API_KEY`, and `SERPER_API_KEY` are set in `.env` or the environment. SerperDevTool will fail without `SERPER_API_KEY`.

- **Output file not found**: Reports are written to `output/report.md` relative to the CrewAI project root (`src/financial_researcher/`). The path is `src/financial_researcher/output/report.md` from the repo root.
