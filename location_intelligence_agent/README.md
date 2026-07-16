# Build a Location Intelligence ADK Agent with MCP servers for BigQuery and Google Maps

## About This Project
This project guides you through building an intelligent agent using the Agent Development Kit (ADK), powered by Gemini 3.1 Pro. The agent is equipped with tools from remote Model Context Protocol (MCP) servers to securely access **BigQuery** (for demographic, pricing, and sales data) and **Google Maps** (for real-world location analysis and validation). 

The resulting agent can orchestrate requests between the user and Google Cloud services to solve business problems related to a fictitious bakery dataset.

## Architecture

![Location Intelligence Agent architecture](https://codelabs.developers.google.com/static/adk-mcp-bigquery-maps/img/82dd7bd2823a821b_856.png)

## What You'll Do
* **Set up the Data:** Create the foundational bakery dataset in BigQuery.
* **Develop the Agent:** Build an intelligent agent using the Agent Development Kit (ADK).
* **Integrate Tools:** Equip the agent with BigQuery and Maps functionalities via the MCP server.
* **Analyze the Market:** Interact with the agent to assess market trends and saturation.

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
cd location_intelligence_agent
```

### 3. Provision Google Cloud resources and credentials

```bash
./setup_env.sh
```

This script:
* Detects your active `gcloud` project.
* Enables the required APIs: `aiplatform`, `apikeys`, `mapstools`, and `bigquery` (including their MCP endpoints).
* Creates a Google Maps Platform API key.
* Writes a `.env` file in this folder with `GOOGLE_GENAI_USE_VERTEXAI`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`, and `MAPS_API_KEY`.

### 4. Seed the BigQuery dataset

```bash
./setup_bigquery.sh [gs://optional-bucket-name]
```

This creates (or reuses) a Cloud Storage bucket, uploads the CSVs in [`seed/`](seed/), and creates the `mcp_bakery` BigQuery dataset with four tables: `demographics`, `bakery_prices`, `sales_history_weekly`, and `foot_traffic`.

## Running the Agent

From the `location_intelligence_agent/` folder, with the virtual environment active:

```bash
make run
```

This is equivalent to running `adk web`, which launches the ADK dev UI (with tracing and session inspection) at a local URL you can open in your browser. Select `root_agent` in the UI and start chatting — e.g. ask it to compare bakery pricing across neighborhoods or find nearby competitors on the map.

You can also run it headlessly:

```bash
adk run .
```

### Makefile shortcuts

| Command | Description |
|---|---|
| `make setup-env` | Runs `setup_env.sh` (APIs, Maps API key, `.env`) |
| `make setup-bigquery` | Runs `setup_bigquery.sh` (bucket + `mcp_bakery` dataset) |
| `make run` | Runs `adk web` |
| `make cleanup` | Runs `cleanup.sh` |

## Cleanup

To tear down everything the setup scripts created (BigQuery dataset, storage bucket, Maps API keys, and local `.env`):

```bash
./cleanup.sh
```

You'll be prompted to confirm before anything is deleted, and asked separately whether to disable the APIs that were enabled during setup.
---