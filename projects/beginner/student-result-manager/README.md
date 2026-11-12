# Student Result Management App

## Problem statement

Record and calculate student results locally with privacy safeguards.

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
