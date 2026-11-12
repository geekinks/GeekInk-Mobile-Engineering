# GeekInk Mobile Engineering

> **Offline First. Low Resource. Resilient by Design.**  
> GeekInk — *Builders Who Leave a Mark.*

A practical, 300-day-equivalent learning repository: three independent 100-day Android-focused pathways for learners building under constrained connectivity, electricity, storage, and hardware conditions.

## Choose a pathway

| Pathway | Core stack | Local-first data |
| --- | --- | --- |
| [Dart and Flutter](curriculum/dart-flutter/README.md) | Dart, Flutter, Material 3 | Drift/SQLite |
| [React Native](curriculum/react-native/README.md) | TypeScript, React Native, Expo | expo-sqlite |
| [Kotlin Android](curriculum/kotlin-android/README.md) | Kotlin, Compose, Android SDK | Room |

Each path has ten modules of ten daily lessons, practical scenarios, a mini challenge, assessment criteria, offline and low-resource considerations, and submission guidance.

## What makes this curriculum different?

The UI reads from local data first. Essential work is saved before a network request, queued durable operations synchronize later, and users can see pending, successful, and failed synchronization. Learners practise idempotency, bounded retries, conflict handling, privacy, battery-aware background work, and recovery after interruptions.

Start with the [student guide](docs/student-guide.md), [environment setup](docs/environment-setup.md), and [offline-first principles](docs/offline-first-principles.md). Instructors should begin with the [instructor guide](docs/instructor-guide.md) and [local learning infrastructure](docs/local-learning-infrastructure.md).

## Repository map

- `curriculum/` — three complete 100-day pathways.
- `projects/` — beginner, intermediate, and advanced offline-first briefs.
- `exercises/` — track-specific practical work (linked from lessons as cohorts expand).
- `templates/` — local-first starter architecture guidance.
- `infrastructure/` — LAN hosting, caches, offline testing, and backups.
- `docs/` — learner, instructor, resilience, assessment, and capstone guides.
- `task/` — GitHub-based submission process without personal directories.

## Learning without the internet

Clone or download the repository while connected, then keep it on the learner device, a USB drive, or a local learning server. A cohort can host it over LAN with:

```bash
python3 -m http.server 8000
```

Read more in [local learning infrastructure](docs/local-learning-infrastructure.md). Toolchains cannot perform a clean offline build until their SDKs and dependencies have been downloaded and cached; the setup guide is explicit about this limitation.

## Validate the curriculum

No paid service or secret is required.

```bash
python3 scripts/validate_curriculum.py
python3 scripts/validate_links.py
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md), follow the [Code of Conduct](CODE_OF_CONDUCT.md), and report vulnerabilities through [SECURITY.md](SECURITY.md). See [implementation progress](docs/implementation-progress.md) for the maintained build checklist.
