# Lab 5 — Build the Comment and Direct-Message Response Router

- **Course:** Agentic AI for Instagram Marketing (C695)
- **Version:** v1.0 (3 August 2026)
- **Topic 3:** Automating Engagement and Community Management
- **Maps to:** LO3: Design a governed workflow for comment and direct-message intent, risk, lead capture, personalised drafts, follow-up, and human escalation
- **Tools:** Approved generative AI assistant, spreadsheet application, text editor, labs/resources/harbour-hearth-community-scenarios.csv, labs/resources/harbour-hearth-brand-brief.md, C695-campaign-pack/02-agent-prompt-contract.md

**Duration:** 50 minutes

---

## What You Will Do

You design a community agent that routes eight synthetic Instagram comments and direct messages without exposing identifiers or promising unauthorised outcomes. The router drafts from approved facts for routine cases, captures only minimum lead fields, and stops for safety, allergy, payment, refund, privacy, or order-specific requests.

## What You Will Build

C695-campaign-pack/05-community-response-router.md plus 05-response-queue.csv containing the intent taxonomy, risk rules, minimum-data lead schema, reviewed response drafts, escalation owners, and a workflow dry-run.

## Prerequisites

- Completed Labs 1 to 4 and keep the G-C-A-T-E contract active.
- Use only the synthetic messages; do not paste a real Inbox export.
- All responses remain drafts and no direct message is sent.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Create 05-community-response-router.md with sections for Intent Taxonomy, Risk Rules, Lead Capture, Response Templates, Workflow, and Review Log.**

```text
File: C695-campaign-pack/05-community-response-router.md
```

**2. Define six intent categories: informational, commercial question, lead request, order service, sensitive issue, and abuse or spam. Assign each a default public/private route, risk tier, owner, and response-time target.**

```text
Sensitive includes health, allergy, safety, payment, privacy, legal, threat, and crisis content. Order-specific changes require identity and order verification outside the AI workflow.
```

**3. Create the response queue with the exact header below. Copy scenario IDs and messages from the synthetic CSV, then mask any phone number or order reference before AI classification.**

```text
scenario_id,masked_message,intent,confidence,risk_tier,public_or_private,approved_source,response_action,owner,draft_status,reason
```

**4. Ask the AI to classify the masked scenarios and propose a draft or escalation record.**

```text
Apply the G-C-A-T-E contract to each synthetic Instagram message.

Return: scenario_id | intent | confidence high/medium/low | risk low/medium/high | public/private route | exact approved source | response action DRAFT/ASK ONE QUESTION/ESCALATE/NO RESPONSE | draft wording | human owner | reason.

Rules:
- use only approved brand-brief facts;
- do not repeat identifiers or request credentials;
- do not confirm order changes, refunds, compensation, medical advice, liability, or account outcomes;
- move personal, order, payment, allergy, safety, and complaint details to an approved private human channel;
- low confidence or missing facts = ESCALATE;
- all wording remains DRAFT — HUMAN REVIEW REQUIRED.
```

**5. Review each result against the message and brand brief. Routine collection-window and pre-order-link questions may receive a sourced draft. Allergy, refund, order change, duplicate charge, weekend uncertainty, and illness reports must escalate without an invented answer.**

```text
Expected high-risk owners: Service Owner for order/refund/payment; Safety Owner for allergy or illness; Privacy Owner for personal-data concerns.
```

**6. Write the minimum-data lead-capture schema for a person who explicitly asks for a corporate breakfast quote. Use an approved form rather than the AI chat.**

```text
Fields: contact name, work email, approximate quantity, requested date, request summary, consent or authorised basis, source, assigned owner, status, retention date. Prohibited: age, home address, ethnicity, health, income, password, payment number, or unrelated message history.
```

**7. Add follow-up rules. State the purpose before collection, send only the promised response, record consent or basis, assign an owner, suppress further marketing when consent is withdrawn, and remove the lead when the retention rule expires.**

```text
A lead response may be personalised from the stated request and approved offer facts; it may not infer a person's role, urgency, budget, or preferences.
```

**8. Design the node-by-node community workflow: receive event, minimise and mask, deterministic sensitive-keyword check, AI intent classification, confidence gate, retrieve approved response, human review, reply placeholder, lead hand-off, log, and error path.**

```text
Instagram messaging conversations and API capabilities have platform permissions and interaction limits. Record OWNER TO VERIFY CURRENT PLATFORM RULES rather than hard-coding an unverified production assumption.
```

**9. Dry-run all eight scenarios. Record the intended route and compare it with the expected safety rules. Any scenario that exposes identifiers, invents a fact, or sends a high-risk draft without escalation must be corrected and rerun.**

```text
Pass rule: 8 of 8 scenarios have a defensible route; all high-risk scenarios show STOP — HUMAN ESCALATION.
```

## Test It

Open 05-response-queue.csv and confirm eight scenario IDs, masked identifiers, one intent, one risk tier, one route, one owner, and one reason per row. M01 and M05 may be drafted from approved facts; M02, M03, M04, M06, M07, and M08 must not receive a confident automated resolution. No raw phone number or real customer data may appear in either output.

## Checkpoint for the Next Lab

Keep the reviewed taxonomy, queue, lead schema, and escalation owners. Lab 6 adds review and UGC permission handling, privacy and copyright checks, and the incident response path.

## Troubleshooting

- **The agent classifies a message correctly but answers unsafely:** Evaluate routing and wording separately; high-risk intent always forces the escalation action before drafting.
- **A lead record contains too much data:** Start from the promised follow-up purpose and delete every field not needed to deliver it.
- **Confidence is always high:** Require evidence for the label and use low confidence when the approved knowledge source cannot answer the request.

## Challenge

Add multilingual detection that routes unsupported languages to a human instead of translating sensitive content automatically.

## Reflection

Why is a correct escalation often a better community outcome than a fast personalised answer?

---

[← Lab 4](lab-04-build-the-content-calendar-agent-and-publishing-workflow.md) · [Lab 6 →](lab-06-create-the-ugc-review-privacy-and-escalation-runbook.md)
