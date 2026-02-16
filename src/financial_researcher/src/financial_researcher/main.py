#!/usr/bin/env python
# src/financial_researcher/main.py
"""
Entry Point - Step 4 of Implementation Guide

This is the entry point that initializes the crew and triggers execution.
Run with: crewai run
Or: python -m financial_researcher.main

Implementation Order:
1. Define agents in config/agents.yaml
2. Define tasks in config/tasks.yaml
3. Implement crew logic in crew.py
4. Create entry point here (this file)
"""
import os
from financial_researcher.crew import ResearchCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    
    This function:
    1. Defines inputs (fills placeholders like {company} in YAML configs)
    2. Creates the crew and kicks off execution
    3. Handles results and output files
    """
    # Step 4a: Define inputs
    # These values replace placeholders (e.g., {company}) in agents.yaml and tasks.yaml
    inputs = {
        'company': 'Tesla'  # Change this to research different companies
    }

    # Step 4b: Create and run the crew
    # ResearchCrew().crew() creates the crew instance
    # kickoff(inputs=inputs) starts execution and fills placeholders
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Step 4c: Handle results
    # result.raw contains the final output (last task's output)
    # Tasks with output_file also write to disk automatically
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()