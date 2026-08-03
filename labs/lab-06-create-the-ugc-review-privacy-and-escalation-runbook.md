# Lab 6 — Create the UGC, Review, Privacy and Escalation Runbook

- **Course:** Agentic AI for Instagram Marketing (C695)
- **Version:** v1.0 (3 August 2026)
- **Topic 3:** Automating Engagement and Community Management
- **Maps to:** LO4: Apply privacy, copyright, platform, brand, and escalation rules to reviews, user-generated content, community responses, and AI-supported incident handling
- **Tools:** Approved generative AI assistant, spreadsheet application, text editor, labs/resources/06-ugc-permission-register-starter.txt, labs/resources/harbour-hearth-ugc-scenarios.csv, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/05-community-response-router.md

**Duration:** 55 minutes

---

## What You Will Do

You extend the community router with a rights and responsibility gate for reviews and user-generated content. The runbook records permission scope, checks AI drafts for truthful and fair treatment, and gives the team a practical response when content, privacy, or automation goes wrong.

## What You Will Build

C695-campaign-pack/06-ugc-and-governance-runbook.md plus 06-ugc-permission-register.csv containing rights decisions, privacy and truth checks, escalation templates, retention rules, and an incident simulation.

## Prerequisites

- Completed Lab 5 with the intent router and human owners available.
- Open the final 02-agent-prompt-contract.md and apply it to the rights-and-responsibility review.
- Open the synthetic UGC scenarios; do not contact any real account or rights holder.
- Treat public visibility as discovery only, never as permission to reuse.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Copy the supplied eight-row starter into 06-ugc-permission-register.csv and keep the exact header below.**

```text
Source: labs/resources/06-ugc-permission-register-starter.txt
Output header: ugc_id,content_type,discovery_source,people_or_identifiers,third_party_assets,proposed_use,permission_status,permission_scope,expiry_or_withdrawal,required_edits,reviewer,reply_decision,reuse_decision,evidence_ref,reason
```

**2. Read all scenarios and separate the decision to reply from the decision to reuse. A business may write a courteous public reply while reuse remains prohibited or pending.**

```text
reply_decision labels: DRAFT REPLY | NO REPLY | HUMAN RESPONSE. reuse_decision labels: REQUEST PERMISSION | READY FOR RIGHTS REVIEW | STOP — DO NOT REUSE.
```

**3. Ask the AI to apply the saved G-C-A-T-E contract and identify rights and privacy questions without making a legal conclusion.**

```text
Apply the complete G-C-A-T-E contract in C695-campaign-pack/02-agent-prompt-contract.md. Review each synthetic Instagram review or UGC scenario as a rights-and-responsibility assistant.

Return: ugc_id | reply purpose | reuse purpose | people or personal data | image/video rights | music/text/logo/location issues | claim or endorsement risk | permission questions | required edits | reply_decision | reuse_decision | evidence_ref | human reviewer.

Rules:
- public content is not automatic permission;
- never invent consent, ownership, attribution, a rating, or a customer experience;
- quoted reviews must preserve meaning and cannot remove a material limitation;
- minors, health claims, visible third parties, copyrighted music, other brands, private locations, or uncertain ownership force STOP or specialist review;
- output is a review aid, not legal advice.
```

**4. Write a permission-request template that states the exact asset, proposed channel, format, editing, attribution, duration, commercial use, storage, and withdrawal contact. Do not use deceptive incentives or imply the person must agree.**

```text
Permission remains PENDING until recorded by the authorised owner. Silence is not permission.
```

**5. Create the responsible AI gate with six checks: purpose, data minimisation, rights, truth, fairness, and accountability. Define the evidence needed to pass each check and the owner for unresolved cases.**

```text
Any failed rights, privacy, or truth check forces STOP. Brand or format issues may be REVISE when they can be corrected without changing meaning.
```

**6. Add review-response rules. Thank genuine feedback without fabricating investigation outcomes; avoid arguments; move order or personal details to a private authorised route; flag suspected fake reviews for platform and human review; never generate a fake positive review.**

```text
A response may acknowledge experience and explain the next contact step; it may not promise a refund, admission, deletion, or compensation without owner approval.
```

**7. Define retention and withdrawal handling. Record where permission evidence is stored, who can access it, review date, expiry, channels covered, and the action when permission is withdrawn or content is deleted at source.**

```text
Withdrawal path: stop new use → locate active placements → remove where controlled → update register → notify owner → retain only necessary decision evidence.
```

**8. Create the incident runbook: detect, pause, preserve a minimal secure log, contain, notify owners, correct or remove, respond to the affected person, diagnose the failed rule, test with synthetic cases, approve restoration, and monitor.**

```text
Required owners: Community, Brand, Privacy, Rights, Safety, and Technical Workflow Owner.
```

**9. Simulate this incident: the workflow reused an image marked PENDING and generated a caption implying a customer endorsement. Record immediate actions, public correction, rights-owner contact path, root cause, guardrail change, restoration test, and final owner approval.**

```text
Expected immediate status: PAUSE UGC WORKFLOW — RIGHTS AND TRUTH INCIDENT.
```

## Test It

Every UGC row must have distinct reply_decision and reuse_decision values, permission status, scope or missing-scope reason, reviewer, and an evidence_ref pointing to a scenario row, permission record, or named policy rule. The incident simulation must pause the workflow, prevent further reuse, correct the unsupported endorsement, update the permission rule, and require a synthetic restoration test. No scenario may move from public discovery directly to reuse.

## Checkpoint for the Next Lab

Keep the permission register, responsible AI gate, and incident runbook. Labs 7 and 8 will add evidence-linked performance decisions while reusing the same privacy, rights, and approval boundaries.

## Troubleshooting

- **The team treats attribution as permission:** Record attribution and permission as separate fields; both may be required, and neither substitutes for the other.
- **The AI gives a definitive copyright conclusion:** Change its role to identify issues and questions, then route uncertain ownership or scope to the authorised reviewer.
- **The incident plan says only 'delete the post':** Add containment, secure evidence, affected-person response, root cause, rule correction, restoration test, and monitoring.

## Challenge

Add a quarterly rights-audit query that identifies expired permissions, missing scope, withdrawn consent, deleted source content, and assets without a reviewer.

## Reflection

What is the most important difference between finding community content, replying to it, and reusing it in marketing?

---

[← Lab 5](lab-05-build-the-comment-and-direct-message-response-router.md) · [Lab 7 →](lab-07-build-the-instagram-insights-dashboard-and-evidence-linked-report.md)
