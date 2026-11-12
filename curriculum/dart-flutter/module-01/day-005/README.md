# Day 005: The mobile software engineer

**Track:** Dart and Flutter Engineering  
**Module 01:** Programming and Mobile Software Foundations  
**Scenario:** a Kano student attendance register

## Learning objectives

- Explain the purpose and trade-offs of the mobile software engineer.
- Implement one focused, testable slice using Dart and Dart console programs.
- State how the slice behaves with no network, little storage, or an unexpected shutdown.

## Prerequisites

Complete the earlier days in this module. Use a physical Android device when an emulator is slow or unavailable; the lesson can be read and planned offline.

## Concept

A mobile software engineer designs, builds, tests, releases, and maintains applications for mobile devices. They consider touch interaction, accessibility, battery, storage, permissions, device differences, and intermittent networks alongside code quality.

## Practical code example

```dart
void main() {
  const role = 'Mobile software engineer';
  print('$role designs for real devices');
}
```

This tiny example is deliberately observable: run it, change its value, and confirm the result before adding framework code.

## Step-by-step implementation

1. Create a branch or local commit named `day-005`.
2. Sketch the smallest program or function that supports a Kano student attendance register.
3. Validate input before writing it; surface a human-readable error.
4. Persist essential data locally before attempting remote work.
5. Record pending network work with a stable operation ID when synchronization applies.
6. Test once online and once with airplane mode enabled.

## Hands-on exercise

Build a small feature for a Kano student attendance register. It must show a clear loading, success, empty, or error state appropriate to its current data. Add one test or a written manual test case covering an interruption.

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
