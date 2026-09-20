# Agentic AI Applications with Codex

Official learner courseware and hands-on activities for **C695 — Agentic AI Applications with Codex**, a one-day, 7.5-hour course by Tertiary Infotech.

| Course detail | Information |
|---|---|
| Course code | `C695` |
| Programme | Non-WSQ commercial short course |
| Duration | 1 day / 7.5 instructional hours |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/agentic-ai-applications-with-codex.html) |

## About the course

This practical course shows developers and technical teams how to use Codex as a governed coding agent: establishing repository context, planning bounded changes, working with tools and approvals, coordinating parallel tasks, verifying outcomes, and evaluating adoption readiness.

## Learning outcomes

By the end of the course, learners can:

- analyse an agentic coding task and choose an appropriate Codex execution surface;
- write bounded instructions and apply repository context, sandbox and approval controls;
- use tools, skills, subagents and cloud automation while retaining human accountability;
- evaluate functional correctness, reliability, cost, risk and adoption readiness using repeatable evidence.

## Topics covered

The course follows the same topic sequence as the WSQ programme, compressed into one focused day:

1. Understand Codex as an agentic coding system and establish a safe repository baseline.
2. Turn a feature request into a bounded plan and implementation.
3. Control agent behaviour with scoped instructions, sandboxing and approval policies.
4. Coordinate parallel work with worktrees and verify browser-facing changes.
5. Package reusable skills and automate headless Codex execution.
6. Evaluate agent quality with golden tasks and design governed adoption.

## Activities

| # | Activity | Main outcome |
|---|---|---|
| 01 | [Repository Reconnaissance and Baseline](labs/lab-01-repository-reconnaissance/README.md) | Evidence-backed repository map and baseline checks |
| 02 | [Prompt-to-Plan Feature Delivery](labs/lab-02-prompt-plan-feature/README.md) | Scoped implementation plan and verified change |
| 03 | [Scoped AGENTS.md Hierarchy](labs/lab-03-agents-hierarchy/README.md) | Predictable instruction hierarchy |
| 04 | [Sandbox and Approval Experiment](labs/lab-04-sandbox-approval/README.md) | Safe permissions and approval boundaries |
| 05 | [Parallel Worktrees without Collision](labs/lab-05-parallel-worktrees/README.md) | Independent concurrent work streams |
| 06 | [Browser QA with Playwright](labs/lab-06-browser-qa/README.md) | Reproducible UI verification evidence |
| 07 | [Build and Evaluate a Codex Skill](labs/lab-07-reusable-skill/README.md) | Reusable skill package and evaluation |
| 08 | [Headless Codex Exec for CI](labs/lab-08-headless-exec/README.md) | Scriptable non-interactive agent workflow |
| 09 | [Golden-Task Evaluation Harness](labs/lab-09-evaluation-harness/README.md) | Repeatable quality and regression checks |
| 10 | [Governed Codex Adoption](labs/lab-10-capstone-governed-adoption/README.md) | Capstone operating model with controls |

Each activity folder contains self-contained instructions, a prompt contract, scoped `AGENTS.md` guidance and evidence checks.

## Public package and distribution boundary

The public learner package contains the editable and rendered slides, Learner Guide, Lesson Plan, and the complete activities tree. Assessment instruments, answer keys, credentials, private source references, and build-only QA renders are deliberately excluded.

## Repository structure

```text
C695-Agentic-AI-Applications-with-Codex/
├── README.md
├── LG-Agentic AI Applications with Codex (C695).md
├── courseware/
│   ├── Agentic AI Applications with Codex (C695)-v1.0.pptx
│   ├── Agentic AI Applications with Codex (C695)-v1.0.pdf
│   ├── LG-Agentic AI Applications with Codex (C695).docx
│   ├── LG-Agentic AI Applications with Codex (C695).pdf
│   ├── LP-Agentic AI Applications with Codex (C695).docx
│   └── LP-Agentic AI Applications with Codex (C695).pdf
└── labs/
    ├── README.md
    └── lab-01-... through lab-10-...
```

## Getting started

1. Open the Learner Guide for the concepts and detailed procedures.
2. Read [`labs/README.md`](labs/README.md).
3. Complete Activities 01–10 in sequence, keeping the requested evidence from each activity.
4. Use a practice repository and follow the approval boundaries defined by the trainer.

```bash
git clone https://github.com/tertiarycourses/C695-Agentic-AI-Applications-with-Codex.git
cd C695-Agentic-AI-Applications-with-Codex
```

## License

These materials are provided for educational use as part of **C695 — Agentic AI Applications with Codex**. © Tertiary Infotech Pte. Ltd. All rights reserved.
