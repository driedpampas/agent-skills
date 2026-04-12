---
name: fetch-site
description: Fetch the text content of any public website URL.
---
# fetch-site
Reads the DOM of a remote URL and returns the primary text content. Useful for summarizing specific articles or extracting webpage data.

## Instructions
Call the `run_js` tool using `index.html` and a JSON string for data with the following fields:
- `url`: Required. The full HTTP or HTTPS URL of the site to read.
