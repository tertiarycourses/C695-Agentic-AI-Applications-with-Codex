"""Topic 4 — Analytics, Ads and Optimisation with AI Agents."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Build the Instagram Insights Dashboard and Evidence-Linked Report",
        objective="LO5: Calculate and interpret Instagram organic and paid metrics, then produce a source-linked dashboard, diagnosis, and bounded next action",
        duration="45 minutes",
        desc=(
            "You validate a synthetic Instagram performance export, calculate clearly defined organic and paid metrics, and build a compact decision dashboard. "
            "The report separates observation from hypothesis, cites source rows and date scope, protects guardrails, and recommends one controlled learning action."
        ),
        build="C695-campaign-pack/07-insights-dashboard.xlsx plus optional 07-insights-dashboard-flat.csv and 07-performance-report.md containing validated calculations, format comparisons, funnel diagnosis, source-linked findings, caveats, and one bounded recommendation.",
        services="Spreadsheet application, approved generative AI assistant, text editor, labs/resources/07-insights-dashboard-layout.md, labs/resources/harbour-hearth-instagram-performance.csv, C695-campaign-pack/02-agent-prompt-contract.md",
        prerequisites=[
            "Completed Labs 1 to 6 and keep the primary outcome, guardrails, and approval rules available.",
            "Open the synthetic performance CSV in a spreadsheet without changing the source file.",
            "Use the metric definitions in this lab; do not substitute a denominator silently.",
        ],
        deck_steps=[
            "Validate schema, dates, identifiers, missing values, duplicates, and organic/paid scope.",
            "Calculate interactions, reach-based rates, CPA, and ROAS with explicit formulas.",
            "Compare content formats and locate the weakest customer-journey transition.",
            "Write source-linked findings, hypotheses, caveats, and one bounded next action.",
        ],
        steps=[
            (
                "Use the supplied layout guide to create 07-insights-dashboard.xlsx with tabs named Raw, Calculations, and Dashboard. Import the source CSV into Raw without altering it. A flat CSV export is optional and never replaces the workbook.",
                "Layout: labs/resources/07-insights-dashboard-layout.md\nSource: labs/resources/harbour-hearth-instagram-performance.csv\nPrimary output: C695-campaign-pack/07-insights-dashboard.xlsx\nOptional export: C695-campaign-pack/07-insights-dashboard-flat.csv",
            ),
            (
                "Validate the extract before calculating. Confirm unique content_id, ISO dates, allowed formats, numeric non-negative counts, reach not greater than views, paid rows with spend, no blank required fields, and one stated reporting window.",
                "Record exceptions as DATA ISSUE and stop any calculation that depends on the affected row.",
            ),
            (
                "Add calculated columns with the exact definitions below. Return NA when the denominator is zero.",
                "Interactions = likes + comments + saves + shares\nInteraction rate by reach (%) = interactions / reach × 100\nSave rate by reach (%) = saves / reach × 100\nShare rate by reach (%) = shares / reach × 100\nProfile-visit rate by reach (%) = profile_visits / reach × 100\nLink-click rate by reach (%) = link_clicks / reach × 100\nPurchase rate by link click (%) = purchases / link_clicks × 100\nCPA (paid row) = spend_sgd / purchases\nROAS (paid row) = revenue_sgd / spend_sgd\nBlended paid CPA = total spend_sgd for Paid rows / total purchases for Paid rows\nBlended paid ROAS = total revenue_sgd for Paid rows / total spend_sgd for Paid rows",
            ),
            (
                "Create KPI cards for total views, total reach, total interactions, total saves, total shares, total link clicks, total purchases, total paid spend, total attributed revenue, blended paid CPA, blended paid ROAS, and total negative feedback.",
                "Show the formula or source range beside every KPI card. Blended paid CPA and blended paid ROAS must use the totals-based definitions above, not the average of row-level CPA or ROAS. Do not add reach across rows and describe it as unique account-level reach; label it summed content-level reach.",
            ),
            (
                "Build a format comparison table for Image, Carousel, Reel, and Stories using mean interaction rate by reach, mean save rate, mean share rate, total link clicks, and total purchases. Keep organic and paid scope visible.",
                "A higher engagement rate does not prove a higher purchase contribution; report both layers.",
            ),
            (
                "Create 07-performance-report.md with headings for Data Scope, Metric Definitions, Observations, Driver Hypotheses, Guardrails, Recommendation, and Caveats.",
                "File: C695-campaign-pack/07-performance-report.md",
            ),
            (
                "Ask the AI to write an evidence-linked report from the completed dashboard table, not from the raw CSV alone.",
                """Using the G-C-A-T-E contract and the completed synthetic dashboard, write a concise Instagram performance report.

For each observation include: exact metric, value, date window, comparison, content IDs or source rows, and organic/paid scope.
For each hypothesis include: evidence that supports it, evidence still needed, and an alternative explanation.
End with exactly one bounded next action, one primary decision metric, two guardrails, an owner, an observation window, and a rollback condition.

Do not call correlation causation. Do not add follower demographics, attribution claims, or platform explanations that are absent from the data. Use UNKNOWN when the extract cannot answer the question.""",
            ),
            (
                "Review every narrative statement against the dashboard. Label it OBSERVATION, HYPOTHESIS, or UNKNOWN; remove any claim with no content ID, metric, or source row.",
                "Required caveats: synthetic data, content-level reach is not deduplicated, paid and organic effects differ, attribution is not independently verified, and results do not establish causation.",
            ),
            (
                "Add an exception panel for tracking issue, unusually high negative feedback, low result volume, capacity risk, missing rights status, and unavailable owner. Each exception must state HOLD or STOP and the responsible owner.",
                "No dashboard colour alone may trigger a public, targeting, or spend action.",
            ),
            (
                "Add a Verification Log on the Dashboard tab and retain the manual checks used in Test It.",
                "Columns: Check ID | Source row or range | Formula tested | Expected value | Observed value | PASS / REVISE | Reviewer | Date.",
            ),
        ],
        test=(
            "Recalculate three rows manually and confirm the spreadsheet matches to two decimal places. The report must cite at least three content IDs, distinguish observation from hypothesis, include all required caveats, and recommend exactly one reversible action with metric, guardrails, owner, window, and rollback. "
            "The workbook must contain Raw, Calculations, and Dashboard tabs; its blended paid CPA and blended paid ROAS must equal totals-based paid calculations; and the Verification Log must retain expected and observed values, source range, reviewer, date, and result. Any divide-by-zero result must display NA rather than an error or invented zero."
        ),
        checkpoint="Keep the dashboard, metric definitions, diagnosis, guardrails, and one-action recommendation. Lab 8 uses them to design an ads, retargeting, and optimisation loop without activating spend.",
        troubleshooting=[
            ("Reach totals are treated as unique people", "Label them summed content-level reach because the export does not deduplicate people across content rows."),
            ("The AI selects a winner from engagement alone", "Require outcome, paid scope, guardrails, and attribution caveats before a recommendation."),
            ("Spreadsheet errors appear on organic rows", "Use NA when spend or another denominator is zero and keep organic and paid calculations separate."),
        ],
        challenge="Add a simple two-chart dashboard: interaction rate by content ID and purchases by content ID, each with direct labels and a note distinguishing organic and paid rows.",
        reflection="Which dashboard number is easiest to misinterpret, and what definition or caveat prevents the wrong decision?",
    ),
    dict(
        num=8,
        topic=4,
        title="Design and Simulate the Instagram Ads, Retargeting and Optimisation Loop",
        objective="LO6: Design a human-governed Instagram ads and retargeting loop for audience, budget, and creative decisions using evidence, limits, approval, cooldown, and rollback",
        duration="55 minutes",
        desc=(
            "You complete the connected course pack with an AI-assisted Instagram ads blueprint and a bounded continuous-improvement policy. "
            "You then run eight synthetic scenarios through the policy to prove that strong numbers cannot override tracking, customer, rights, capacity, cooldown, or human-approval guardrails."
        ),
        build="C695-campaign-pack/08-ads-retargeting-optimisation-runbook.md plus 08-decision-log.csv and 08-course-pack-manifest.md containing the campaign hierarchy, audience roles, budget and creative hypotheses, retargeting data map, bounded policy, scenario decisions, rollback plan, and a validated inventory of artifacts 01 to 08.",
        services="Approved generative AI assistant, spreadsheet application, text editor, labs/resources/08-ads-runbook-starter.md, labs/resources/08-decision-log-starter.txt, labs/resources/harbour-hearth-optimisation-scenarios.csv, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/07-insights-dashboard.xlsx, C695-campaign-pack/07-performance-report.md",
        prerequisites=[
            "Completed Labs 1 to 7 with all numbered artifacts in C695-campaign-pack; use the Rejoin Path in the labs index to reconstruct any missing checkpoint first.",
            "Open the final 02-agent-prompt-contract.md and apply it to every AI-assisted campaign and optimisation decision.",
            "Use hypothetical budget values only; do not open or change a live advertising account.",
            "Keep account IDs, payment details, event verification, audience eligibility, and live settings as OWNER TO VERIFY.",
        ],
        deck_steps=[
            "Align business goal, objective, event, audience role, budget, creative, destination, and metric.",
            "Map prospecting and retargeting signals with rights, retention, exclusions, and suppression.",
            "Define minimum evidence, allowed action, magnitude, cooldown, approval, and rollback.",
            "Simulate eight scenarios and prove guardrails can force HOLD or STOP.",
        ],
        steps=[
            (
                "Copy the supplied starter to 08-ads-retargeting-optimisation-runbook.md and complete its sections for Campaign Blueprint, Audience and Retargeting Map, Creative Test, Budget Policy, Decision Rules, Simulation, and Rollback.",
                "Source: labs/resources/08-ads-runbook-starter.md\nOutput: C695-campaign-pack/08-ads-retargeting-optimisation-runbook.md",
            ),
            (
                "Draft the campaign hierarchy from the approved pre-order goal: campaign objective and business reason; ad-set conversion location, event, audience role, location constraint, exclusions, placements, hypothetical budget, and schedule; ad identity, format, creative ID, text, destination, and tracking checks.",
                "Use OWNER TO VERIFY for the current Meta objective options, verified event, account identity, payment method, platform eligibility, and live placement settings.",
            ),
            (
                "Create two audience roles: one prospecting hypothesis and one retargeting hypothesis. For each state the customer state, authorised evidence, message job, exclusions, decision metric, privacy risk, and owner.",
                "Do not invent demographic or sensitive traits. Audience suggestions are hypotheses; strict location, age, language, or exclusion controls require a genuine business or safety reason.",
            ),
            (
                "Build the retargeting data map. Include source signal, collection purpose, notice or consent/basis, platform eligibility, retention, access, minimum audience concerns, exclusion after purchase, frequency control, deletion or suppression path, and owner.",
                "Potential sources: eligible content engagement, website event, video view, approved lead, or authorised customer list. Availability and eligibility remain OWNER TO VERIFY.",
            ),
            (
                "Define one controlled creative test based on Lab 7. Change exactly one variable, such as hook angle, while holding audience, offer, format, destination, budget, schedule, and optimisation stable.",
                "Record hypothesis, control, treatment, primary metric, two guardrails, minimum window, minimum result count, practical threshold, stop rule, and decision owner.",
            ),
            (
                "Write the bounded optimisation policy below. The agent recommends only; a named Marketing Owner approves every change.",
                """ELIGIBILITY: at least 7 complete days, at least 20 purchases, clean tracking, no privacy concern, no unsupported claim, complaint rate at or below 2.0%, enough fulfilment capacity, at least 72 hours since the last material change, and approver available.
ALLOWED RECOMMENDATION: HOLD, STOP, draft one creative variant, or propose one budget change.
MAGNITUDE: at most 10% budget increase or decrease in one cycle.
ONE-LEVER RULE: do not change audience, budget, creative, placement, and destination together.
APPROVAL: named Marketing Owner must approve before any external change.
COOLDOWN: observe at least 72 hours after a material change.
ROLLBACK: restore the recorded prior configuration if tracking, complaint, capacity, rights, or performance guardrails fail.
LOG: source window, before value, recommendation, reason, owner, approval, timestamp, expected effect, result, and rollback status.""",
            ),
            (
                "Copy the supplied eight-row decision-log starter to 08-decision-log.csv and keep the exact header.",
                "Source: labs/resources/08-decision-log-starter.txt\nOutput header: scenario_id,decision,blocking_guardrail,evidence,proposed_lever,magnitude,approver,cooldown_or_next_check,rollback,status_reason",
            ),
            (
                "Ask the AI to apply the saved G-C-A-T-E contract and the policy to each scenario independently. It must test guardrails before performance and may not combine scenarios.",
                """Apply the complete G-C-A-T-E contract in C695-campaign-pack/02-agent-prompt-contract.md. For each synthetic scenario return: scenario_id | ELIGIBLE yes/no | decision HOLD/STOP/PROPOSE | blocking guardrail | evidence fields | at most one proposed lever | magnitude | approval needed | next check | rollback | reason.

Apply the written policy exactly. A high ROAS cannot override a tracking error, complaint breach, capacity shortfall, low event volume, cooldown, missing approver, privacy concern, or unsupported claim. Never activate an ad or change a live setting.""",
            ),
            (
                "Review the eight decisions. SC01 may propose one change up to 10% because it meets the synthetic eligibility rules. SC02-SC08 must HOLD or STOP for their stated tracking, complaint, capacity, volume, cooldown, approver, or claim guardrail.",
                "If any blocked scenario receives PROPOSE, strengthen the guardrail-first order and rerun all scenarios.",
            ),
            (
                "Add the continuous feedback loop and rollback checklist: observe fixed window, validate, diagnose, propose one lever, approve, record before state, apply placeholder, observe cooldown, compare, retain or rollback, and update the learning log.",
                "Public action, audience creation, ad activation, and spend remain disabled in this lab.",
            ),
            (
                "Create 08-course-pack-manifest.md and inventory every expected artifact from 01 through 08. Validate cross-artifact consistency before closing the lab.",
                "Manifest columns: Artifact | Present | Version or date | Final status | Source or provenance | Owner | Unresolved OWNER TO VERIFY. Cross-check the same customer action, approved offer facts, content IDs, account placeholder, time zone, status vocabulary, rights state, primary metric, guardrails, and human owners across the pack. Resolve inconsistencies or record OWNER TO VERIFY with an owner and next check.",
            ),
        ],
        test=(
            "The runbook must contain campaign, ad-set, and ad decisions; two evidence-led audience roles; a retargeting data map; one-variable creative test; explicit eligibility, magnitude, approval, cooldown, and rollback rules; and eight scenario decisions. "
            "Only SC01 may be eligible to PROPOSE, and even that row must require human approval. No row may indicate that a live change was made. The manifest must list every expected 01-to-08 file with presence, version or date, status, provenance, owner, and unresolved OWNER TO VERIFY items; the cross-artifact checks must show no unexplained contradiction."
        ),
        checkpoint="This is the final lab. Keep all eight numbered artifacts, the 08 course-pack manifest, and the decision logs together as the Harbour & Hearth Instagram operations pack. Any unresolved item must remain OWNER TO VERIFY with a named owner and next check before a workplace pilot.",
        troubleshooting=[
            ("The agent recommends budget first", "Force the order: validate data, check guardrails, locate the funnel break, then choose one lever."),
            ("Retargeting is described only as 'people who engaged'", "Add source, rights, eligibility, retention, exclusions, frequency, suppression, and owner."),
            ("Several settings change in one recommendation", "Return to the one-lever rule and turn other ideas into later hypotheses, not simultaneous actions."),
        ],
        challenge="Add promotion criteria for moving from recommendation-only to one low-risk reversible automated action, including correction rate, incident-free runs, owner coverage, and automatic rollback evidence.",
        reflection="Why can a performance-improving recommendation still be the wrong business decision, and which guardrail in your policy catches that case?",
    ),
]
