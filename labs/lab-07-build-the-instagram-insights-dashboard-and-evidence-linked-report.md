# Lab 7 — Build the Instagram Insights Dashboard and Evidence-Linked Report

- **Course:** Agentic AI for Instagram Marketing (C695)
- **Version:** v1.0 (3 August 2026)
- **Topic 4:** Analytics, Ads and Optimisation with AI Agents
- **Maps to:** LO5: Calculate and interpret Instagram organic and paid metrics, then produce a source-linked dashboard, diagnosis, and bounded next action
- **Tools:** Spreadsheet application, approved generative AI assistant, text editor, labs/resources/07-insights-dashboard-layout.md, labs/resources/harbour-hearth-instagram-performance.csv, C695-campaign-pack/02-agent-prompt-contract.md

**Duration:** 45 minutes

---

## What You Will Do

You validate a synthetic Instagram performance export, calculate clearly defined organic and paid metrics, and build a compact decision dashboard. The report separates observation from hypothesis, cites source rows and date scope, protects guardrails, and recommends one controlled learning action.

## What You Will Build

C695-campaign-pack/07-insights-dashboard.xlsx plus optional 07-insights-dashboard-flat.csv and 07-performance-report.md containing validated calculations, format comparisons, funnel diagnosis, source-linked findings, caveats, and one bounded recommendation.

## Prerequisites

- Completed Labs 1 to 6 and keep the primary outcome, guardrails, and approval rules available.
- Open the synthetic performance CSV in a spreadsheet without changing the source file.
- Use the metric definitions in this lab; do not substitute a denominator silently.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Use the supplied layout guide to create 07-insights-dashboard.xlsx with tabs named Raw, Calculations, and Dashboard. Import the source CSV into Raw without altering it. A flat CSV export is optional and never replaces the workbook.**

```text
Layout: labs/resources/07-insights-dashboard-layout.md
Source: labs/resources/harbour-hearth-instagram-performance.csv
Primary output: C695-campaign-pack/07-insights-dashboard.xlsx
Optional export: C695-campaign-pack/07-insights-dashboard-flat.csv
```

**2. Validate the extract before calculating. Confirm unique content_id, ISO dates, allowed formats, numeric non-negative counts, reach not greater than views, paid rows with spend, no blank required fields, and one stated reporting window.**

```text
Record exceptions as DATA ISSUE and stop any calculation that depends on the affected row.
```

**3. Add calculated columns with the exact definitions below. Return NA when the denominator is zero.**

```text
Interactions = likes + comments + saves + shares
Interaction rate by reach (%) = interactions / reach × 100
Save rate by reach (%) = saves / reach × 100
Share rate by reach (%) = shares / reach × 100
Profile-visit rate by reach (%) = profile_visits / reach × 100
Link-click rate by reach (%) = link_clicks / reach × 100
Purchase rate by link click (%) = purchases / link_clicks × 100
CPA (paid row) = spend_sgd / purchases
ROAS (paid row) = revenue_sgd / spend_sgd
Blended paid CPA = total spend_sgd for Paid rows / total purchases for Paid rows
Blended paid ROAS = total revenue_sgd for Paid rows / total spend_sgd for Paid rows
```

**4. Create KPI cards for total views, total reach, total interactions, total saves, total shares, total link clicks, total purchases, total paid spend, total attributed revenue, blended paid CPA, blended paid ROAS, and total negative feedback.**

```text
Show the formula or source range beside every KPI card. Blended paid CPA and blended paid ROAS must use the totals-based definitions above, not the average of row-level CPA or ROAS. Do not add reach across rows and describe it as unique account-level reach; label it summed content-level reach.
```

**5. Build a format comparison table for Image, Carousel, Reel, and Stories using mean interaction rate by reach, mean save rate, mean share rate, total link clicks, and total purchases. Keep organic and paid scope visible.**

```text
A higher engagement rate does not prove a higher purchase contribution; report both layers.
```

**6. Create 07-performance-report.md with headings for Data Scope, Metric Definitions, Observations, Driver Hypotheses, Guardrails, Recommendation, and Caveats.**

```text
File: C695-campaign-pack/07-performance-report.md
```

**7. Ask the AI to write an evidence-linked report from the completed dashboard table, not from the raw CSV alone.**

```text
Using the G-C-A-T-E contract and the completed synthetic dashboard, write a concise Instagram performance report.

For each observation include: exact metric, value, date window, comparison, content IDs or source rows, and organic/paid scope.
For each hypothesis include: evidence that supports it, evidence still needed, and an alternative explanation.
End with exactly one bounded next action, one primary decision metric, two guardrails, an owner, an observation window, and a rollback condition.

Do not call correlation causation. Do not add follower demographics, attribution claims, or platform explanations that are absent from the data. Use UNKNOWN when the extract cannot answer the question.
```

**8. Review every narrative statement against the dashboard. Label it OBSERVATION, HYPOTHESIS, or UNKNOWN; remove any claim with no content ID, metric, or source row.**

```text
Required caveats: synthetic data, content-level reach is not deduplicated, paid and organic effects differ, attribution is not independently verified, and results do not establish causation.
```

**9. Add an exception panel for tracking issue, unusually high negative feedback, low result volume, capacity risk, missing rights status, and unavailable owner. Each exception must state HOLD or STOP and the responsible owner.**

```text
No dashboard colour alone may trigger a public, targeting, or spend action.
```

**10. Add a Verification Log on the Dashboard tab and retain the manual checks used in Test It.**

```text
Columns: Check ID | Source row or range | Formula tested | Expected value | Observed value | PASS / REVISE | Reviewer | Date.
```

## Test It

Recalculate three rows manually and confirm the spreadsheet matches to two decimal places. The report must cite at least three content IDs, distinguish observation from hypothesis, include all required caveats, and recommend exactly one reversible action with metric, guardrails, owner, window, and rollback. The workbook must contain Raw, Calculations, and Dashboard tabs; its blended paid CPA and blended paid ROAS must equal totals-based paid calculations; and the Verification Log must retain expected and observed values, source range, reviewer, date, and result. Any divide-by-zero result must display NA rather than an error or invented zero.

## Checkpoint for the Next Lab

Keep the dashboard, metric definitions, diagnosis, guardrails, and one-action recommendation. Lab 8 uses them to design an ads, retargeting, and optimisation loop without activating spend.

## Troubleshooting

- **Reach totals are treated as unique people:** Label them summed content-level reach because the export does not deduplicate people across content rows.
- **The AI selects a winner from engagement alone:** Require outcome, paid scope, guardrails, and attribution caveats before a recommendation.
- **Spreadsheet errors appear on organic rows:** Use NA when spend or another denominator is zero and keep organic and paid calculations separate.

## Challenge

Add a simple two-chart dashboard: interaction rate by content ID and purchases by content ID, each with direct labels and a note distinguishing organic and paid rows.

## Reflection

Which dashboard number is easiest to misinterpret, and what definition or caveat prevents the wrong decision?

---

[← Lab 6](lab-06-create-the-ugc-review-privacy-and-escalation-runbook.md) · [Lab 8 →](lab-08-design-and-simulate-the-instagram-ads-retargeting-and-optimisation-loop.md)
