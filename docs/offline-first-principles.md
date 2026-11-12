# Offline-first principles

GeekInk — **Builders Who Leave a Mark.** This guide is designed for learners who may work with expensive data, interrupted electricity, and modest hardware. Keep a local copy with the repository.

## Purpose

Local data is the primary UI source of truth. A repository mediates local and remote sources. Changes are written locally, assigned idempotency keys, queued, retried with bounded exponential backoff, and made visible as pending, synced, or failed. Eventual consistency needs an explicit conflict rule and audit information.

## Practical checklist

- Work in small commits; after an unexpected shutdown, run the smallest useful test first.
- Keep source code, sample data, and instructions usable without a cloud account.
- Test the essential flow in airplane mode before calling it complete.
- Record assumptions and observed device behaviour in your submission.

## Further study

Use downloaded official documentation when connectivity is available. Version-sensitive commands belong in the cohort's cached setup pack, not in assumptions about a fresh offline machine.
