#!/usr/bin/env python3
"""Write the maintained, offline-readable repository guides and project briefs."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

COMMON = '''# {title}

GeekInk — **Builders Who Leave a Mark.** This guide is designed for learners who may work with expensive data, interrupted electricity, and modest hardware. Keep a local copy with the repository.

## Purpose

{body}

## Practical checklist

- Work in small commits; after an unexpected shutdown, run the smallest useful test first.
- Keep source code, sample data, and instructions usable without a cloud account.
- Test the essential flow in airplane mode before calling it complete.
- Record assumptions and observed device behaviour in your submission.

## Further study

Use downloaded official documentation when connectivity is available. Version-sensitive commands belong in the cohort's cached setup pack, not in assumptions about a fresh offline machine.
'''

DOCS = {
"index.md": ("Documentation hub", "Start with the student guide and environment setup. Instructors should use the instructor guide, assessment rubric, and local-learning infrastructure guide before a cohort begins."),
"student-guide.md": ("Student guide", "Choose one track, complete lessons in order, and build each day on a local Git branch. A physical Android device is sufficient; emulators are optional. Submit source, screenshots or written evidence, and an honest offline test report."),
"instructor-guide.md": ("Instructor guide", "Facilitate short explanations, paired practical work, device testing, and reflection. Demonstrate failed networks and recovery deliberately. Assess outcomes rather than hardware ownership. Accept screenshots and written reports when video is impractical; never require personal student folders in this repository."),
"environment-setup.md": ("Environment setup", "Download SDKs, toolchains, package caches, and platform images during connectivity windows. Verify a minimal project once online, archive installers and caches on an external drive, then use physical-device USB debugging. A clean build needs dependencies that were previously downloaded; offline mode cannot invent them."),
"offline-first-principles.md": ("Offline-first principles", "Local data is the primary UI source of truth. A repository mediates local and remote sources. Changes are written locally, assigned idempotency keys, queued, retried with bounded exponential backoff, and made visible as pending, synced, or failed. Eventual consistency needs an explicit conflict rule and audit information."),
"low-resource-development.md": ("Low-resource development", "Profile A (4 GB RAM): physical device, lightweight editor, small projects, no required emulator. Profile B (8 GB): SSD and occasional connected downloads. Profile C (16 GB+): emulator and several devices. Close background apps, use incremental builds, conserve storage, and back up source to removable media."),
"power-aware-engineering.md": ("Power-aware engineering", "Use constrained, batched, deferrable background work rather than polling. Respect the operating system scheduler and Doze mode. Optimise media, database queries, and retry limits. For learning, commit often, maintain local backups, and recover after an outage by checking version control and a minimal build—never improvise unsafe power or charging practices."),
"local-learning-infrastructure.md": ("Local learning infrastructure", "Serve this folder on a LAN using `python3 -m http.server 8000` from the repository root, then browse from connected devices. Moodle/MoodleBox or a Raspberry Pi Wi-Fi hotspot can host the same static materials. Distribute a versioned ZIP plus cached installers and documentation through USB; verify checksums where possible."),
"assessment-rubric.md": ("Assessment rubric", "Assess functional correctness (30%), local-first behaviour and integrity (25%), tests including interruption evidence (20%), usability/accessibility (10%), code quality (10%), and reflection (5%). Evaluate the learner's decisions under constraints, not their internet speed or device price."),
"learning-resources.md": ("Learning resources", "Prioritise official Flutter, React Native/Expo, Android, Kotlin, SQLite, Git, and accessibility documentation. Cohorts should download a curated snapshot during reliable connectivity and place it in `resources/offline-documentation`; do not redistribute material unless its licence allows it."),
"mobile-development-roadmap.md": ("Mobile development roadmap", "Foundation → language → UI → local data → APIs and synchronization → security → advanced device work → testing → production → capstone. Each of the three tracks follows this 100-day sequence while using its ecosystem's native tools."),
"project-guidelines.md": ("Project guidelines", "Start with an offline user journey and a small data model. Define local storage, sync boundaries, idempotency, conflict policy, storage limits, privacy, tests, and a recovery path before UI polish. Clearly label features as fully offline, locally available, or eventually connected."),
"capstone-guidelines.md": ("Capstone guidelines", "Build a community-relevant Android application: education, health administration, agriculture, transport, or small business are good starting points. Demonstrate local-first core functionality, visible synchronization state, one conflict rule, constrained background work, and reproducible tests."),
"troubleshooting.md": ("Troubleshooting", "If builds fail offline, check that the SDK, Gradle/npm/pub cache, and project dependencies were downloaded earlier. Do not delete working caches to make room without a backup. For device issues, verify USB debugging, cable, storage space, and platform tools. Capture exact errors in the issue template."),
"implementation-progress.md": ("Implementation progress", "- [x] Inspect the Python reference structure\n- [x] Create repository architecture and shared philosophy\n- [x] Publish three 100-day roadmaps and 300 daily lessons\n- [x] Add projects, exercises, templates, and infrastructure guides\n- [x] Add submissions, validation, and GitHub automation\n- [x] Run repository validation\n\nFuture cohorts should improve individual lessons from classroom feedback rather than changing the progression without review."),
}

PROJECTS = {
"beginner": [("offline-personal-profile", "Offline Personal Profile App", "Let a learner create and view a profile without a network."), ("local-todo", "Local Todo Application", "Keep tasks usable and durable across restarts."), ("student-result-manager", "Student Result Management App", "Record and calculate student results locally with privacy safeguards."), ("offline-expense-tracker", "Offline Expense Tracker", "Capture small-business expenses and provide local summaries.")],
"intermediate": [("offline-notes-sync", "Offline Notes with Synchronization", "Create notes locally and sync safe mutations later."), ("student-attendance", "Student Attendance Application", "Capture attendance in classrooms with intermittent connectivity."), ("inventory-management", "Inventory Management Application", "Manage stock locally with carefully reconciled updates."), ("field-data-collection", "Field Data Collection Application", "Collect agricultural or community survey data offline.")],
"advanced": [("offline-learning-management", "Offline-First Learning Management System", "Deliver downloaded learning content, progress, and deferred sync."), ("community-health-records", "Community Health Records Application", "Support local, access-controlled health administration records."), ("agricultural-data-collection", "Agricultural Data Collection Application", "Capture farm observations, media references, and later uploads."), ("community-service-management", "Community Service Management Application", "Coordinate local requests and eventual updates without hiding failures.")],
}

def project(title, statement):
    return f'''# {title}

## Problem statement

{statement}

## Functional requirements

- Create, view, edit, and safely remove the core local records.
- Search or filter records and show meaningful empty, validation, and error states.
- Show each deferred operation as pending, synced, or needing attention.

## Non-functional requirements

The app must be usable on a low-end Android device, accessible, restart-safe, and understandable without continuous internet.

## Offline requirements

Core capture and viewing are fully offline. Synchronization is eventual and must never be required to save essential work.

## Connectivity assumptions

Connections can be absent, slow, duplicated, or interrupted. Remote-only enrichment is labelled clearly; it cannot silently block local work.

## Data storage strategy

Use a local SQLite-backed store as the UI source of truth. Store records, sync metadata, stable IDs, timestamps, and pending mutation payloads. Protect sensitive records using platform secure storage and least-privilege access.

## Synchronization architecture

`UI → repository → local database → durable mutation queue → constrained background worker → API`. Workers send idempotency keys and update local sync state atomically.

## Conflict resolution

Document a field-level merge where safe; otherwise retain both versions or require a user review. Never discard a local edit invisibly. Include timestamps and origin identifiers for auditability.

## Battery and storage considerations

Batch uploads, enforce network/battery constraints, resize media before storing, paginate lists, and offer safe cleanup only after successful backup or sync.

## Security requirements

Validate input, avoid secrets in the repository, encrypt in transit, use secure token storage, and limit sensitive local data to the minimum necessary.

## UI/UX requirements

Use Material Design 3 patterns, readable text, accessible labels, offline status, and clear recovery actions.

## Testing requirements

Test CRUD, restart persistence, airplane mode, duplicated retry, server conflict, low storage, and interrupted background work on a physical device where possible.

## Architecture diagram

```text
Screen → View model/state → Repository → Local database (source of truth)
                                   └→ Durable queue → constrained sync → API
```

## Implementation milestones

1. User journey, schema, and local CRUD.
2. Validation, tests, and offline UI states.
3. Durable queue, idempotency, and observable sync status.
4. Remote adapter, retry policy, and conflict handling.
5. Accessibility, performance, release documentation.

## Evaluation rubric

| Area | Weight |
| --- | ---: |
| Reliable local core | 30% |
| Synchronization and conflict policy | 25% |
| Tests and interruption evidence | 20% |
| Security, accessibility, resource awareness | 15% |
| Documentation and reflection | 10% |

## Extension challenges

Add multi-device conflict review, export/import, permission roles, or a deliberately remote-only feature with graceful degradation.
'''

def write(relative, text):
    path = ROOT / relative; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(text, encoding="utf-8")

def main():
    for name, (title, body) in DOCS.items(): write(Path("docs") / name, COMMON.format(title=title, body=body))
    for level, projects in PROJECTS.items():
        write(Path("projects") / level / "README.md", f"# {level.title()} offline-first projects\n\nChoose a brief and implement it in your selected track.\n")
        for slug, title, statement in projects: write(Path("projects") / level / slug / "README.md", project(title, statement))
    write("task/README.md", "# Student tasks\n\nSubmit through GitHub using the template. Fork or create your own repository; do not add personal directories here.\n")
    write("task/students/README.md", "# Student submissions\n\nThis directory intentionally contains no personal student work. Submit using your own repository, issue, or pull request as your cohort instructs.\n")
    write("task/submission-template.md", "# GeekInk submission\n\n- Student name:\n- GitHub username:\n- Technology track:\n- Module / day:\n- Task title:\n- Repository link:\n- Implementation description:\n- Screenshot(s) or optional demonstration video:\n- Offline testing performed:\n- Connectivity conditions tested:\n- Challenges encountered:\n- Lessons learned:\n")
    for name, text in {"offline-first-architecture":"Local source-of-truth, queues, conflicts, idempotency, and observability.","mobile-ui-ux":"Accessible, responsive, low-end-device-friendly mobile interfaces.","mobile-backend-integration":"REST boundaries, local/remote sources, and resilient synchronization.","mobile-security":"Sessions, secure storage, permissions, validation, and privacy.","mobile-testing":"Unit, UI, integration, interruption, memory, and battery testing.","mobile-devops":"Reproducible local builds, CI, versioning, and release process.","mobile-performance":"Battery, storage, network, and rendering performance.","mobile-architecture":"Repositories, state, clean boundaries, and pragmatic patterns."}.items(): write(Path("specializations") / name / "README.md", f"# {name.replace('-', ' ').title()}\n\n{text}\n\nUse this specialization after the core pathway to deepen practical capability.\n")
    write("resources/README.md", "# Resources\n\nCohorts can place legally distributable offline references, small datasets, cheat sheets, tools, and design resources in the named folders. Do not commit proprietary SDKs or secrets.\n")
    for d in ("cheat-sheets", "datasets", "recommended-reading", "offline-documentation", "tools", "design-resources"): write(Path("resources") / d / "README.md", f"# {d.replace('-', ' ').title()}\n\nStore curated, licence-compliant materials here for offline cohort use.\n")
    write("requirements.md", "# Requirements\n\nA physical Android device and USB cable are sufficient. Profile A: 4 GB RAM; Profile B: 8 GB and SSD; Profile C: 16 GB+ for emulator work. Internet is required only to initially download toolchains, SDKs, and packages; cache them for later use.\n")
    write("infrastructure/local-learning-server/README.md", "# Local learning server\n\nRun `python3 -m http.server 8000` at repository root, then share the host on a trusted local Wi-Fi network. Copy the repository to USB for offline distribution.\n")
    write("infrastructure/offline-package-cache/README.md", "# Offline package cache\n\nPopulate SDK and package caches during a reliable connection. Archive a tested cache with tool versions and checksums. Never claim a clean offline build will work without prior downloads.\n")
    write("infrastructure/offline-testing/README.md", "# Offline testing\n\nUse airplane mode, slow-network tooling where available, process restarts, limited storage, and queued mutations to test resilience.\n")
    write("infrastructure/backup-guides/README.md", "# Backup guides\n\nCommit locally, keep a copy on removable media, and periodically verify that a clone or archive restores.\n")
    write("templates/flutter-starter/README.md", "# Flutter local-first starter\n\nSuggested layers: `presentation/`, `domain/`, `data/local/`, `data/remote/`, and `data/sync/`. Write to Drift/SQLite first; queue a mutation with an idempotency key; expose sync state to the UI.\n")
    write("templates/react-native-starter/README.md", "# React Native local-first starter\n\nUse TypeScript, expo-sqlite, a repository boundary, persistent query/mutation state, and a durable queue. The screen must render local data when the API is unreachable.\n")
    write("templates/kotlin-starter/README.md", "# Kotlin local-first starter\n\nUse Compose → ViewModel → repository → Room as the main read path. Persist outgoing work and let WorkManager run it only under declared constraints.\n")

if __name__ == "__main__": main()
