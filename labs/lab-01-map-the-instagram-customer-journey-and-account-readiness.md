# Lab 1 — Map the Instagram Customer Journey and Account Readiness

- **Course:** Agentic AI for Instagram Marketing (C695)
- **Version:** v1.0 (3 August 2026)
- **Topic 1:** Foundations of Agentic AI for Instagram Marketing
- **Maps to:** LO1: Explain AI agents and map the customer journey, account readiness, tools, evidence, and approval gates for an Instagram workflow
- **Tools:** Approved generative AI assistant, text editor, labs/resources/harbour-hearth-brand-brief.md, labs/resources/harbour-hearth-audience-signals.csv, optional view-only Instagram Professional account

**Duration:** 50 minutes

---

## What You Will Do

You begin the connected Harbour & Hearth scenario by turning an approved synthetic brand brief and audience signals into a measurable Instagram customer journey. You then complete a Professional-account readiness and tool-permission map so every later agent knows what it may read, draft, recommend, or hand to a human.

## What You Will Build

C695-campaign-pack/01-foundation-and-readiness.md containing the decision chain, five-stage customer journey, tool-role map, account-readiness checklist, risk tiers, and approval gates.

## Prerequisites

- Create a local folder named C695-campaign-pack.
- Open the synthetic brand brief and audience-signals CSV; do not add real account or customer data.
- Use a new AI chat in an organisation-approved tool.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Create 01-foundation-and-readiness.md with headings for Decision Chain, Customer Journey, Tool Map, Account Readiness, and Approval Gates.**

```text
File: C695-campaign-pack/01-foundation-and-readiness.md
```

**2. Read the brand brief without AI. List approved offer facts, the desired customer action, operating constraints, and every explicit unknown. Keep the source heading beside each fact.**

```text
Rule: sourced fact / labelled hypothesis / UNKNOWN — do not create a fourth category.
```

**3. Write the measurable decision chain at the top of the file. Use completed Sunrise Breakfast Box pre-orders as the customer action and name one primary outcome plus two guardrails.**

```text
Because <BUSINESS RESULT>, Instagram will help <AUDIENCE NEED> by encouraging <CUSTOMER ACTION>; we will judge it by <PRIMARY OUTCOME> while protecting <GUARDRAIL 1> and <GUARDRAIL 2>.
```

**4. Ask the AI to map the customer journey using only the supplied synthetic sources. Paste the brand brief and audience signals where indicated.**

```text
You are an Instagram customer-journey analyst. Use only the supplied synthetic brand brief and audience signals. Do not invent demographics, testimonials, product claims, prices, performance, or account features.

Return a Markdown table with exactly five stages: Discover, Evaluate, Engage, Act, Return.
Columns: Stage | Customer question | Evidence IDs | Instagram content or interaction job | Desired micro-action | Measurement | Risk or unknown | Human decision.

For each row:
- cite at least one source heading or signal ID;
- label inference as HYPOTHESIS;
- use UNKNOWN when the source is silent;
- separate organic content, community interaction, and paid delivery roles.

BRAND BRIEF:
<PASTE BRAND BRIEF>

AUDIENCE SIGNALS:
<PASTE CSV ROWS>
```

**5. Review the journey row by row. Remove invented details and ensure every stage connects to the same pre-order action without pretending a view, like, save, or message is a purchase.**

```text
Required distinction: micro-action supports the journey; the completed pre-order is the business outcome.
```

**6. Create a tool-role table for an AI assistant, image tool, spreadsheet, Meta Business Suite, n8n, and the Instagram API. Record read, draft, recommend, or external-action capability; required data; risk tier; owner; and fallback.**

```text
Risk guide: LOW = synthetic/read-only; MEDIUM = create or classify drafts; HIGH = publish, message, collect personal data, change audience, or change spend.
```

**7. Complete the Professional-account readiness checklist. Record status as READY, NOT READY, or OWNER TO VERIFY; never paste a username, token, recovery code, or customer identifier.**

```text
Check: Business or Creator account; correct public identity; bio/contact/link; account owner; multi-factor authentication; connected Meta assets where required; role permissions; Singapore time zone; approved data sources; publishing and messaging authority; revoke path; draft-mode test.
```

**8. Add approval gates and stop conditions. Publishing, direct messaging, lead-data collection, UGC reuse, audience creation, ad activation, budget changes, and any unsupported claim must stop for the named human owner.**

```text
Status labels: DRAFT | READY FOR HUMAN REVIEW | APPROVED BY <ROLE> | STOP — <REASON>.
```

**9. Add a Review Log with your initials, date, three corrections made to the AI output, and unresolved account-readiness items.**

```text
## Review Log
- Reviewer: <INITIALS>
- Date: <YYYY-MM-DD>
- Corrections: <LIST>
- Owner to verify: <LIST>

| Fact checked | Source heading or signal ID | Expected | Observed | Result |
|---|---|---|---|---|
| <FACT 1> | <SOURCE> | <EXPECTED> | <OBSERVED> | PASS / REVISE |
| <FACT 2> | <SOURCE> | <EXPECTED> | <OBSERVED> | PASS / REVISE |
| <FACT 3> | <SOURCE> | <EXPECTED> | <OBSERVED> | PASS / REVISE |
```

## Test It

Open 01-foundation-and-readiness.md. It must contain five journey stages, at least one source reference per stage, a tool map with six tools, all twelve readiness checks, and explicit human gates for public action, personal data, UGC reuse, targeting, and spend. Select three factual statements at random; each must trace to the supplied sources, and the Review Log must retain the source, expected value, observed value, and PASS or REVISE result.

## Checkpoint for the Next Lab

Keep 01-foundation-and-readiness.md. Lab 2 turns its decisions, tools, unknowns, and authority boundaries into a reusable prompt contract.

## Troubleshooting

- **The journey is only a list of content formats:** Rewrite each row around a customer question, evidence, micro-action, measurement, and human decision.
- **The checklist asks for access tokens:** Remove secret values. Record only status, owner, permission scope, test result, and revoke path.
- **The agent treats engagement as revenue:** Separate leading indicators from the completed pre-order and label attribution limitations.

## Challenge

Add a RACI-style ownership row for brand review, privacy review, publishing, customer escalation, analytics, and budget approval.

## Reflection

Which Instagram workflow action has the highest combined customer, brand, and financial impact, and what evidence should a human see before approving it?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-write-and-test-the-instagram-agent-prompt-contract.md)
