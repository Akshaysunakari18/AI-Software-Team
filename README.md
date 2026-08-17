# 🤖 AI Software Team

An autonomous multi-agent software development system that takes a natural-language software requirement, generates the required Python code, creates automated tests, validates the implementation, fixes failures through an iterative feedback loop, and pushes approved code to GitHub.

---

## 🚀 Project Overview

The AI Software Team simulates a small software engineering team using multiple AI agents.

Instead of manually writing and testing every project, the user provides a requirement such as:

> Build a Python student marks management system.

The system automatically:

1. Receives the requirement.
2. Sends it to the Coding Agent.
3. Generates the required Python project.
4. Sends the generated project to the Testing Agent.
5. Generates pytest test cases.
6. Runs the tests.
7. If tests fail, sends the failure feedback back to the Coding Agent.
8. Re-tests the corrected implementation.
9. If all tests pass, the Manager Agent approves the project.
10. The GitHub Agent commits and pushes the approved project to the `developer` branch.

---

# 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │      USER        │
                    │   Requirement    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  MANAGER AGENT   │
                    │  Orchestrator    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  CODING AGENT    │
                    │ Generate Project │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ GENERATED CODE   │
                    │    workspace/   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ TESTING AGENT    │
                    │ Generate pytest  │
                    │      Tests       │
                    └────────┬─────────┘
                             │
                             ▼
                       ┌────────────┐
                       │   PYTEST   │
                       └─────┬──────┘
                             │
                    ┌────────┴────────┐
                    │                 │
                  FAIL              PASS
                    │                 │
                    ▼                 ▼
            ┌──────────────┐   ┌──────────────┐
            │ Coding Agent │   │ Manager      │
            │ Fixes Code   │   │ Approves     │
            └──────┬───────┘   └──────┬───────┘
                   │                  │
                   └──────►           ▼
                            ┌──────────────────┐
                            │  GITHUB AGENT    │
                            │ Commit & Push    │
                            └────────┬─────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │ GitHub Developer │
                            │     Branch       │
                            └──────────────────┘