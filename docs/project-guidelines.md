# Project guidelines

GeekInk — **Builders Who Leave a Mark.** This guide is designed for learners who may work with expensive data, interrupted electricity, and modest hardware. Keep a local copy with the repository.

## Purpose

Start with an offline user journey and a small data model. Define local storage, sync boundaries, idempotency, conflict policy, storage limits, privacy, tests, and a recovery path before UI polish. Clearly label features as fully offline, locally available, or eventually connected.

## Practical checklist

- Work in small commits; after an unexpected shutdown, run the smallest useful test first.
- Keep source code, sample data, and instructions usable without a cloud account.
- Test the essential flow in airplane mode before calling it complete.
- Record assumptions and observed device behaviour in your submission.

## Further study

Use downloaded official documentation when connectivity is available. Version-sensitive commands belong in the cohort's cached setup pack, not in assumptions about a fresh offline machine.
