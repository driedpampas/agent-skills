# agent-skills

A collection of skills for AI Edge Gallery agents. Each skill lives in its own directory and exposes an `index.html` entry point that implements the `ai_edge_gallery_get_result` interface.

## Skills

| Skill | Description |
|-------|-------------|
| [fetch-site](./fetch-site/) | Fetch the text content of any public website URL |
| [search-ddg](./search-ddg/) | Search the web using DuckDuckGo |

## Usage

Each skill directory contains:
- `SKILL.md` – skill metadata and usage instructions consumed by the agent runtime
- `scripts/index.html` – the runnable skill script invoked via the `run_js` tool

To use a skill, call the `run_js` tool with the skill's `index.html` and pass a JSON string as data. See each skill's README for the exact parameters.