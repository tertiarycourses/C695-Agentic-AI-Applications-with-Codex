# Lab 4 — Build the Content Calendar Agent and Publishing Workflow

- **Course:** Agentic AI for Instagram Marketing (C695)
- **Version:** v1.0 (3 August 2026)
- **Topic 2:** AI-Powered Content Creation and Scheduling
- **Maps to:** LO2: Build a brand-consistent calendar agent and controlled scheduling workflow with approval, duplicate prevention, failure handling, and verification
- **Tools:** Approved generative AI assistant, spreadsheet application, text editor, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/03-instagram-content-kit.md, optional Meta Business Suite or n8n view-only access

**Duration:** 60 minutes

---

## What You Will Do

You convert the reviewed content kit into a seven-day Instagram calendar and a draft-first publishing workflow. The workflow can prepare and validate a schedule, but it stops at the human approval gate before Meta Business Suite or an API publishing action.

## What You Will Build

C695-campaign-pack/04-calendar-and-publishing-workflow.md plus 04-instagram-calendar.csv containing seven scheduled drafts, validation rules, a node-by-node n8n-style workflow, approval evidence, error handling, and a dry-run log.

## Prerequisites

- Completed Lab 3 with seven content IDs explicitly promoted to READY FOR HUMAN REVIEW.
- Open the final 02-agent-prompt-contract.md and apply it to every AI-assisted workflow step.
- Use Asia/Singapore as the calendar time zone.
- Keep the publishing step disabled or represented by a placeholder; do not connect credentials.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Create 04-instagram-calendar.csv with exactly the required header and seven rows, one for each reviewed content ID.**

```text
content_id,date_sgt,time_sgt,format,journey_stage,pillar,asset_ref,caption_status,hashtag_status,rights_status,cta,destination,reviewer,approval_status,publish_status,learning_question
```

**2. Assign each content item to one day in a seven-day window. Balance customer-journey jobs, pillars, and formats; do not schedule two items for the same minute.**

```text
Use ISO dates and 24-hour Singapore time. Keep publish_status=DRAFT for all rows.
```

**3. Create 04-calendar-and-publishing-workflow.md. Define allowed status transitions and the composite duplicate key.**

```text
DRAFT → READY FOR HUMAN REVIEW → APPROVED BY <ROLE> → SCHEDULED → PUBLISHED or ERROR. Duplicate key: account placeholder + content_id + scheduled ISO timestamp.
```

**4. Write deterministic preflight rules. A row may reach the publishing placeholder only when content ID, asset, caption, hashtags, rights, CTA, destination, reviewer, approval evidence, time zone, and timestamp are present and compatible.**

```text
Fail closed on UNKNOWN rights, missing reviewer, missing approval, past timestamp, duplicate key, conflicting destination, or invalid status transition.
```

**5. Ask the AI to apply the saved G-C-A-T-E contract and turn the rules into a node-by-node n8n-style workflow specification.**

```text
Apply the complete G-C-A-T-E contract in C695-campaign-pack/02-agent-prompt-contract.md. Create a recommendation-only workflow specification with these nodes:
1. Manual Trigger for training; optional Schedule Trigger for a future approved deployment.
2. Read one calendar row.
3. Validate required fields and Asia/Singapore timestamp.
4. Check duplicate key against the log.
5. Retrieve the matching reviewed content brief.
6. Run factual, brand, rights, format, CTA, and destination checks.
7. Create a human approval request showing the final payload.
8. IF approved, send to a disabled PUBLISH PLACEHOLDER; otherwise STOP.
9. Write the decision and status to the log.
10. Error branch with retry limit 1, then human hand-off.

For each node return: purpose, input fields, deterministic rule, output fields, credential requirement, error path, and evidence retained. Do not include a real token or executable publishing request.
```

**6. Add a publishing checklist for an authorised owner using the current approved interface. It must verify account identity, final asset, caption, link, time zone, date and time, preview, permissions, reviewer, and rollback owner.**

```text
Optional view-only exploration: locate Planner or draft controls in Meta Business Suite and record interface differences; close without saving or scheduling.
```

**7. Create two dry-run inputs. Safe Row uses complete synthetic values and approval_status=APPROVED BY MARKETING OWNER. Unsafe Row removes approval and sets rights_status=UNKNOWN.**

```text
Expected Safe Row result: READY AT PUBLISH PLACEHOLDER — EXTERNAL ACTION DISABLED. Expected Unsafe Row result: STOP — APPROVAL AND RIGHTS REQUIRED.
```

**8. Add duplicate protection and retry behaviour. Replaying the same Safe Row must produce SKIP — DUPLICATE KEY, and a simulated publish error may retry once before ERROR — HUMAN HAND-OFF.**

```text
Never retry an unknown outcome in a way that could create a duplicate public post.
```

**9. Record all three dry-run results in a log with input hash or filename, validation outcome, approval status, proposed action, timestamp, and owner.**

```text
## Dry-Run Log
| Run | Input | Validation | Approval | Result | Owner |
|---|---|---|---|---|---|
```

## Test It

The calendar must have seven unique content IDs, ISO dates, Asia/Singapore times, and DRAFT publication status. The Safe Row must stop at the disabled publish placeholder; the Unsafe Row must stop for approval and rights; the replay must skip as a duplicate. No credential, token, real account ID, or live scheduling action may appear in the files.

## Checkpoint for the Next Lab

Keep 04-instagram-calendar.csv and the workflow dry-run log. Labs 5 and 6 add community events, response routing, and rights governance to the same operating system.

## Troubleshooting

- **The workflow relies on the AI to decide if fields are missing:** Move schema, timestamp, status, rights, approval, and duplicate checks into deterministic validation nodes.
- **A failed publish could create duplicates:** Use an idempotency key, inspect the action log, and hand off after one uncertain result instead of retrying blindly.
- **Calendar balance is arbitrary:** Use the customer-journey job, pillar, format, and learning question columns to justify every date choice.

## Challenge

Add an expiry rule that returns an approved row to REVIEW when the scheduled time changes, the asset changes, or more than seven days pass after approval.

## Reflection

Which validation belongs in a fixed rule rather than an AI judgement, and what failure would occur if the boundary were reversed?

---

[← Lab 3](lab-03-create-the-instagram-content-and-creative-kit.md) · [Lab 5 →](lab-05-build-the-comment-and-direct-message-response-router.md)
