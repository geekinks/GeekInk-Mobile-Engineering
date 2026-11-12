# Day 042: JSON and serialisation

**Track:** React Native Engineering  
**Module 05:** APIs and Synchronization  
**Scenario:** a farmer field observation

## Learning objectives

- Explain the purpose and trade-offs of json and serialisation.
- Implement one focused, testable slice using TypeScript and React Native components.
- State how the slice behaves with no network, little storage, or an unexpected shutdown.

## Prerequisites

Complete the earlier days in this module. Use a physical Android device when an emulator is slow or unavailable; the lesson can be read and planned offline.

## Concept

Separate local and remote sources for a farmer field observation. A sync queue stores an idempotency key, status, attempts, and last error. When a connection returns, retry bounded batches with exponential backoff; never block local use on the request.

## Practical code example

```ts
const message: string = 'Saved locally';
console.log(message);
```

This tiny example is deliberately observable: run it, change its value, and confirm the result before adding framework code.

## Step-by-step implementation

1. Create a branch or local commit named `day-042`.
2. Sketch the smallest screen or function that supports a farmer field observation.
3. Validate input before writing it; surface a human-readable error.
4. Persist essential data locally before attempting remote work.
5. Record pending network work with a stable operation ID when synchronization applies.
6. Test once online and once with airplane mode enabled.

## Hands-on exercise

Build a small feature for a farmer field observation. It must show a clear loading, success, empty, or error state appropriate to its current data. Add one test or a written manual test case covering an interruption.

## Mini challenge

Extend the feature so a user can leave the app after saving, reopen it, and still see the saved local result. If a server is involved, display **Pending sync**, **Synced**, or **Needs attention** rather than pretending every change is remote.

## Expected output

A focused, readable implementation and a screenshot or short written test record showing the feature works on a device or simulator. Data created while offline remains visible after restart.

## Assessment criteria

| Criterion | Weight |
| --- | ---: |
| Correct implementation and readable code | 35% |
| Local data, validation, and error handling | 25% |
| Offline/interruption test evidence | 20% |
| Accessibility and resource-aware choices | 10% |
| Reflection and documentation | 10% |

## Offline considerations

Do not use a connectivity check as permission to erase or disable essential work. Queue retryable changes, make retries idempotent, and keep server-only actions explicitly labelled. Reconcile conflicts using a documented rule such as field-level merge, last-write-with-review, or user choice.

## Low-resource considerations

Prefer physical-device testing, small sample data, compressed media, paginated lists, and incremental builds. Close memory-heavy tools before building. Do not assume a clean build will work offline unless dependencies and SDK packages were previously cached.

## Additional learning resources

- [Offline-first principles](../../../../docs/offline-first-principles.md)
- [Low-resource development](../../../../docs/low-resource-development.md)
- Official documentation bundled or cached by your cohort; download only when connectivity is available.

## Submission instructions

Open a GitHub issue or pull request using the [submission template](../../../../task/submission-template.md). Include your repository link, one screenshot or written verification, the offline condition tested, and one lesson learned. Video is optional.
