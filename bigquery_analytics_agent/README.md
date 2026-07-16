# Build a BigQuery Analytics ADK Agent Plugin

## About This Project
This project guides you through building an intelligent agent using the Agent Development Kit (ADK) that can analyze data directly in **BigQuery**. The agent uses a BigQuery-backed plugin/toolset to explore datasets, run queries, and answer analytical questions in natural language, without you having to hand-write SQL.

## Architecture

![BigQuery Analytics Agent Plugin architecture](https://codelabs.developers.google.com/static/adk-bigquery-agent-analytics-plugin/img/c8d3754ee87af43f_856.png)

## What You'll Do
* **Develop the Agent:** Build an intelligent agent using the Agent Development Kit (ADK).
* **Integrate BigQuery:** Equip the agent with a BigQuery analytics plugin/toolset.
* **Analyze Data:** Interact with the agent to explore datasets and answer analytical questions over BigQuery data.

## Prerequisites
* A modern web browser such as Chrome.
* A Google Cloud project with billing enabled, or a standard Gmail account.
* Familiarity with using a command-line interface (CLI) in Google Cloud Shell.
* Basic understanding of Python to read and understand the ADK development code.
* `gcloud` CLI installed and authenticated (`gcloud auth login`), with a default project set (`gcloud config set project <PROJECT_ID>`).
* Python 3.10+.

## Setup

Run these steps from the repo root (`adk-workspace/`).

### 1. Create the Python environment

```bash
source setup.sh
```

This creates/activates a `.venv` at the repo root and installs the shared dependency, `google-adk`.

### 2. Move into the agent folder

```bash
cd bigquery_analytics_agent
```

### 3. Configure credentials

Create a `.env` file in this folder (see [`agent.py`](agent.py) for the model/config it expects), e.g.:

```bash
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=<your-api-key>
```

This file is gitignored and never committed.

## Running the Agent

From the `bigquery_analytics_agent/` folder, with the virtual environment active:

```bash
adk web
```

This launches the ADK dev UI (with tracing and session inspection) at a local URL you can open in your browser. Select `root_agent` in the UI and start chatting.

You can also run it headlessly:

```bash
adk run .
```

## Status

This agent is currently a skeleton (`agent.py` with a bare `root_agent`). BigQuery tooling, setup/cleanup scripts, and seed data are not wired up yet — see [`location_intelligence_agent`](../location_intelligence_agent/) for the target shape this agent will grow into.
