#!/usr/bin/env python3
"""Small dependency-free Markdown hygiene check for offline-friendly CI."""
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
errors = []
for path in root.rglob("*.md"):
    lines = path.read_text(encoding="utf-8").splitlines()
    content = lines
    if lines and lines[0] == "---":
        try:
            content = lines[lines.index("---", 1) + 1:]
        except ValueError:
            errors.append(f"{path.relative_to(root)}: unclosed front matter")
            content = []
    if not content or not any(line.startswith("# ") for line in content):
        errors.append(f"{path.relative_to(root)}: needs one top-level title")
    for no, line in enumerate(lines, 1):
        if line.endswith(" ") and not line.endswith("  "):
            errors.append(f"{path.relative_to(root)}:{no}: trailing space")
if errors:
    print("Markdown hygiene failed:\n- " + "\n- ".join(errors)); sys.exit(1)
print("Markdown hygiene passed.")
