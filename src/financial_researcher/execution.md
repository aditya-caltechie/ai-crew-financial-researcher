Adityas-Laptop:debate averma$ pwd
/Users/averma/github/Udemy/02_AI-ML_Courses/02_AgenticAI/Agents-AI/3_crew/debate
Adityas-Laptop:debate averma$ cd ../financial_researcher/
Adityas-Laptop:financial_researcher averma$ ls
README.md       knowledge       output          pyproject.toml  src             uv.lock
Adityas-Laptop:financial_researcher averma$ 
Adityas-Laptop:financial_researcher averma$ crewai run 
Running the Crew
Using CPython 3.11.14 interpreter at: /opt/homebrew/opt/python@3.11/bin/python3.11
Creating virtual environment at: .venv
      Built financial-researcher @ file:///Users/averma/github/Udemy/02_AI-ML_Courses/02_AgenticAI/Agents-AI/3_crew/financial_rese
Installed 217 packages in 1.42s
/Users/averma/github/Udemy/02_AI-ML_Courses/02_AgenticAI/Agents-AI/3_crew/financial_researcher/.venv/lib/python3.11/site-packages/pydantic/_internal/_config.py:295: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  warnings.warn(DEPRECATION_MESSAGE, DeprecationWarning)
/Users/averma/github/Udemy/02_AI-ML_Courses/02_AgenticAI/Agents-AI/3_crew/financial_researcher/.venv/lib/python3.11/site-packages/pydantic/_internal/_fields.py:192: UserWarning: Field name "schema" in "DatabricksQueryToolSchema" shadows an attribute in parent "BaseModel"
  warnings.warn(
/Users/averma/github/Udemy/02_AI-ML_Courses/02_AgenticAI/Agents-AI/3_crew/financial_researcher/.venv/lib/python3.11/site-packages/pydantic/_internal/_generate_schema.py:502: UserWarning: <built-in function callable> is not a Python type (it may be an instance of an object), Pydantic will allow any object with no validation since we cannot even enforce that the input is an instance of the given type. To get rid of this error wrap the type with `pydantic.SkipValidation`.
  warn(
/Users/averma/github/Udemy/02_AI-ML_Courses/02_AgenticAI/Agents-AI/3_crew/financial_researcher/.venv/lib/python3.11/site-packages/crewai_tools/tools/scrapegraph_scrape_tool/scrapegraph_scrape_tool.py:34: PydanticDeprecatedSince20: Pydantic V1 style `@validator` validators are deprecated. You should migrate to Pydantic V2 style `@field_validator` validators, see the migration guide for more details. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  @validator("website_url")
/Users/averma/github/Udemy/02_AI-ML_Courses/02_AgenticAI/Agents-AI/3_crew/financial_researcher/.venv/lib/python3.11/site-packages/crewai_tools/tools/selenium_scraping_tool/selenium_scraping_tool.py:26: PydanticDeprecatedSince20: Pydantic V1 style `@validator` validators are deprecated. You should migrate to Pydantic V2 style `@field_validator` validators, see the migration guide for more details. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  @validator("website_url")
/Users/averma/github/Udemy/02_AI-ML_Courses/02_AgenticAI/Agents-AI/3_crew/financial_researcher/.venv/lib/python3.11/site-packages/crewai_tools/tools/vision_tool/vision_tool.py:15: PydanticDeprecatedSince20: Pydantic V1 style `@validator` validators are deprecated. You should migrate to Pydantic V2 style `@field_validator` validators, see the migration guide for more details. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.10/migration/
  @validator("image_path_url")
╭──────────────────────────────────────────────────── Crew Execution Started ────────────────────────────────────────────────────╮
│                                                                                                                                │
│  Crew Execution Started                                                                                                        │
│  Name: crew                                                                                                                    │
│  ID: d51c0e25-71d4-4d72-ab44-66b698a73c57                                                                                      │
│                                                                                                                                │
│                                                                                                                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: ffa00438-9748-4f4d-a7d4-a17100fb4b95
       Status: Executing Task...

🚀 Crew: crew
└── 📋 Task: ffa00438-9748-4f4d-a7d4-a17100fb4b95
       Status: Executing Task...
    └── 🤖 Agent: Senior Financial Researcher for Tesla
            Status: In Progress

# Agent: Senior Financial Researcher for Tesla
## Task: Conduct thorough research on company Tesla. Focus on: 1. Current company status and health 2. Historical company performance 3. Major challenges and opportunities 4. Recent news and events 5. Future outlook and potential developments
Make sure to organize your findings in a structured format with clear sections.

_(Full execution log continues with Serper searches, research document, Market Analyst task, and final report - see output/report.md for the complete Tesla report)_

Report has been saved to output/report.md
Adityas-Laptop:financial_researcher averma$
