# search-ddg

Search the web using DuckDuckGo and return up-to-date results.

## What it does

Queries DuckDuckGo for a given search term and returns the top result snippets. Useful for retrieving current events, facts outside the model's training data, or any information that benefits from a live web search.

## Usage

Call the `run_js` tool with `scripts/index.html` and pass a JSON string as data:

```json
{ "query": "latest news on renewable energy" }
```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `query` | Yes | The exact search terms to look up. Keep it concise. |

### Response

On success:

```json
{ "query": "latest news on renewable energy", "results": ["Snippet 1 …", "Snippet 2 …"] }
```

On failure:

```json
{ "error": "Error description" }
```

> **Tip:** Only trigger this skill when asked for recent events or facts outside your training data.

## Files

| File | Description |
|------|-------------|
| `SKILL.md` | Skill metadata consumed by the agent runtime |
| `scripts/index.html` | Runnable skill script |
