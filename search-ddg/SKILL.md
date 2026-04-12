---
name: search-ddg
description: Search the web using DuckDuckGo to retrieve up-to-date information or facts.
---
# search-ddg
This skill allows the model to autonomously trigger a web search when it needs current data.

## Instructions
Call the `run_js` tool using `index.html` and a JSON string for data with the following fields:
- `query`: Required. The exact search terms to look up. Keep it concise.

Constraints:
- Only trigger when asked for recent events or facts outside your training data.
