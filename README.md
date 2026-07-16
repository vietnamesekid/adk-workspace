# ADK Workspace

A working lab for reproducing common **agent patterns and multi-agent workflows** with [Google's Agent Development Kit](https://google.github.io/adk-docs/) (`google-adk`), and taking them from a local prototype to something that actually runs production-ready on Google Cloud.

Each subdirectory is a self-contained ADK agent app. This root just holds the shared Python environment and the conventions every agent in here follows.

## Why ADK

ADK is Google's code-first, model-agnostic framework for building agents: an `Agent` combines a model, an instruction, and a set of tools, and a `Runner` drives the reasoning/acting loop around it. What makes it useful beyond a single agent is its **workflow primitives** — deterministic orchestrators you compose agents with instead of hand-rolling control flow:

| Pattern               | ADK primitive     | Use it when                                                                                                        |
| --------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Pipeline              | `SequentialAgent` | Step B needs step A's output (shared session state via `output_key`)                                               |
| Fan-out / fan-in      | `ParallelAgent`   | Independent sub-tasks can run concurrently, then get merged                                                        |
| Iterative refinement  | `LoopAgent`       | A critique-and-revise loop until a condition or max-iterations is hit                                              |
| Dynamic delegation    | `sub_agents`      | The LLM itself should route to the right specialist agent at runtime                                               |
| Agent-as-tool         | `AgentTool`       | A parent agent stays in control and calls another agent like a function                                            |
| External tool servers | MCP Toolsets      | Tools live behind a Model Context Protocol server (BigQuery, Maps, internal APIs, etc.) instead of in-process code |

This workspace is where these get exercised one at a time, against real Google Cloud services, before they're considered "done."

## What "production-ready" means here

Not just "it runs on my machine." Each agent in this workspace is expected to:

- Load configuration (`GOOGLE_CLOUD_PROJECT`, API keys, model name) from environment, never hardcoded
- Provision its own cloud dependencies through idempotent setup scripts (BigQuery datasets, API keys, enabled services) rather than manual console clicks
- Be cleanly disposable — a matching cleanup script tears down everything setup created
- Be deployable with ADK's built-in deploy targets once it's validated locally:
  - `adk deploy cloud` → Vertex AI Agent Engine (fully managed, autoscaling)
  - `adk deploy cloud_run` → Cloud Run
  - `adk deploy gke` → GKE

Locally, every agent is run and iterated on with:

```bash
adk web    # dev UI with tracing and session inspection
adk run    # headless CLI run
```

## Repo layout

```text
adk-workspace/
├── requirements.txt      # shared deps (google-adk) for the whole workspace
├── setup.sh              # source this to create/activate .venv and install deps
└── <agent_name>/         # one folder per agent, each independently runnable
    ├── agent.py           # root_agent definition
    ├── tools.py           # tool/toolset factories (incl. MCP toolsets)
    ├── setup_env.sh       # provisions APIs/keys, writes .env
    ├── setup_bigquery.sh  # provisions this agent's cloud data, if any
    ├── cleanup.sh         # tears down everything the setup scripts created
    ├── seed/              # sample data for local/demo runs
    └── Makefile           # `make run`, `make setup-env`, ...
```

## Getting started

```bash
source setup.sh                     # creates .venv, activates it, installs google-adk
cd <agent_name>
./setup_env.sh && ./setup_bigquery.sh   # if the agent needs cloud resources
make run                            # or: adk web
```

## Agents in this workspace

| Agent                                                         | Description                                                                                                                                                    |
| ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`location_intelligence_agent`](location_intelligence_agent/) | Combines a BigQuery MCP toolset (demographics, pricing, sales) with a Google Maps MCP toolset to answer market-siting questions for a fictitious bakery chain. |

New agents should follow the same shape: a `Makefile`, setup/cleanup scripts, and an `agent.py` that reads its config from the environment.
