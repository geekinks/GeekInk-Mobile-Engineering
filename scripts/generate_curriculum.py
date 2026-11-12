#!/usr/bin/env python3
"""Generate the 300 deliberately scoped GeekInk daily lesson documents.

The curriculum map lives here so titles, objectives and scenarios can be reviewed
without hand-editing hundreds of nearly identical files. Generated README files
are committed curriculum material, not runtime output.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    ("Mobile Engineering Foundations", ["Mobile engineering and community impact", "Install tools and preserve installers", "Physical-device debugging", "Mobile operating systems and app lifecycle", "Project structure and source control", "Hardware constraints and inclusive design", "Offline-first architecture", "Git without continuous internet", "Power-aware development workflow", "First resilient mobile screen"]),
    ("Language Fundamentals", ["Variables and types", "Control flow", "Functions", "Collections", "Objects and data models", "Errors and defensive programming", "Asynchronous work", "Data transformations", "Code organization", "Programming challenge: market calculator"]),
    ("Mobile UI and UX Engineering", ["Mobile design and task flows", "Layouts and components", "Material Design 3", "Navigation and routing", "Responsive interfaces", "Accessible interaction", "Forms and validation", "Loading and error states", "Empty and offline states", "Optimising UI for low-end devices"]),
    ("Local Storage and Offline Data", ["Local-first data modelling", "SQLite foundations", "CRUD operations", "Repository pattern", "Persistent preferences", "Files and media", "Migrations", "Transactions and integrity", "Local search and caching", "Offline data milestone"]),
    ("APIs and Synchronization", ["HTTP and REST", "JSON and serialisation", "Network awareness", "Remote and local data sources", "Sync queue design", "Idempotent mutations", "Retry and exponential backoff", "Conflict resolution", "Eventual consistency", "Synchronization observability"]),
    ("Authentication and Application Security", ["Authentication boundaries", "Authorization", "Secure local storage", "Tokens and session persistence", "Offline session policy", "Encryption fundamentals", "Secure communication", "Input validation", "Privacy and permissions", "Security review"]),
    ("Advanced Mobile Engineering", ["State management", "Architecture patterns", "Background processing", "Scheduled sync constraints", "Notifications", "Camera and media", "Location services", "Offline notifications", "Storage and resource optimisation", "Advanced engineering milestone"]),
    ("Testing and Performance", ["Unit tests", "UI and component tests", "Integration tests", "Offline-first tests", "Network interruption simulation", "Low-memory testing", "Battery profiling", "Storage profiling", "Logging and debugging", "Quality gate"]),
    ("Production Mobile Applications", ["Product discovery and planning", "Architecture proposal", "Implementation sprint: local features", "Implementation sprint: remote integration", "Sync implementation", "Performance pass", "Accessibility and security pass", "Release build", "Android deployment", "Production retrospective"]),
    ("Professional Engineering and Capstone", ["Clean Architecture", "SOLID and pragmatic boundaries", "Design patterns", "Versioning and release notes", "CI/CD without paid services", "Documentation and code review", "Open-source collaboration", "Production readiness", "Capstone hardening", "Capstone demonstration"]),
]

# Flutter begins only after learners have a working mental model of programs and
# can write, run, debug, and organise Dart console code. This deliberately
# mirrors the Python reference's foundations → language → functions progression.
DART_MODULES = [
    ("Programming and Mobile Software Foundations", ["What is a program?", "What is programming?", "Programming languages and translation", "What is software engineering?", "The mobile software engineer", "How mobile applications work", "Problem solving and algorithms", "Set up Dart and your workspace", "Git, files, and local backups", "Your first Dart program"]),
    ("Dart Programming Fundamentals", ["Dart syntax, main, and print", "Variables and naming", "Data types and type inference", "Type conversion and user input", "Arithmetic, comparison, and logical operators", "Strings and interpolation", "Conditional statements", "Loops", "Functions and return values", "Dart calculator challenge"]),
    ("Dart Core Skills", ["Lists and iteration", "Maps and sets", "Null safety", "Classes and objects", "Constructors and encapsulation", "Inheritance, interfaces, and mixins", "Exceptions and defensive programming", "Futures, async, and await", "Files, JSON, packages, and code organisation", "Dart console project: student records"]),
    ("Flutter Foundations and UI", ["Why Flutter and the widget tree", "Install Flutter and run on a physical device", "Flutter project structure", "Stateless and stateful widgets", "Layouts and constraints", "Material Design 3", "Forms and validation", "Navigation and routing", "Accessible responsive interfaces", "First Flutter offline-ready screen"]),
    ("Local Storage and Offline Data", MODULES[3][1]),
    ("APIs and Synchronization", MODULES[4][1]),
    ("Authentication, Security, and State", ["Authentication boundaries", "Authorization", "Secure local storage", "Tokens and session persistence", "Offline session policy", "Provider and Riverpod", "BLoC and Cubit", "Encryption and secure communication", "Input validation and privacy", "Security and state review"]),
    ("Advanced Flutter Engineering", ["Repository and clean architecture", "Background processing", "Scheduled sync constraints", "Push notifications", "Camera and media", "Location services", "Offline notifications", "Storage and resource optimisation", "Device APIs", "Advanced engineering milestone"]),
    ("Testing, Performance, and Production", ["Unit tests", "Widget tests", "Integration tests", "Offline-first tests", "Network interruption simulation", "Low-memory and battery profiling", "Logging and debugging", "Product planning and architecture", "Android release build and deployment", "Production retrospective"]),
    ("Professional Engineering and Capstone", MODULES[9][1]),
]

DART_EARLY = {
    1: ("A program is a precise, ordered set of instructions that tells a computer how to transform input into useful output. A calculator, attendance app, and reminder are all programs. Before writing code, identify the user, input, processing, output, and what must remain useful when the network is absent.", "void main() {\n  print('A program follows instructions.');\n}"),
    2: ("Programming is the work of analysing a problem, designing instructions, writing code, testing it, and improving it. Code is only one part: a useful solution also handles mistakes, maintains data, and communicates clearly with users.", "void main() {\n  const students = 30;\n  print('Attendance expected: $students');\n}"),
    3: ("A programming language lets people express instructions in a form a computer can translate. Dart source is compiled or run by Dart tooling; its rules for syntax and types help developers communicate unambiguously. Flutter later uses Dart, but today focus on the language itself.", "void main() {\n  const language = 'Dart';\n  print('I am learning $language');\n}"),
    4: ("Software engineering is the disciplined creation and maintenance of software. It includes requirements, design, version control, testing, security, release, and support—not only writing code. Offline-first design is an engineering decision because data loss and poor connectivity are system constraints.", "void main() {\n  const requirement = 'Save attendance without internet';\n  print(requirement);\n}"),
    5: ("A mobile software engineer designs, builds, tests, releases, and maintains applications for mobile devices. They consider touch interaction, accessibility, battery, storage, permissions, device differences, and intermittent networks alongside code quality.", "void main() {\n  const role = 'Mobile software engineer';\n  print('$role designs for real devices');\n}"),
    6: ("Mobile apps run under an operating system that manages memory, battery, permissions, processes, and background limits. An app may be paused or stopped at any time, so it must persist important work rather than relying only on in-memory variables.", "void main() {\n  const lifecycleRule = 'Persist essential work early';\n  print(lifecycleRule);\n}"),
    7: ("An algorithm is a finite, clear sequence of steps. Start with a small problem: validate a mark, decide pass/fail, then display the result. Draw or write the steps before coding; this makes bugs cheaper to find.", "void main() {\n  const mark = 62;\n  print(mark >= 50 ? 'Pass' : 'Try again');\n}"),
    8: ("Install Dart when a connection is available, run `dart --version`, and keep a copy of the installer and the downloaded SDK location. A physical phone is not needed for console Dart. Never promise an offline installation can download missing dependencies.", "void main() {\n  print('Dart environment verified');\n}"),
    9: ("A project is a deliberate folder of source code, notes, and configuration. Git records local history even with no internet. Commit after a working change and keep a second copy on trusted removable storage; a GitHub push can wait for connectivity.", "void main() {\n  print('Commit small, working changes locally');\n}"),
    10: ("A first program proves the edit-run-observe loop. Save `hello.dart`, run `dart run hello.dart`, change the message, and run it again. This feedback loop is the foundation for debugging larger mobile applications.", "void main() {\n  print('Hello, GeekInk!');\n  print('Builders Who Leave a Mark.');\n}"),
}

DART_BASICS = {
    11: ("Every Dart executable starts at `main`. Statements normally end in semicolons, and `print` makes program behaviour visible while learning and debugging.", "void main() {\n  print('Dart starts in main');\n}"),
    12: ("Variables give meaningful names to changing values. Use `final` when a value is assigned once and `const` for a compile-time constant; this prevents accidental changes.", "void main() {\n  final learner = 'Amina';\n  const cohort = 'GeekInk';\n  print('$learner — $cohort');\n}"),
    13: ("Dart has numbers, strings, booleans, lists, maps, and more. Type inference is convenient, but understand the value each variable can safely hold.", "void main() {\n  int marks = 75;\n  String name = 'Sadiya';\n  bool submitted = true;\n  print('$name: $marks, submitted: $submitted');\n}"),
    14: ("Convert text deliberately before calculation. User-provided text is untrusted: parse it safely and show an error instead of crashing when conversion fails.", "void main() {\n  final quantity = int.tryParse('12');\n  print(quantity ?? 0);\n}"),
    15: ("Operators calculate values and make decisions. Parenthesise non-obvious expressions, and use comparisons to describe a rule such as a pass mark.", "void main() {\n  const mark = 62;\n  print(mark >= 50 && mark <= 100);\n}"),
    16: ("Strings represent text. Interpolation with `$name` or `${expression}` keeps messages readable; do not construct user-facing text with confusing fragments.", "void main() {\n  const item = 'maize';\n  const bags = 4;\n  print('$bags bags of $item');\n}"),
    17: ("A conditional selects one path based on a boolean expression. Cover the valid, invalid, and boundary cases explicitly.", "void main() {\n  const balance = 500;\n  if (balance > 0) { print('Credit available'); } else { print('No credit'); }\n}"),
    18: ("Loops repeat a bounded task. Prefer iterating directly over a collection when possible, and avoid unnecessary work that drains a device battery.", "void main() {\n  for (final name in ['Amina', 'Bashir']) { print(name); }\n}"),
    19: ("Functions group a named behaviour, accept inputs through parameters, and return outputs. Small pure functions are easier to test than long mixed-purpose code.", "int total(int price, int quantity) => price * quantity;\nvoid main() => print(total(250, 3));"),
    20: ("Combine Dart fundamentals into a small console program before adding Flutter. Decompose the calculator into input parsing, calculation, and output functions, then test invalid input.", "double add(double a, double b) => a + b;\nvoid main() => print(add(12.5, 7.5));"),
}

TRACKS = {
    "dart-flutter": {"name": "Dart and Flutter Engineering", "language": "Dart", "ui": "Flutter widgets", "database": "Drift/SQLite", "state": "Provider, Riverpod, and BLoC/Cubit", "background": "Workmanager-compatible background tasks", "code": "final message = 'Saved locally';\nprint(message);"},
    "react-native": {"name": "React Native Engineering", "language": "TypeScript", "ui": "React Native components", "database": "expo-sqlite", "state": "Context, Zustand, Redux Toolkit, and TanStack Query", "background": "Expo background tasks where supported", "code": "const message: string = 'Saved locally';\nconsole.log(message);"},
    "kotlin-android": {"name": "Kotlin Native Android Engineering", "language": "Kotlin", "ui": "Jetpack Compose", "database": "Room", "state": "ViewModel and StateFlow", "background": "WorkManager", "code": "val message = \"Saved locally\"\nprintln(message)"},
}

SECTIONS = ["Learning objectives", "Prerequisites", "Concept", "Practical code example", "Step-by-step implementation", "Hands-on exercise", "Mini challenge", "Expected output", "Assessment criteria", "Offline considerations", "Low-resource considerations", "Additional learning resources", "Submission instructions"]

def lesson(track_slug, track, module_no, topic_no, title, modules):
    day = (module_no - 1) * 10 + topic_no
    scenario = ["a Kano student attendance register", "a clinic visit record", "a farmer field observation", "a small-shop inventory item", "a community transport note"][day % 5]
    storage = track["database"]
    concept = (f"{title} is practised in the context of {track['name']}. Build the essential action first, "
               f"then make its data safe on the device. A useful mobile application treats connectivity as an "
               f"enhancement: the interface reads a local source of truth and records a pending change for later synchronization.")
    code = track['code']
    console_dart = track_slug == "dart-flutter" and module_no <= 3
    if track_slug == "dart-flutter" and module_no == 1:
        concept, code = DART_EARLY[topic_no]
    elif track_slug == "dart-flutter" and module_no == 2:
        concept, code = DART_BASICS[day]
    elif module_no == 5 if track_slug == "dart-flutter" else module_no == 4:
        concept = f"Model {scenario} locally with {storage}. The screen reads the local database; a repository owns validation and transactions so a power loss or interrupted request cannot silently discard the record."
    elif module_no == 6 if track_slug == "dart-flutter" else module_no == 5:
        concept = f"Separate local and remote sources for {scenario}. A sync queue stores an idempotency key, status, attempts, and last error. When a connection returns, retry bounded batches with exponential backoff; never block local use on the request."
    elif module_no == 8 if track_slug == "dart-flutter" else module_no == 7:
        concept = f"Use {track['state']} to expose stable UI state and {track['background']} only for deferrable work. The operating system may delay work; the app must remain correct if it runs late, twice, or not at all."
    elif module_no == 9 if track_slug == "dart-flutter" else module_no == 8:
        concept = f"Verify {scenario} in normal, offline, slow-network, low-storage, and interrupted-process conditions. A test is valuable when it checks what the user keeps, sees, and can retry—not merely implementation details."
    medium = "Dart console programs" if console_dart else track['ui']
    build_unit = "program or function" if console_dart else "screen or function"
    return f'''# Day {day:03d}: {title}

**Track:** {track['name']}  
**Module {module_no:02d}:** {modules[module_no-1][0]}  
**Scenario:** {scenario}

## Learning objectives

- Explain the purpose and trade-offs of {title.lower()}.
- Implement one focused, testable slice using {track['language']} and {medium}.
- State how the slice behaves with no network, little storage, or an unexpected shutdown.

## Prerequisites

Complete the earlier days in this module. Use a physical Android device when an emulator is slow or unavailable; the lesson can be read and planned offline.

## Concept

{concept}

## Practical code example

```{ "dart" if track_slug == "dart-flutter" else "ts" if track_slug == "react-native" else "kotlin" }
{code}
```

This tiny example is deliberately observable: run it, change its value, and confirm the result before adding framework code.

## Step-by-step implementation

1. Create a branch or local commit named `day-{day:03d}`.
2. Sketch the smallest {build_unit} that supports {scenario}.
3. Validate input before writing it; surface a human-readable error.
4. Persist essential data locally before attempting remote work.
5. Record pending network work with a stable operation ID when synchronization applies.
6. Test once online and once with airplane mode enabled.

## Hands-on exercise

Build a small feature for {scenario}. It must show a clear loading, success, empty, or error state appropriate to its current data. Add one test or a written manual test case covering an interruption.

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
'''

def main():
    curriculum = ROOT / "curriculum"
    for slug, track in TRACKS.items():
        track_dir = curriculum / slug
        modules = DART_MODULES if slug == "dart-flutter" else MODULES
        rows = []
        for m, (module, topics) in enumerate(modules, 1):
            mod_dir = track_dir / f"module-{m:02d}"
            links = []
            for n, title in enumerate(topics, 1):
                day = (m - 1) * 10 + n
                d = mod_dir / f"day-{day:03d}"
                d.mkdir(parents=True, exist_ok=True)
                (d / "README.md").write_text(lesson(slug, track, m, n, title, modules), encoding="utf-8")
                links.append(f"| {day:03d} | {title} | [Lesson](day-{day:03d}/README.md) |")
                rows.append(f"| {day:03d} | Module {m:02d} | {title} | [Lesson](module-{m:02d}/day-{day:03d}/README.md) |")
            (mod_dir / "README.md").write_text(f"# Module {m:02d}: {module}\n\n**Days {(m-1)*10+1:03d}–{m*10:03d} | {track['name']}**\n\n## Outcomes\n\nBy the end of this module, you can apply its skills to a local-first mobile feature and explain its offline, power, and storage trade-offs.\n\n## Daily lessons\n\n| Day | Topic | Lesson |\n| ---: | --- | --- |\n" + "\n".join(links) + "\n\n## Module milestone\n\nDeliver a small, tested feature for a community scenario. Preserve essential data locally and document one interruption test.\n", encoding="utf-8")
        (track_dir / "README.md").write_text(f"# {track['name']} — 100-Day Pathway\n\nThis path teaches professional mobile engineering through local-first applications for constrained environments. The primary local store is **{track['database']}**; state techniques include **{track['state']}**.\n\n| Day | Module | Topic | Lesson |\n| ---: | --- | --- | --- |\n" + "\n".join(rows) + "\n", encoding="utf-8")
    (curriculum / "README.md").write_text("# GeekInk Mobile Engineering Curriculum\n\nChoose one 100-day pathway, or use the shared module sequence to compare approaches. Every lesson includes practical work, an offline test, and low-resource guidance.\n\n- [Dart and Flutter](dart-flutter/README.md)\n- [React Native](react-native/README.md)\n- [Kotlin Android](kotlin-android/README.md)\n", encoding="utf-8")

if __name__ == "__main__":
    main()
