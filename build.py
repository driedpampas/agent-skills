#!/usr/bin/env python3
"""Build script for agent-skills GitHub Pages site.

- Copies every file as-is so raw files (e.g. SKILL.md) remain accessible.
- For each README.md, also generates a styled index.html in the same directory.
- Adds .nojekyll to the output so GitHub Pages does not re-run Jekyll.
"""

import os
import shutil
import markdown

OUTPUT_DIR = "_site"

# Directories to skip entirely
SKIP_DIRS = {".git", ".github", "_site", "node_modules", "__pycache__"}

# Files to skip (not copied to output)
SKIP_FILES = {"build.py", ".gitignore", ".nojekyll"}

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; }}
    body {{
      max-width: 860px;
      margin: 48px auto;
      padding: 0 24px 64px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                   Helvetica, Arial, sans-serif;
      line-height: 1.65;
      color: #24292f;
      background: #fff;
    }}
    a {{ color: #0969da; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    h1, h2, h3, h4 {{ line-height: 1.25; margin-top: 1.5em; margin-bottom: .5em; }}
    h1 {{ font-size: 2em; border-bottom: 1px solid #d0d7de; padding-bottom: .3em; }}
    h2 {{ font-size: 1.5em; border-bottom: 1px solid #d0d7de; padding-bottom: .3em; }}
    code {{
      background: #f6f8fa;
      border: 1px solid #d0d7de;
      border-radius: 6px;
      padding: 2px 6px;
      font-size: .9em;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
    }}
    pre {{
      background: #f6f8fa;
      border: 1px solid #d0d7de;
      border-radius: 6px;
      padding: 16px;
      overflow-x: auto;
      line-height: 1.45;
    }}
    pre code {{
      background: none;
      border: none;
      padding: 0;
      font-size: .875em;
    }}
    blockquote {{
      border-left: 4px solid #d0d7de;
      color: #57606a;
      margin: 0;
      padding: 0 16px;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 1em 0;
    }}
    th, td {{
      border: 1px solid #d0d7de;
      padding: 8px 13px;
      text-align: left;
    }}
    th {{ background: #f6f8fa; font-weight: 600; }}
    tr:nth-child(even) {{ background: #f6f8fa; }}
    img {{ max-width: 100%; }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def extract_title(text: str) -> str:
    """Return the text of the first ATX heading, or 'README' as fallback."""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return "README"


def build() -> None:
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    os.makedirs(OUTPUT_DIR)

    md = markdown.Markdown(extensions=["fenced_code", "tables", "toc"])

    for root, dirs, files in os.walk("."):
        # Prune directories we never want to descend into
        dirs[:] = sorted(
            d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")
        )

        rel_root = os.path.relpath(root, ".")
        dest_dir = OUTPUT_DIR if rel_root == "." else os.path.join(OUTPUT_DIR, rel_root)
        os.makedirs(dest_dir, exist_ok=True)

        for fname in files:
            if fname in SKIP_FILES:
                continue

            src = os.path.join(root, fname)

            if fname == "README.md":
                with open(src, encoding="utf-8") as fh:
                    text = fh.read()

                title = extract_title(text)
                html_body = md.convert(text)
                md.reset()

                # Write rendered HTML as the directory index
                index_path = os.path.join(dest_dir, "index.html")
                with open(index_path, "w", encoding="utf-8") as fh:
                    fh.write(HTML_TEMPLATE.format(title=title, body=html_body))

                # Also copy the raw README.md so it remains accessible
                shutil.copy2(src, os.path.join(dest_dir, fname))

            else:
                shutil.copy2(src, os.path.join(dest_dir, fname))

    # Prevent GitHub Pages from running Jekyll on the output
    with open(os.path.join(OUTPUT_DIR, ".nojekyll"), "w"):
        pass
    print(f"Site built in '{OUTPUT_DIR}/'")


if __name__ == "__main__":
    build()
