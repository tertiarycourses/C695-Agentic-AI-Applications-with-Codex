# Lab 8 — Design and Simulate the Instagram Ads, Retargeting and Optimisation Loop

- **Course:** Agentic AI for Instagram Marketing (C695)
- **Version:** v1.0 (3 August 2026)
- **Topic 4:** Analytics, Ads and Optimisation with AI Agents
- **Maps to:** LO6: Design a human-governed Instagram ads and retargeting loop for audience, budget, and creative decisions using evidence, limits, approval, cooldown, and rollback
- **Tools:** Approved generative AI assistant, spreadsheet application, text editor, labs/resources/08-ads-runbook-starter.md, labs/resources/08-decision-log-starter.txt, labs/resources/harbour-hearth-optimisation-scenarios.csv, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/07-insights-dashboard.xlsx, C695-campaign-pack/07-performance-report.md

**Duration:** 55 minutes

---

## What You Will Do

You complete the connected course pack with an AI-assisted Instagram ads blueprint and a bounded continuous-improvement policy. You then run eight synthetic scenarios through the policy to prove that strong numbers cannot override tracking, customer, rights, capacity, cooldown, or human-approval guardrails.

## What You Will Build

C695-campaign-pack/08-ads-retargeting-optimisation-runbook.md plus 08-decision-log.csv and 08-course-pack-manifest.md containing the campaign hierarchy, audience roles, budget and creative hypotheses, retargeting data map, bounded policy, scenario decisions, rollback plan, and a validated inventory of artifacts 01 to 08.

## Prerequisites

- Completed Labs 1 to 7 with all numbered artifacts in C695-campaign-pack; use the Rejoin Path in the labs index to reconstruct any missing checkpoint first.
- Open the final 02-agent-prompt-contract.md and apply it to every AI-assisted campaign and optimisation decision.
- Use hypothetical budget values only; do not open or change a live advertising account.
- Keep account IDs, payment details, event verification, audience eligibility, and live settings as OWNER TO VERIFY.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Copy the supplied starter to 08-ads-retargeting-optimisation-runbook.md and complete its sections for Campaign Blueprint, Audience and Retargeting Map, Creative Test, Budget Policy, Decision Rules, Simulation, and Rollback.**

```text
Source: labs/resources/08-ads-runbook-starter.md
Output: C695-campaign-pack/08-ads-retargeting-optimisation-runbook.md
```

**2. Draft the campaign hierarchy from the approved pre-order goal: campaign objective and business reason; ad-set conversion location, event, audience role, location constraint, exclusions, placements, hypothetical budget, and schedule; ad identity, format, creative ID, text, destination, and tracking checks.**

```text
Use OWNER TO VERIFY for the current Meta objective options, verified event, account identity, payment method, platform eligibility, and live placement settings.
```

**3. Create two audience roles: one prospecting hypothesis and one retargeting hypothesis. For each state the customer state, authorised evidence, message job, exclusions, decision metric, privacy risk, and owner.**

```text
Do not invent demographic or sensitive traits. Audience suggestions are hypotheses; strict location, age, language, or exclusion controls require a genuine business or safety reason.
```

**4. Build the retargeting data map. Include source signal, collection purpose, notice or consent/basis, platform eligibility, retention, access, minimum audience concerns, exclusion after purchase, frequency control, deletion or suppression path, and owner.**

```text
Potential sources: eligible content engagement, website event, video view, approved lead, or authorised customer list. Availability and eligibility remain OWNER TO VERIFY.
```

**5. Define one controlled creative test based on Lab 7. Change exactly one variable, such as hook angle, while holding audience, offer, format, destination, budget, schedule, and optimisation stable.**

```text
Record hypothesis, control, treatment, primary metric, two guardrails, minimum window, minimum result count, practical threshold, stop rule, and decision owner.
```

**6. Write the bounded optimisation policy below. The agent recommends only; a named Marketing Owner approves every change.**

```text
ELIGIBILITY: at least 7 complete days, at least 20 purchases, clean tracking, no privacy concern, no unsupported claim, complaint rate at or below 2.0%, enough fulfilment capacity, at least 72 hours since the last material change, and approver available.
ALLOWED RECOMMENDATION: HOLD, STOP, draft one creative variant, or propose one budget change.
MAGNITUDE: at most 10% budget increase or decrease in one cycle.
ONE-LEVER RULE: do not change audience, budget, creative, placement, and destination together.
APPROVAL: named Marketing Owner must approve before any external change.
COOLDOWN: observe at least 72 hours after a material change.
ROLLBACK: restore the recorded prior configuration if tracking, complaint, capacity, rights, or performance guardrails fail.
LOG: source window, before value, recommendation, reason, owner, approval, timestamp, expected effect, result, and rollback status.
```

**7. Copy the supplied eight-row decision-log starter to 08-decision-log.csv and keep the exact header.**

```text
Source: labs/resources/08-decision-log-starter.txt
Output header: scenario_id,decision,blocking_guardrail,evidence,proposed_lever,magnitude,approver,cooldown_or_next_check,rollback,status_reason
```

**8. Ask the AI to apply the saved G-C-A-T-E contract and the policy to each scenario independently. It must test guardrails before performance and may not combine scenarios.**

```text
Apply the complete G-C-A-T-E contract in C695-campaign-pack/02-agent-prompt-contract.md. For each synthetic scenario return: scenario_id | ELIGIBLE yes/no | decision HOLD/STOP/PROPOSE | blocking guardrail | evidence fields | at most one proposed lever | magnitude | approval needed | next check | rollback | reason.

Apply the written policy exactly. A high ROAS cannot override a tracking error, complaint breach, capacity shortfall, low event volume, cooldown, missing approver, privacy concern, or unsupported claim. Never activate an ad or change a live setting.
```

**9. Review the eight decisions. SC01 may propose one change up to 10% because it meets the synthetic eligibility rules. SC02-SC08 must HOLD or STOP for their stated tracking, complaint, capacity, volume, cooldown, approver, or claim guardrail.**

```text
If any blocked scenario receives PROPOSE, strengthen the guardrail-first order and rerun all scenarios.
```

**10. Add the continuous feedback loop and rollback checklist: observe fixed window, validate, diagnose, propose one lever, approve, record before state, apply placeholder, observe cooldown, compare, retain or rollback, and update the learning log.**

```text
Public action, audience creation, ad activation, and spend remain disabled in this lab.
```

**11. Create 08-course-pack-manifest.md and inventory every expected artifact from 01 through 08. Validate cross-artifact consistency before closing the lab.**

```text
Manifest columns: Artifact | Present | Version or date | Final status | Source or provenance | Owner | Unresolved OWNER TO VERIFY. Cross-check the same customer action, approved offer facts, content IDs, account placeholder, time zone, status vocabulary, rights state, primary metric, guardrails, and human owners across the pack. Resolve inconsistencies or record OWNER TO VERIFY with an owner and next check.
```

## Test It

The runbook must contain campaign, ad-set, and ad decisions; two evidence-led audience roles; a retargeting data map; one-variable creative test; explicit eligibility, magnitude, approval, cooldown, and rollback rules; and eight scenario decisions. Only SC01 may be eligible to PROPOSE, and even that row must require human approval. No row may indicate that a live change was made. The manifest must list every expected 01-to-08 file with presence, version or date, status, provenance, owner, and unresolved OWNER TO VERIFY items; the cross-artifact checks must show no unexplained contradiction.

## Checkpoint for the Next Lab

This is the final lab. Keep all eight numbered artifacts, the 08 course-pack manifest, and the decision logs together as the Harbour & Hearth Instagram operations pack. Any unresolved item must remain OWNER TO VERIFY with a named owner and next check before a workplace pilot.

## Troubleshooting

- **The agent recommends budget first:** Force the order: validate data, check guardrails, locate the funnel break, then choose one lever.
- **Retargeting is described only as 'people who engaged':** Add source, rights, eligibility, retention, exclusions, frequency, suppression, and owner.
- **Several settings change in one recommendation:** Return to the one-lever rule and turn other ideas into later hypotheses, not simultaneous actions.

## Challenge

Add promotion criteria for moving from recommendation-only to one low-risk reversible automated action, including correction rate, incident-free runs, owner coverage, and automatic rollback evidence.

## Reflection

Why can a performance-improving recommendation still be the wrong business decision, and which guardrail in your policy catches that case?

---

[← Lab 7](lab-07-build-the-instagram-insights-dashboard-and-evidence-linked-report.md) · [Labs index →](README.md)
