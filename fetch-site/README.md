# fetch-site

Fetches the text content of any public website URL and returns it as plain text.

## What it does

Reads the DOM of a remote URL, strips away scripts, styles, navigation, and other non-content elements, then returns the primary readable text. Useful for summarizing articles, extracting webpage data, or grounding answers in live web content.

## Usage

Call the `run_js` tool with `scripts/index.html` and pass a JSON string as data:

```json
{ "url": "https://example.com" }
```

### Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `url` | Yes | The full HTTP or HTTPS URL of the site to fetch |

### Response

On success:

```json
{ "url": "https://example.com", "content": "Page text content …" }
```

On failure:

```json
{ "error": "Error description" }
```

> **Note:** Local, loopback, link-local, and private network URLs are blocked. Content is capped at 8,000 characters.

## Files

| File | Description |
|------|-------------|
| `SKILL.md` | Skill metadata consumed by the agent runtime |
| `scripts/index.html` | Runnable skill script |
