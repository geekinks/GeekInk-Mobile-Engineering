#!/usr/bin/env python3
"""Validate GeekInk curriculum completeness without third-party packages."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TRACKS = ("dart-flutter", "react-native", "kotlin-android")
REQUIRED = ("Learning objectives", "Prerequisites", "Concept", "Practical code example", "Step-by-step implementation", "Hands-on exercise", "Mini challenge", "Expected output", "Assessment criteria", "Offline considerations", "Low-resource considerations", "Additional learning resources", "Submission instructions")

def main():
    errors = []
    for track in TRACKS:
        base = ROOT / "curriculum" / track
        modules = sorted(base.glob("module-*/README.md"))
        if len(modules) != 10:
            errors.append(f"{track}: expected 10 module READMEs, found {len(modules)}")
        lessons = sorted(base.glob("module-*/day-*/README.md"))
        if len(lessons) != 100:
            errors.append(f"{track}: expected 100 lessons, found {len(lessons)}")
        for module in range(1, 11):
            found = list((base / f"module-{module:02d}").glob("day-*/README.md"))
            if len(found) != 10:
                errors.append(f"{track}/module-{module:02d}: expected 10 lessons, found {len(found)}")
        for lesson in lessons:
            text = lesson.read_text(encoding="utf-8")
            missing = [section for section in REQUIRED if f"## {section}" not in text]
            if missing:
                errors.append(f"{lesson.relative_to(ROOT)}: missing {', '.join(missing)}")
            if "Offline considerations" not in text or "Low-resource considerations" not in text:
                errors.append(f"{lesson.relative_to(ROOT)}: missing resilience coverage")
    for path in (ROOT / "docs" / "instructor-guide.md", ROOT / "docs" / "offline-first-principles.md", ROOT / "docs" / "low-resource-development.md", ROOT / "docs" / "power-aware-engineering.md", ROOT / "task" / "submission-template.md"):
        if not path.is_file(): errors.append(f"Missing required documentation: {path.relative_to(ROOT)}")
    projects = list((ROOT / "projects").glob("*/*/README.md"))
    if len(projects) < 9: errors.append(f"Expected at least 9 project briefs, found {len(projects)}")
    for project in projects:
        text = project.read_text(encoding="utf-8")
        missing = [s for s in ("Offline requirements", "Connectivity assumptions", "Data storage strategy", "Conflict resolution", "Testing requirements", "Evaluation rubric") if s.lower() not in text.lower()]
        if missing: errors.append(f"{project.relative_to(ROOT)}: missing {', '.join(missing)}")
    if errors:
        print("Curriculum validation failed:\n- " + "\n- ".join(errors))
        return 1
    print("Curriculum validation passed: 3 tracks × 10 modules × 10 lessons; documentation and projects present.")
    return 0

if __name__ == "__main__": sys.exit(main())
