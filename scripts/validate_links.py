#!/usr/bin/env python3
"""Check relative Markdown links within the repository."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
pattern = re.compile(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)")
bad = []
for source in ROOT.rglob("*.md"):
    for target in pattern.findall(source.read_text(encoding="utf-8")):
        if "://" in target or target.startswith("mailto:"): continue
        if not (source.parent / target).resolve().exists(): bad.append(f"{source.relative_to(ROOT)} -> {target}")
if bad:
    print("Broken internal links:\n- " + "\n- ".join(bad)); sys.exit(1)
print("Internal Markdown links passed.")
