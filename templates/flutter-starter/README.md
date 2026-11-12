# Flutter local-first starter

Suggested layers: `presentation/`, `domain/`, `data/local/`, `data/remote/`, and `data/sync/`. Write to Drift/SQLite first; queue a mutation with an idempotency key; expose sync state to the UI.
