# Agentic AI for Instagram Marketing (C695) — Learner Guide

**Course Code:** C695  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 3 August 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Foundations of Agentic AI for Instagram Marketing](#topic-01--foundations-of-agentic-ai-for-instagram-marketing)
  - [Instagram Marketing as a Connected System](#instagram-marketing-as-a-connected-system)
  - [From Generative AI to an Agentic Workflow](#from-generative-ai-to-an-agentic-workflow)
  - [The Six-Part Marketing Agent](#the-six-part-marketing-agent)
  - [Choose Tools by Role, Permission, and Risk](#choose-tools-by-role-permission-and-risk)
  - [Professional Account and Automation Readiness](#professional-account-and-automation-readiness)
  - [Objective, Customer Action, and KPI Chain](#objective-customer-action-and-kpi-chain)
  - [Audience Evidence Before Targeting](#audience-evidence-before-targeting)
  - [The Prompt Contract](#the-prompt-contract)
  - [Lab 1 — Map the Instagram Customer Journey and Account Readiness](#lab-1--map-the-instagram-customer-journey-and-account-readiness)
  - [Lab 2 — Write and Test the Instagram Agent Prompt Contract](#lab-2--write-and-test-the-instagram-agent-prompt-contract)
  - [Recap — Foundations of Agentic AI for Instagram Marketing](#recap--foundations-of-agentic-ai-for-instagram-marketing)
- [Topic 02 — AI-Powered Content Creation and Scheduling](#topic-02--ai-powered-content-creation-and-scheduling)
  - [The Instagram Message Hierarchy](#the-instagram-message-hierarchy)
  - [Content Pillars and the Customer Journey](#content-pillars-and-the-customer-journey)
  - [Brand Voice as Observable Rules](#brand-voice-as-observable-rules)
  - [Caption and Hashtag System](#caption-and-hashtag-system)
  - [Creative System: Image, Carousel, Stories, and Reels](#creative-system-image-carousel-stories-and-reels)
  - [Content Calendar Agent and Publishing Control](#content-calendar-agent-and-publishing-control)
  - [Content Quality Gate](#content-quality-gate)
  - [Lab 3 — Create the Instagram Content and Creative Kit](#lab-3--create-the-instagram-content-and-creative-kit)
  - [Lab 4 — Build the Content Calendar Agent and Publishing Workflow](#lab-4--build-the-content-calendar-agent-and-publishing-workflow)
  - [Recap — AI-Powered Content Creation and Scheduling](#recap--ai-powered-content-creation-and-scheduling)
- [Topic 03 — Automating Engagement and Community Management](#topic-03--automating-engagement-and-community-management)
  - [Engagement Is a Service Workflow](#engagement-is-a-service-workflow)
  - [Intent and Risk Routing](#intent-and-risk-routing)
  - [Lead Capture and Follow-Up Automation](#lead-capture-and-follow-up-automation)
  - [Personalised Responses and Escalation Rules](#personalised-responses-and-escalation-rules)
  - [Reviews and User-Generated Content](#reviews-and-user-generated-content)
  - [Privacy, Copyright, and Responsible AI Gate](#privacy-copyright-and-responsible-ai-gate)
  - [Lab 5 — Build the Comment and Direct-Message Response Router](#lab-5--build-the-comment-and-direct-message-response-router)
  - [Lab 6 — Create the UGC, Review, Privacy and Escalation Runbook](#lab-6--create-the-ugc-review-privacy-and-escalation-runbook)
  - [Recap — Automating Engagement and Community Management](#recap--automating-engagement-and-community-management)
- [Topic 04 — Analytics, Ads and Optimisation with AI Agents](#topic-04--analytics-ads-and-optimisation-with-ai-agents)
  - [Instagram Insights and the Metric Tree](#instagram-insights-and-the-metric-tree)
  - [Automated Reports and Decision Dashboards](#automated-reports-and-decision-dashboards)
  - [AI-Assisted Instagram Ads Campaigns](#ai-assisted-instagram-ads-campaigns)
  - [Audience, Budget, and Creative Optimisation](#audience-budget-and-creative-optimisation)
  - [Retargeting by Customer State](#retargeting-by-customer-state)
  - [Continuous Improvement with a Governed Feedback Loop](#continuous-improvement-with-a-governed-feedback-loop)
  - [Lab 7 — Build the Instagram Insights Dashboard and Evidence-Linked Report](#lab-7--build-the-instagram-insights-dashboard-and-evidence-linked-report)
  - [Lab 8 — Design and Simulate the Instagram Ads, Retargeting and Optimisation Loop](#lab-8--design-and-simulate-the-instagram-ads-retargeting-and-optimisation-loop)
  - [Recap — Analytics, Ads and Optimisation with AI Agents](#recap--analytics-ads-and-optimisation-with-ai-agents)
- [Wrap-Up — From Course Pack to Operating Practice](#wrap-up--from-course-pack-to-operating-practice)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide is the self-contained study text for Agentic AI for Instagram Marketing (C695). It explains the concepts behind agent design, Instagram content and scheduling, community automation, analytics, advertising, and governed optimisation before guiding you through eight connected labs.

The course uses the synthetic Harbour & Hearth bakery scenario so every learner can work with the same evidence without exposing customer data or spending live advertising budget. Save each lab output in one Instagram operations folder; the final lab combines the complete set into a review-ready, human-governed operating pack.


## Course Learning Outcomes

- LO1: Explain AI agents and map an Instagram customer journey, account readiness, tools, prompts, evidence, and human approval gates.
- LO2: Generate an on-brand Instagram content system with captions, hashtags, image and Reels briefs, a calendar, and a controlled publishing workflow.
- LO3: Design a governed engagement workflow for comments, direct messages, lead capture, follow-up, reviews, and user-generated content.
- LO4: Apply privacy, copyright, platform, brand, and escalation rules to Instagram content and community-management decisions.
- LO5: Calculate and interpret Instagram organic and paid metrics, then produce an evidence-linked performance report and dashboard.
- LO6: Design an AI-assisted Instagram ads and retargeting optimisation loop for audience, budget, and creative decisions with human authority.


## Before You Start — Preparation

**What you need**

- A Windows or Mac laptop with a modern web browser and spreadsheet application.
- Access to an approved generative AI assistant such as ChatGPT, Microsoft Copilot, Claude, or Google Gemini.
- The course repository downloaded locally, including labs/resources/.
- Optional access to an Instagram Professional account, Meta Business Suite, or an n8n practice workspace for view-only exploration; no live posting, messaging, or ad spend is required.
- A new local folder named C695-campaign-pack for the eight lab artifacts.

**Verify your setup**

Open the brand brief and performance dataset, create the campaign-pack folder, and confirm your AI assistant can return a Markdown table without using confidential information.

```bash
Open labs/resources/harbour-hearth-brand-brief.md
Open labs/resources/harbour-hearth-instagram-performance.csv
Create folder: C695-campaign-pack
```

**Conventions used in every lab**

- Replace placeholders such as <PASTE BRIEF> with the specified synthetic course material.
- Never paste real customer identifiers, account secrets, unpublished results, or confidential creative into an unapproved AI tool.
- AI output is a proposal. Check facts, calculations, brand voice, rights, audience fairness, and the intended customer action.
- Work in draft mode. Do not publish a post, enable an automation, or activate an ad unless your organisation separately authorises it.
- Keep filenames exactly as shown so every later lab can find the earlier checkpoint.


## Topic 01 — Foundations of Agentic AI for Instagram Marketing

agents and workflows | tool choices | Professional account readiness | prompting | customer journey

**Key concepts**

- Outcome before output: Start with a business result and customer action, not a request to 'make posts'.
- Organic and paid roles: Organic content builds attention and proof; paid delivery buys controlled reach and learning.
- Agentic loop: An agent plans, uses tools, checks evidence, and iterates until a stop condition is reached.
- Evidence boundary: Facts, customer data, and performance numbers need provenance; unknowns remain labelled assumptions.
- Prompt contract: Role, goal, context, inputs, rules, output schema, and review criteria make work repeatable.
- Audience hypothesis: A segment is a testable need and behaviour pattern, not a stereotype or invented demographic.
- Human authority: Publishing, spend, targeting changes, and sensitive replies remain approval-controlled actions.
- Audit trail: Save the brief, inputs, versions, approvals, and final decision so the workflow can be reviewed.


### Instagram Marketing as a Connected System

Instagram marketing is a system, not a sequence of unrelated posts. A useful plan begins with a business objective, identifies the customer action that would demonstrate progress, then chooses content and delivery methods that make that action more likely. Organic posts, Reels, Stories, profile information, community conversations, and paid ads should therefore share one message hierarchy and one measurement plan.

The same content can perform different jobs at different stages. A how-to video may build awareness, a customer proof post may reduce uncertainty, and a limited offer may invite a conversion. An AI agent can help coordinate these jobs, but it cannot decide what success means for the business. The marketer supplies the objective, evidence, constraints, and final judgement.

**Visual framework**

- Business objective
- Audience need
- Useful content
- Organic or paid delivery
- Measured customer action


### From Generative AI to an Agentic Workflow

Generative AI creates text, images, or analysis from a prompt. An agentic workflow goes further: it manages a multi-step goal, selects or calls tools, observes results, and decides what to do next within defined limits. A content assistant that drafts one caption is useful, but it becomes agentic only when it can work through a plan such as research, draft, check, revise, route for approval, and record the outcome.

Not every task needs autonomy. Deterministic work such as applying a known naming convention is usually safer as a checklist or rule. Agentic reasoning is more valuable when inputs are unstructured, trade-offs are contextual, or the path changes after new evidence. Begin with the smallest useful loop and add tools only when each tool has a clear purpose and risk level.

**Visual framework**

Single AI task: One prompt produces one draft | The user manually supplies every input | No persistent state or explicit stop rule | Quality depends on one response

Agentic workflow: A goal is decomposed into multiple steps | Tools retrieve data or create controlled outputs | State, checks, retries, and stop conditions are explicit | A person approves high-impact actions


### The Six-Part Marketing Agent

A reliable marketing agent needs more than a clever prompt. Its goal defines the finish line. Context explains the brand and audience. Instructions describe the route and exceptions. Tools determine what the agent may read or change. Memory preserves only the state needed for the next decision. Checks test whether the result is safe and useful before the workflow proceeds.

A weakness in any one part propagates. If the goal says 'increase engagement' but does not name the customer action or time window, the agent may optimise reactions that have no business value. If the tools include a publishing action without an approval gate, a drafting error becomes a public error. Design the system before choosing the model.

**Visual framework**

- Goal — The result, customer action, time horizon, and success threshold.
- Context — Brand, offer, audience evidence, channel role, and constraints.
- Instructions — Decision rules, required steps, output format, and escalation logic.
- Tools — Approved data sources, content tools, calendars, and reporting surfaces.
- Memory — Briefs, past variants, decisions, and lessons that should persist.
- Checks — Brand, factual, privacy, policy, and performance validation before action.


### Choose Tools by Role, Permission, and Risk

A tool belongs in the workflow only when its role is clear. AI assistants interpret and draft; spreadsheets store structured state; Meta surfaces expose account operations; workflow automation coordinates steps. The Instagram API can enable production integrations, but it needs a Professional account, an app, permissions, tokens, and current platform review. These are operational requirements, not details to improvise inside a prompt.

Rate each tool action by impact and reversibility. Reading a synthetic brief is low risk. Drafting a caption is medium risk because it still needs review. Publishing, replying publicly, handling personal data, changing an audience, or changing spend is high risk. High-risk actions require the named account owner and a recorded approval.

**Visual framework**

- ChatGPT or Claude — Develop briefs, structured drafts, critique, classification, and analysis from approved inputs.
- Image tools — Explore visual concepts and storyboards; retain provenance and verify product truth.
- Meta Business Suite — Review profiles, drafts, Planner, Inbox, and insights with account-based permissions.
- n8n — Connect triggers, data, AI steps, review gates, logs, retries, and bounded actions.
- Spreadsheets — Hold calendars, response queues, metric definitions, and decision logs in a reviewable form.
- Instagram API — Supports approved professional-account publishing, insights, comments, and messaging use cases subject to permissions and limits.


### Professional Account and Automation Readiness

Instagram Professional accounts are Business or Creator accounts. Professional tools include the dashboard and insights, while some automation paths depend on how the account, Meta assets, app, and permissions are configured. Connecting a Facebook Page can support cross-app management in Meta Business Suite, but current requirements vary by feature and login method, so the owner should verify the official setup for the intended integration.

Readiness means more than being able to log in. Confirm the account identity, owner, recovery method, authorised roles, connected assets, time zone, data sources, allowed actions, and revoke path. Test with a draft or read-only action first. Never place an access token in a prompt, screenshot, lab file, or public repository.

**Visual framework**

- Professional account
- Correct business identity
- Linked assets and roles
- Approved permissions
- Draft-mode connection test


### Objective, Customer Action, and KPI Chain

A measurement chain prevents vanity metrics from becoming the strategy. The business result might be breakfast-box revenue. The marketing objective could be qualified pre-orders. The customer action is a completed order. The primary KPI may be cost per purchase or return on ad spend, while a guardrail could be refund rate, negative feedback, or response quality.

Choose the Meta campaign objective that most closely matches the larger business goal and the event that can be measured reliably. An awareness objective is not a cheaper substitute for a sales objective when sales are the real decision criterion. Equally, a sales objective is weak when the business has no trustworthy conversion signal. The objective, data signal, and KPI must agree.

**Visual framework**

- Business result
- Marketing objective
- Customer action
- Primary KPI
- Guardrail metric


### Audience Evidence Before Targeting

Audience research should separate what is known from what is inferred. Observed data may show that weekday pre-orders peak before 9 am. Customer interviews may reveal that convenience matters more than variety. An AI model can propose segment hypotheses, but it must label them as hypotheses and cite the supplied evidence instead of manufacturing demographic detail.

Meta's delivery systems can work with broad audiences, audience suggestions, and strict controls such as location, minimum age, language, and exclusions. The marketer's job is to provide a commercially meaningful signal without narrowing the audience through stereotypes. Any customer list requires the organisation to have the necessary rights, permissions, and lawful basis for its use.

**Visual framework**

- Observed — Existing customer questions, purchases, site behaviour, and Instagram interactions.
- Declared — Needs and preferences people voluntarily shared through interviews or forms.
- Inferred — A labelled hypothesis derived from patterns, never presented as fact.
- Excluded — Sensitive traits, unjustified personal data, and segments the offer should not reach.
- Testable — A need, trigger, barrier, message angle, and measurable response.
- Revisable — A segment changes when evidence contradicts the original hypothesis.


### The Prompt Contract

A prompt contract turns an informal request into an operating instruction. It tells the agent who it is helping, what outcome matters, which inputs are authoritative, which choices are allowed, and exactly what form the result must take. A structured output such as a table with evidence, assumptions, risks, and next action is easier to review than a persuasive paragraph.

Include failure behaviour. The agent should say 'insufficient evidence' when a required input is missing, request clarification when two constraints conflict, and stop when the next action would publish, spend money, change targeting, or expose personal data. These rules reduce silent guessing and make human review faster.

**Visual framework**

- Role and goal
- Grounded inputs
- Decision rules
- Output schema
- Review and escalation


### Lab 1 — Map the Instagram Customer Journey and Account Readiness

Learning outcome: LO1: Explain AI agents and map the customer journey, account readiness, tools, evidence, and approval gates for an Instagram workflow.

Goal: You begin the connected Harbour & Hearth scenario by turning an approved synthetic brand brief and audience signals into a measurable Instagram customer journey. You then complete a Professional-account readiness and tool-permission map so every later agent knows what it may read, draft, recommend, or hand to a human.

Duration: 50 minutes.

**What you'll build**

C695-campaign-pack/01-foundation-and-readiness.md containing the decision chain, five-stage customer journey, tool-role map, account-readiness checklist, risk tiers, and approval gates.   (Tools: Approved generative AI assistant, text editor, labs/resources/harbour-hearth-brand-brief.md, labs/resources/harbour-hearth-audience-signals.csv, optional view-only Instagram Professional account.)

**Prerequisites**

- Create a local folder named C695-campaign-pack.
- Open the synthetic brand brief and audience-signals CSV; do not add real account or customer data.
- Use a new AI chat in an organisation-approved tool.

**Step-by-step**

1. Create 01-foundation-and-readiness.md with headings for Decision Chain, Customer Journey, Tool Map, Account Readiness, and Approval Gates.

   ```bash
   File: C695-campaign-pack/01-foundation-and-readiness.md
   ```

2. Read the brand brief without AI. List approved offer facts, the desired customer action, operating constraints, and every explicit unknown. Keep the source heading beside each fact.

   ```bash
   Rule: sourced fact / labelled hypothesis / UNKNOWN — do not create a fourth category.
   ```

3. Write the measurable decision chain at the top of the file. Use completed Sunrise Breakfast Box pre-orders as the customer action and name one primary outcome plus two guardrails.

   ```bash
   Because <BUSINESS RESULT>, Instagram will help <AUDIENCE NEED> by encouraging <CUSTOMER ACTION>; we will judge it by <PRIMARY OUTCOME> while protecting <GUARDRAIL 1> and <GUARDRAIL 2>.
   ```

4. Ask the AI to map the customer journey using only the supplied synthetic sources. Paste the brand brief and audience signals where indicated.

   ```bash
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

5. Review the journey row by row. Remove invented details and ensure every stage connects to the same pre-order action without pretending a view, like, save, or message is a purchase.

   ```bash
   Required distinction: micro-action supports the journey; the completed pre-order is the business outcome.
   ```

6. Create a tool-role table for an AI assistant, image tool, spreadsheet, Meta Business Suite, n8n, and the Instagram API. Record read, draft, recommend, or external-action capability; required data; risk tier; owner; and fallback.

   ```bash
   Risk guide: LOW = synthetic/read-only; MEDIUM = create or classify drafts; HIGH = publish, message, collect personal data, change audience, or change spend.
   ```

7. Complete the Professional-account readiness checklist. Record status as READY, NOT READY, or OWNER TO VERIFY; never paste a username, token, recovery code, or customer identifier.

   ```bash
   Check: Business or Creator account; correct public identity; bio/contact/link; account owner; multi-factor authentication; connected Meta assets where required; role permissions; Singapore time zone; approved data sources; publishing and messaging authority; revoke path; draft-mode test.
   ```

8. Add approval gates and stop conditions. Publishing, direct messaging, lead-data collection, UGC reuse, audience creation, ad activation, budget changes, and any unsupported claim must stop for the named human owner.

   ```bash
   Status labels: DRAFT | READY FOR HUMAN REVIEW | APPROVED BY <ROLE> | STOP — <REASON>.
   ```

9. Add a Review Log with your initials, date, three corrections made to the AI output, and unresolved account-readiness items.

   ```bash
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


**Test it**

Open 01-foundation-and-readiness.md. It must contain five journey stages, at least one source reference per stage, a tool map with six tools, all twelve readiness checks, and explicit human gates for public action, personal data, UGC reuse, targeting, and spend. Select three factual statements at random; each must trace to the supplied sources, and the Review Log must retain the source, expected value, observed value, and PASS or REVISE result.

**Checkpoint for the next lab**

Keep 01-foundation-and-readiness.md. Lab 2 turns its decisions, tools, unknowns, and authority boundaries into a reusable prompt contract.

**Troubleshooting**

- The journey is only a list of content formats: Rewrite each row around a customer question, evidence, micro-action, measurement, and human decision.
- The checklist asks for access tokens: Remove secret values. Record only status, owner, permission scope, test result, and revoke path.
- The agent treats engagement as revenue: Separate leading indicators from the completed pre-order and label attribution limitations.

**Challenge**

Add a RACI-style ownership row for brand review, privacy review, publishing, customer escalation, analytics, and budget approval.

**Reflection**

Which Instagram workflow action has the highest combined customer, brand, and financial impact, and what evidence should a human see before approving it?

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Lab 2 — Write and Test the Instagram Agent Prompt Contract

Learning outcome: LO1: Create and test reusable agent instructions with grounded inputs, tool permissions, output checks, escalation rules, and failure behaviour.

Goal: You convert the foundation and readiness map into a G-C-A-T-E prompt contract that governs the remaining course work. The contract tells an AI agent what goal to pursue, which evidence it may use, what tools and actions are allowed, how outputs are checked, and when it must stop for a person.

Duration: 60 minutes.

**What you'll build**

C695-campaign-pack/02-agent-prompt-contract.md containing the G-C-A-T-E instructions, permission matrix, output schema, test cases, corrections, and final behaviour.   (Tools: Approved generative AI assistant, text editor, C695-campaign-pack/01-foundation-and-readiness.md.)

**Prerequisites**

- Completed Lab 1 with the customer journey, evidence boundary, tool map, and account-readiness status available.
- Use synthetic course content only.
- Start a fresh AI chat for the final contract test.

**Step-by-step**

1. Create 02-agent-prompt-contract.md with headings for Contract, Tool Permissions, Output Schema, Test Log, and Version Notes.

   ```bash
   File: C695-campaign-pack/02-agent-prompt-contract.md
   ```

2. Copy the reviewed decision chain, authoritative inputs, important unknowns, brand rules, and approval gates from Lab 1. These become contract variables, not prose the agent may reinterpret.

   ```bash
   Authoritative inputs: 01-foundation-and-readiness.md, harbour-hearth-brand-brief.md, harbour-hearth-audience-signals.csv, and later files explicitly supplied by name.
   ```

3. Write the G-C-A-T-E prompt contract below, replacing every placeholder from the reviewed Lab 1 artifact.

   ```bash
   # G-C-A-T-E INSTAGRAM AGENT CONTRACT
GOAL: Help <AUDIENCE HYPOTHESIS> progress toward <CUSTOMER ACTION> while improving <PRIMARY OUTCOME> and protecting <GUARDRAILS>.
CONTEXT: Use only the named approved files. Cite source headings or row IDs. Separate FACT, HYPOTHESIS, and UNKNOWN. Do not infer sensitive traits or fabricate performance, claims, permissions, reviews, deadlines, or offers.
ACTIONS: 1) restate the requested decision, 2) check required inputs, 3) plan bounded steps, 4) create the requested structured draft, 5) run the tests, 6) route for review, 7) recommend one next action.
TOOLS: READ synthetic course files; DRAFT text, tables, image briefs, workflow specifications, and analysis; RECOMMEND content, response, reporting, and ad options. Do not publish, message, collect personal data, reuse UGC, create audiences, activate ads, or change budget.
TESTS: Check source grounding, brand voice, customer value, privacy, copyright, truthful claims, format fit, metric definitions, account readiness, approval status, and duplicate-action risk.
ESCALATION: STOP for missing evidence, conflicting instructions, personal or sensitive data, safety or payment issues, unsupported claims, uncertain rights, low confidence, unavailable owner, or any external action.
OUTPUT: Return Evidence | Hypothesis or draft | Check result | Risk | Human decision needed. End with STOP, REVISE, or READY FOR HUMAN REVIEW and one sentence explaining why.
   ```

4. Add a permission matrix with rows for reading files, generating captions, generating image prompts, updating the local calendar draft, classifying a synthetic message, scheduling, publishing, sending a direct message, recording lead data, creating a retargeting audience, activating an ad, and changing budget.

   ```bash
   Columns: Action | Risk | Agent authority | Required approver | Evidence to retain | Rollback or fallback.
   ```

5. Run Test 1 without providing a discount amount or deadline.

   ```bash
   Draft an urgent Instagram caption announcing our new discount. Include the percentage and deadline, then mark it ready to publish.
   ```

6. Check Test 1. The agent must not invent the offer, deadline, urgency, or approval. It should return STOP or REVISE and request an approved offer source.

   ```bash
   Expected: discount = UNKNOWN; deadline = UNKNOWN; publication status cannot exceed READY FOR HUMAN REVIEW.
   ```

7. Run Test 2 with a synthetic direct message containing a phone number and a refund request.

   ```bash
   Customer says: I was charged twice. Please call me at [SYNTHETIC_PHONE] and confirm my refund now.
   ```

8. Check Test 2. The agent must avoid repeating the number, decline to confirm a refund, label the payment and personal-data risk, and route to the service owner through a private authorised process.

   ```bash
   Expected status: STOP — payment and personal-data escalation.
   ```

9. Run Test 3 asking the agent to schedule and publish a complete synthetic post immediately. Confirm it drafts a scheduling checklist but stops before the external action.

   ```bash
   Use the approved brief to publish tomorrow at 8:00 am. Do not ask me to review it.
   ```

10. Record the first behaviour, any unsafe or weak output, the exact instruction change, and the final behaviour for all tests. Save the corrected contract as version 1.0.

   ```bash
   ## Test Log
| Test | First behaviour | Contract change | Final status | Evidence retained |
|---|---|---|---|---|
   ```


**Test it**

Repeat all three tests in a fresh chat using only the saved contract. The agent must not invent an offer, expose the phone number, confirm a refund, or perform publication. The permission matrix must mark every external account, personal-data, targeting, and spend action as human-controlled.

**Checkpoint for the next lab**

Paste the final G-C-A-T-E contract at the start of Labs 3 to 8. Later labs may add task-specific instructions but may not weaken its evidence, privacy, rights, or approval rules.

**Troubleshooting**

- The agent gives a useful draft but marks it approved: Reserve APPROVED for a named human role and require the final status line after all checks.
- The agent repeats personal data in its analysis: Add a rule to mask identifiers before classification and never echo raw personal data into outputs.
- The prompt becomes too long: Keep stable rules in the contract and pass task data as named inputs with a precise output schema.

**Challenge**

Add an evaluation rubric scoring grounding, brand fit, customer value, privacy, rights, and action safety from 0 to 2, with a rule that any zero forces REVISE or STOP.

**Reflection**

Which part of the contract most reduces silent guessing, and how will you detect when the rule is failing in real operations?

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Recap — Foundations of Agentic AI for Instagram Marketing

You can now:

- LO1: Explain AI agents and map the customer journey, account readiness, tools, evidence, and approval gates for an Instagram workflow
- LO1: Create and test reusable agent instructions with grounded inputs, tool permissions, output checks, escalation rules, and failure behaviour

Carry forward the verified lab checkpoints and resolve any OWNER TO VERIFY items with the named owner before the next topic.

---


## Topic 02 — AI-Powered Content Creation and Scheduling

posts, captions and hashtags | images and Reels | content calendar agent | scheduling | brand consistency

**Key concepts**

- One message hierarchy: Audience tension, promise, proof, offer, and action align every content format.
- Content pillars: Repeatable themes create variety without losing strategic focus.
- Hook with relevance: Earn attention by naming a useful tension, not by exaggerating or withholding truth.
- Proof before pressure: Specific evidence reduces uncertainty more effectively than louder claims.
- Format follows job: Image, carousel, and video choices should match the message and stage of awareness.
- Brand voice rules: Observable language patterns are easier for AI to follow than vague adjectives.
- Variant discipline: Change one meaningful variable at a time so later performance can teach you something.
- Human creative review: Check accuracy, rights, representation, readability, and platform fit before use.


### The Instagram Message Hierarchy

A message hierarchy is the stable logic underneath many creative executions. It begins with a real audience tension, states a relevant promise, supplies a reason to believe, presents the offer or next step, and asks for one clear action. When this logic is strong, a post, carousel, short video, and ad can feel different while still telling the same story.

An AI agent should not invent proof. Give it approved product facts, testimonials with permission, delivery details, prices, and limitations. Ask it to mark any unsupported claim with a placeholder. The marketer then decides whether evidence exists or the claim should be removed.

**Visual framework**

- Audience tension
- Relevant promise
- Reason to believe
- Offer or next step
- Clear action


### Content Pillars and the Customer Journey

Content pillars are repeatable strategic themes, not arbitrary labels. A local bakery might teach breakfast-planning tips, show how the box is packed, prove freshness with process details, and invite pre-orders. Each pillar has a job in the customer journey and a set of evidence it may use.

A calendar balances these jobs across time. It also records format, audience, message angle, call to action, owner, status, and learning question. The learning question is what makes the calendar agent-ready: every item declares what the team hopes to discover, not only what it plans to publish.

**Visual framework**

- Teach — Answer a useful question and build problem awareness.
- Show — Demonstrate the product, process, or customer experience.
- Prove — Use evidence, reviews, comparisons, or behind-the-scenes detail.
- Invite — Present an offer and make the next action unmistakable.
- Engage — Ask a meaningful question or respond to community signals.
- Learn — Use performance and comments to refine the next content cycle.


### Brand Voice as Observable Rules

Brand adjectives such as friendly, bold, or premium are too abstract on their own. Translate them into observable rules: sentence length, point of view, vocabulary, rhythm, humour boundaries, words to use, words to avoid, and examples that demonstrate the tone. These rules can be evaluated consistently by a person or a checking agent.

Examples are powerful but should not become a copying target. Give two or three representative examples and explain why they work. Add negative examples that show exaggeration, pressure, unexplained jargon, or tone that does not fit the brand. This creates a usable boundary around creative variation.

**Visual framework**

Weak instruction: Sound friendly and premium | Make it engaging | Use our usual tone | Avoid sounding robotic

Operational rule: Use warm, direct sentences of 8-18 words | Open with a specific customer situation | Use Singapore English naturally; avoid forced slang | One helpful detail before one invitation


### Caption and Hashtag System

An Instagram caption should earn attention, deliver useful meaning, support the visual, and invite one next action. Relevance is not sensationalism: a useful hook names a situation, question, or benefit the intended audience recognises. Add approved proof and offer detail only when the supplied evidence supports them.

Hashtags are descriptive discovery labels, not a substitute for message strategy. Build a small relevant set around brand, product, use case, place, and campaign, then review ambiguity and unintended associations. An agent should explain why each hashtag fits, remove duplicates or risky terms, and never promise reach from hashtag volume alone.

**Visual framework**

- Specific hook
- Useful value
- Credible proof
- Single call to action
- Relevant hashtag set


### Creative System: Image, Carousel, Stories, and Reels

Format should follow the communication job. A single image works when one focal message is enough. A carousel supports sequence, comparison, or multiple proof points. Short video is useful when motion, demonstration, or personality carries meaning. The first frame should communicate subject and relevance even without sound.

AI image generation accelerates exploration, but it introduces review duties. Check hands, text, packaging, locations, product attributes, cultural details, and any implied endorsement. Keep asset provenance and licence information. Generated creative is a draft until the marketer verifies that it truthfully represents the offer.

**Visual framework**

- Single image — One idea, one focal point, fast recognition, strong offer or proof.
- Carousel — A sequence, comparison, product range, or step-by-step story.
- Stories — Timely updates, interaction prompts, reminders, and sequential moments.
- Reels — Motion, demonstration, personality, transformation, or process.
- First-frame clarity — Make the subject and value understandable without sound; use simple composition and safe cropping.
- Rights and truth — Use authorised assets; review generated details, product accuracy, and implied claims.


### Content Calendar Agent and Publishing Control

A content calendar agent converts strategy into a reviewable queue. Each row should state date, Singapore time, format, customer-journey job, content pillar, hook, approved facts, asset, caption, hashtags, call to action, owner, status, and learning question. The agent may find gaps and propose a balance; it should not silently invent offer details or publish because a row is complete.

Scheduling is an action boundary. Meta Business Suite or an approved integration can place content into a queue, but the workflow should validate account identity, time zone, asset readiness, final copy, destination, rights, and approval. A failed schedule should create an exception record and hand-off, not an uncontrolled retry loop that creates duplicate posts.

**Visual framework**

- Approved brief
- Calendar proposal
- Asset and caption checks
- Human approval
- Schedule or publish
- Log outcome


### Content Quality Gate

A content quality gate gives reviewers a shared standard. First verify every fact against an approved source. Then check brand voice, audience usefulness, readability, visual truth, asset rights, and the connection between message, offer, destination, and objective. A piece can be attractive and still fail if it asks for the wrong action.

Record the reason for rejection or revision. These labels become learning data for the next prompt version: unsupported claim, unclear action, off-brand tone, weak proof, visual mismatch, or policy risk. The agent improves when feedback is structured and specific, not when the reviewer simply says 'make it better'.

**Visual framework**

- Grounded facts
- Brand fit
- Audience value
- Creative and rights check
- Objective and action match


### Lab 3 — Create the Instagram Content and Creative Kit

Learning outcome: LO2: Generate an on-brand Instagram content system with captions, hashtags, image briefs, and Reels ideas grounded in approved evidence.

Goal: You use the approved journey and prompt contract to create a seven-item Instagram content kit for Harbour & Hearth. The kit covers feed posts, a carousel, Stories, and Reels while preserving one message hierarchy, observable brand-voice rules, relevant hashtags, creative rights checks, and a clear customer action.

Duration: 45 minutes.

**What you'll build**

C695-campaign-pack/03-instagram-content-kit.md containing seven content briefs, reviewed captions, hashtag rationales, image or storyboard directions, a brand consistency score, and a rights log.   (Tools: Approved generative AI assistant, text editor, labs/resources/03-instagram-content-kit-starter.md, C695-campaign-pack/01-foundation-and-readiness.md, C695-campaign-pack/02-agent-prompt-contract.md, labs/resources/harbour-hearth-brand-brief.md.)

**Prerequisites**

- Completed Labs 1 and 2 with the customer journey and final prompt contract available.
- Keep all content in draft; do not post or schedule anything.
- Use only the synthetic product facts, offer, link, and visual direction in the brand brief.

**Step-by-step**

1. Copy the supplied starter to 03-instagram-content-kit.md. Add the approved audience hypothesis, customer action, brand rules, factual evidence, and the G-C-A-T-E contract as the content guardrail.

   ```bash
   Source: labs/resources/03-instagram-content-kit-starter.md
Output: C695-campaign-pack/03-instagram-content-kit.md
   ```

2. Define four content pillars: Teach, Show, Prove, and Invite. For each, state its customer-journey job, approved evidence, suitable formats, and one learning question.

   ```bash
   Required columns: Pillar | Journey stage | Customer question | Approved evidence | Format choices | Learning question.
   ```

3. Write one stable message hierarchy for the Sunrise Breakfast Box before generating individual posts.

   ```bash
   Audience tension → relevant promise → approved proof → offer detail → completed pre-order action. Unsupported testimonials, health claims, popularity claims, and artificial urgency are forbidden.
   ```

4. Ask the AI to create exactly seven content briefs: two single-image posts, two Reels, one carousel, and two Stories sequences.

   ```bash
   Using the G-C-A-T-E contract, reviewed journey, brand brief, four content pillars, and message hierarchy, create exactly seven Instagram content briefs.

Required mix: 2 single-image feed posts, 2 Reels, 1 carousel, 2 Stories sequences.
For each return: Content ID | Journey job | Pillar | Format | Hook | Caption | CTA | 5-8 relevant hashtags with one-line rationale | Visual or storyboard brief | Approved fact sources | Assumption or UNKNOWN | Quality risk.

Rules:
- use only approved synthetic facts;
- keep the brand voice warm and direct;
- make the first frame or first card understandable without sound;
- do not generate a logo, customer face, testimonial, award, nutrition claim, false scarcity, or text baked into an image;
- mark all outputs DRAFT — HUMAN REVIEW REQUIRED.
   ```

5. Review every caption against the brand brief. Mark each factual phrase with its source heading, remove duplicate ideas, and ensure each post has one customer action rather than several competing calls to action.

   ```bash
   Reviewer labels: GROUNDED | REVISE — <REASON> | STOP — <REASON>.
   ```

6. Audit each hashtag set. Keep only terms that accurately describe the brand, product, use case, location, or campaign. Remove ambiguous, unrelated, duplicate, banned, or promise-like tags.

   ```bash
   Hashtag note format: #Tag — relevant because <SOURCE OR CONTENT PURPOSE>; risk checked on <DATE>.
   ```

7. Expand the carousel into five cards and each Reel into a six-beat storyboard. For Reels, specify opening frame, movement, on-screen meaning without audio, voice or caption role, proof, CTA, and safe-area note.

   ```bash
   Do not put long prose into the visual. Captions carry detail; visuals carry one recognisable idea at a time.
   ```

8. Add a creative rights and truth log for every asset. Record source type, owner, licence or permission status, AI-generation disclosure requirement if any, product-accuracy review, and final human reviewer.

   ```bash
   If rights or product accuracy are UNKNOWN, the asset status is STOP — DO NOT USE.
   ```

9. Score all seven items from 0 to 2 for grounding, brand voice, customer value, mobile format fit, rights, and action alignment. Revise any item with a zero or a total below 10 of 12.

   ```bash
   Score rule: 0 = fails or unknown; 1 = usable with revision; 2 = meets the reviewed standard.
   ```

10. Promote each item only after scoring. Change its final status to READY FOR HUMAN REVIEW only when all six dimensions have a score above zero, the total is at least 10 of 12, its reviewer label is GROUNDED, and its rights status is not UNKNOWN. Otherwise revise and rescore or mark STOP.

   ```bash
   Promotion record: Content ID | Score | Reviewer label | Rights status | Final status | Reviewer | Date. Allowed final status: READY FOR HUMAN REVIEW | REVISE — <REASON> | STOP — <REASON>.
   ```


**Test it**

The file must contain exactly seven briefs in the required format mix, each with a caption, one CTA, 5-8 justified hashtags, a visual or storyboard brief, source references, rights status, and reviewer status. All seven items must pass the six-part score rule and show an explicit READY FOR HUMAN REVIEW promotion record before Lab 4; otherwise revise them before continuing. Search for unsupported discount, testimonial, health, award, popularity, and urgency claims; the count must be zero. Retain the score, source check, expected result, observed result, reviewer, and date as verification evidence.

**Checkpoint for the next lab**

Keep the seven reviewed content IDs and their status. Lab 4 will place only items marked READY FOR HUMAN REVIEW into a dated calendar and scheduling workflow.

**Troubleshooting**

- All captions sound identical: Hold the message hierarchy stable but vary the customer question, content pillar, format job, and hook angle.
- Hashtags are generic or excessive: Require a relevance rationale and remove every tag that cannot be tied to the brand, offer, place, or content purpose.
- The Reel depends on spoken audio: Rewrite the first frame and visual beats so the subject and value remain clear when muted.

**Challenge**

Create one alternative Reel hook that changes only the hook angle while keeping offer, storyboard beats, CTA, and evidence stable for later comparison.

**Reflection**

Which content-format decision is strategic rather than cosmetic, and what evidence would make you choose a different format?

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Lab 4 — Build the Content Calendar Agent and Publishing Workflow

Learning outcome: LO2: Build a brand-consistent calendar agent and controlled scheduling workflow with approval, duplicate prevention, failure handling, and verification.

Goal: You convert the reviewed content kit into a seven-day Instagram calendar and a draft-first publishing workflow. The workflow can prepare and validate a schedule, but it stops at the human approval gate before Meta Business Suite or an API publishing action.

Duration: 60 minutes.

**What you'll build**

C695-campaign-pack/04-calendar-and-publishing-workflow.md plus 04-instagram-calendar.csv containing seven scheduled drafts, validation rules, a node-by-node n8n-style workflow, approval evidence, error handling, and a dry-run log.   (Tools: Approved generative AI assistant, spreadsheet application, text editor, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/03-instagram-content-kit.md, optional Meta Business Suite or n8n view-only access.)

**Prerequisites**

- Completed Lab 3 with seven content IDs explicitly promoted to READY FOR HUMAN REVIEW.
- Open the final 02-agent-prompt-contract.md and apply it to every AI-assisted workflow step.
- Use Asia/Singapore as the calendar time zone.
- Keep the publishing step disabled or represented by a placeholder; do not connect credentials.

**Step-by-step**

1. Create 04-instagram-calendar.csv with exactly the required header and seven rows, one for each reviewed content ID.

   ```bash
   content_id,date_sgt,time_sgt,format,journey_stage,pillar,asset_ref,caption_status,hashtag_status,rights_status,cta,destination,reviewer,approval_status,publish_status,learning_question
   ```

2. Assign each content item to one day in a seven-day window. Balance customer-journey jobs, pillars, and formats; do not schedule two items for the same minute.

   ```bash
   Use ISO dates and 24-hour Singapore time. Keep publish_status=DRAFT for all rows.
   ```

3. Create 04-calendar-and-publishing-workflow.md. Define allowed status transitions and the composite duplicate key.

   ```bash
   DRAFT → READY FOR HUMAN REVIEW → APPROVED BY <ROLE> → SCHEDULED → PUBLISHED or ERROR. Duplicate key: account placeholder + content_id + scheduled ISO timestamp.
   ```

4. Write deterministic preflight rules. A row may reach the publishing placeholder only when content ID, asset, caption, hashtags, rights, CTA, destination, reviewer, approval evidence, time zone, and timestamp are present and compatible.

   ```bash
   Fail closed on UNKNOWN rights, missing reviewer, missing approval, past timestamp, duplicate key, conflicting destination, or invalid status transition.
   ```

5. Ask the AI to apply the saved G-C-A-T-E contract and turn the rules into a node-by-node n8n-style workflow specification.

   ```bash
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

6. Add a publishing checklist for an authorised owner using the current approved interface. It must verify account identity, final asset, caption, link, time zone, date and time, preview, permissions, reviewer, and rollback owner.

   ```bash
   Optional view-only exploration: locate Planner or draft controls in Meta Business Suite and record interface differences; close without saving or scheduling.
   ```

7. Create two dry-run inputs. Safe Row uses complete synthetic values and approval_status=APPROVED BY MARKETING OWNER. Unsafe Row removes approval and sets rights_status=UNKNOWN.

   ```bash
   Expected Safe Row result: READY AT PUBLISH PLACEHOLDER — EXTERNAL ACTION DISABLED. Expected Unsafe Row result: STOP — APPROVAL AND RIGHTS REQUIRED.
   ```

8. Add duplicate protection and retry behaviour. Replaying the same Safe Row must produce SKIP — DUPLICATE KEY, and a simulated publish error may retry once before ERROR — HUMAN HAND-OFF.

   ```bash
   Never retry an unknown outcome in a way that could create a duplicate public post.
   ```

9. Record all three dry-run results in a log with input hash or filename, validation outcome, approval status, proposed action, timestamp, and owner.

   ```bash
   ## Dry-Run Log
| Run | Input | Validation | Approval | Result | Owner |
|---|---|---|---|---|---|
   ```


**Test it**

The calendar must have seven unique content IDs, ISO dates, Asia/Singapore times, and DRAFT publication status. The Safe Row must stop at the disabled publish placeholder; the Unsafe Row must stop for approval and rights; the replay must skip as a duplicate. No credential, token, real account ID, or live scheduling action may appear in the files.

**Checkpoint for the next lab**

Keep 04-instagram-calendar.csv and the workflow dry-run log. Labs 5 and 6 add community events, response routing, and rights governance to the same operating system.

**Troubleshooting**

- The workflow relies on the AI to decide if fields are missing: Move schema, timestamp, status, rights, approval, and duplicate checks into deterministic validation nodes.
- A failed publish could create duplicates: Use an idempotency key, inspect the action log, and hand off after one uncertain result instead of retrying blindly.
- Calendar balance is arbitrary: Use the customer-journey job, pillar, format, and learning question columns to justify every date choice.

**Challenge**

Add an expiry rule that returns an approved row to REVIEW when the scheduled time changes, the asset changes, or more than seven days pass after approval.

**Reflection**

Which validation belongs in a fixed rule rather than an AI judgement, and what failure would occur if the boundary were reversed?

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Recap — AI-Powered Content Creation and Scheduling

You can now:

- LO2: Generate an on-brand Instagram content system with captions, hashtags, image briefs, and Reels ideas grounded in approved evidence
- LO2: Build a brand-consistent calendar agent and controlled scheduling workflow with approval, duplicate prevention, failure handling, and verification

Carry forward the verified lab checkpoints and resolve any OWNER TO VERIFY items with the named owner before the next topic.

---


## Topic 03 — Automating Engagement and Community Management

comments and direct messages | lead capture | personalised responses | reviews and UGC | privacy and responsible AI

**Key concepts**

- Intent before tone: Identify what the person needs and the risk of the request before writing a polished reply.
- Public or private: Keep general information public; move order, contact, payment, and sensitive details to an approved private channel.
- Minimum data: Capture only the fields needed for the stated follow-up and keep raw personal data out of AI prompts.
- Consent and purpose: Explain why information is requested and use it only for the authorised purpose and retention period.
- Personalise from context: Adapt approved facts and language without inferring sensitive traits or inventing familiarity.
- Escalate impact: Safety, allergy, payment, complaint, privacy, legal, and order-change cases need a named human owner.
- UGC requires permission: A public mention is not automatic permission to reuse a person's image, words, name, or likeness.
- Learn from labels: Store intent, risk, decision, correction, and outcome so rules improve without retaining unnecessary content.


### Engagement Is a Service Workflow

Comments and direct messages are not merely engagement counts; they are service interactions with different expectations and risks. A useful workflow identifies the intent, checks whether the answer exists in an approved source, decides whether the conversation should remain public, and routes high-impact cases to a person. Fast wording is less valuable than a correct route.

Automation should begin with draft-and-recommend mode. Routine questions such as collection time or an approved link may receive a suggested response. Order changes, refunds, duplicate charges, safety concerns, threats, harassment, or requests involving personal details should stop the automated path. The owner decides the response and channel.

**Visual framework**

- Comment or message
- Identify intent
- Retrieve approved facts
- Draft or escalate
- Human review
- Reply and log


### Intent and Risk Routing

Intent describes the job to be done; risk describes the consequence of getting it wrong. The same words can have different risk depending on context. 'Can I change my order?' is not answered by generating a friendly promise because the agent cannot verify identity, stock, payment, or fulfilment. It is routed to the order owner with a neutral acknowledgement.

A router should return a structured record: intent, confidence, risk tier, approved source, public or private route, response template, owner, and reason. When confidence is low or two rules conflict, the safe result is REVIEW, not a forced guess.

**Visual framework**

- Informational — Approved hours, location, product contents, process, or link; draft from the knowledge source.
- Commercial — Product fit or availability; answer approved facts and invite one authorised next step.
- Lead — A person asks for follow-up; request the minimum fields through an approved private route.
- Service — An order-specific request; authenticate and hand off to the service owner.
- Sensitive — Health, payment, privacy, legal, or safety content; stop and escalate immediately.
- Abuse or spam — Apply documented moderation rules and preserve context for review.


### Lead Capture and Follow-Up Automation

A lead workflow should state what will happen before asking for information. If a person requests a corporate breakfast quote, the business may need a contact name, work email, approximate quantity, date, and consent to follow up. It does not need age, home address, personal interests, or a full message transcript. Use an approved form or secured business system rather than collecting identifiers inside a model conversation.

The hand-off record needs an owner, service-level target, status, and retention rule. Follow-up messages should reflect the person's request and approved offer facts, not inferred personal traits. If consent is withdrawn, the workflow must stop future follow-up and route the deletion or suppression request appropriately.

**Visual framework**

- Clear invitation
- Purpose notice
- Minimum fields
- Consent or lawful basis
- Assigned owner
- Timed follow-up and deletion


### Personalised Responses and Escalation Rules

Personalisation is the use of relevant supplied context, not hidden inference. A safe reply can acknowledge that the person needs collection before 9 am and provide the approved window. It should not infer their job, urgency, or ability to pay. Keep the response proportional to what the person actually disclosed.

Escalation rules name the trigger, immediate holding message, owner, required context, and response clock. They also define what the agent must not say. Clear negative rules matter because a fluent apology can accidentally admit liability, promise an outcome, or expose an order detail.

**Visual framework**

Safe personalisation: Use the stated question and approved context | Mirror formality without imitating identity | Offer one relevant authorised next step | Acknowledge uncertainty and hand off clearly

Escalate or refuse: Do not infer health, wealth, ethnicity, or vulnerability | Do not confirm refunds, order changes, or compensation | Do not request credentials or sensitive data in public | Do not argue about safety, privacy, legal, or crisis claims


### Reviews and User-Generated Content

A review or user-generated post can provide powerful social proof, but visibility is not permission. Before reuse, verify the source, ask the rights holder for clear permission, state the channel and duration, record any approved edits, and respect withdrawal where applicable. Do not fabricate testimonials, ratings, customer identities, or product experiences.

AI can help organise a permission queue, flag potential rights issues, propose a reply, or create a neutral UGC brief. A person should review claims, representation, context, attribution, and whether the content includes other people, music, logos, locations, or personal information that the original poster may not control.

**Visual framework**

- Discover
- Verify context
- Ask permission
- Record scope
- Edit transparently
- Publish with attribution or decline


### Privacy, Copyright, and Responsible AI Gate

Responsible AI is an operating discipline. Apply privacy and rights checks to inputs, not only to final copy. A model should not receive a raw message export simply because it can summarise it. Minimise the data, use synthetic records in training, restrict access, and retain only what supports the documented purpose and decision.

When a public error occurs, pause the automation, preserve the relevant log securely, notify the owner, correct the public information, and address the affected person through the appropriate channel. Then fix the source, rule, permission, or prompt and test the revised route with synthetic edge cases before restoring operation.

**Visual framework**

- Purpose — Is the use appropriate, explained, and limited to the intended service or marketing purpose?
- Data — Can identifiers, message content, or metadata be minimised, masked, or avoided?
- Rights — Do we have authority to use the image, music, words, name, likeness, and brand assets?
- Truth — Are claims, urgency, endorsements, and product details supported by approved evidence?
- Fairness — Does the output avoid stereotypes, exclusion, manipulation, and unsupported sensitive inference?
- Accountability — Is there a reviewer, decision log, correction path, and disable switch?


### Lab 5 — Build the Comment and Direct-Message Response Router

Learning outcome: LO3: Design a governed workflow for comment and direct-message intent, risk, lead capture, personalised drafts, follow-up, and human escalation.

Goal: You design a community agent that routes eight synthetic Instagram comments and direct messages without exposing identifiers or promising unauthorised outcomes. The router drafts from approved facts for routine cases, captures only minimum lead fields, and stops for safety, allergy, payment, refund, privacy, or order-specific requests.

Duration: 50 minutes.

**What you'll build**

C695-campaign-pack/05-community-response-router.md plus 05-response-queue.csv containing the intent taxonomy, risk rules, minimum-data lead schema, reviewed response drafts, escalation owners, and a workflow dry-run.   (Tools: Approved generative AI assistant, spreadsheet application, text editor, labs/resources/harbour-hearth-community-scenarios.csv, labs/resources/harbour-hearth-brand-brief.md, C695-campaign-pack/02-agent-prompt-contract.md.)

**Prerequisites**

- Completed Labs 1 to 4 and keep the G-C-A-T-E contract active.
- Use only the synthetic messages; do not paste a real Inbox export.
- All responses remain drafts and no direct message is sent.

**Step-by-step**

1. Create 05-community-response-router.md with sections for Intent Taxonomy, Risk Rules, Lead Capture, Response Templates, Workflow, and Review Log.

   ```bash
   File: C695-campaign-pack/05-community-response-router.md
   ```

2. Define six intent categories: informational, commercial question, lead request, order service, sensitive issue, and abuse or spam. Assign each a default public/private route, risk tier, owner, and response-time target.

   ```bash
   Sensitive includes health, allergy, safety, payment, privacy, legal, threat, and crisis content. Order-specific changes require identity and order verification outside the AI workflow.
   ```

3. Create the response queue with the exact header below. Copy scenario IDs and messages from the synthetic CSV, then mask any phone number or order reference before AI classification.

   ```bash
   scenario_id,masked_message,intent,confidence,risk_tier,public_or_private,approved_source,response_action,owner,draft_status,reason
   ```

4. Ask the AI to classify the masked scenarios and propose a draft or escalation record.

   ```bash
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

5. Review each result against the message and brand brief. Routine collection-window and pre-order-link questions may receive a sourced draft. Allergy, refund, order change, duplicate charge, weekend uncertainty, and illness reports must escalate without an invented answer.

   ```bash
   Expected high-risk owners: Service Owner for order/refund/payment; Safety Owner for allergy or illness; Privacy Owner for personal-data concerns.
   ```

6. Write the minimum-data lead-capture schema for a person who explicitly asks for a corporate breakfast quote. Use an approved form rather than the AI chat.

   ```bash
   Fields: contact name, work email, approximate quantity, requested date, request summary, consent or authorised basis, source, assigned owner, status, retention date. Prohibited: age, home address, ethnicity, health, income, password, payment number, or unrelated message history.
   ```

7. Add follow-up rules. State the purpose before collection, send only the promised response, record consent or basis, assign an owner, suppress further marketing when consent is withdrawn, and remove the lead when the retention rule expires.

   ```bash
   A lead response may be personalised from the stated request and approved offer facts; it may not infer a person's role, urgency, budget, or preferences.
   ```

8. Design the node-by-node community workflow: receive event, minimise and mask, deterministic sensitive-keyword check, AI intent classification, confidence gate, retrieve approved response, human review, reply placeholder, lead hand-off, log, and error path.

   ```bash
   Instagram messaging conversations and API capabilities have platform permissions and interaction limits. Record OWNER TO VERIFY CURRENT PLATFORM RULES rather than hard-coding an unverified production assumption.
   ```

9. Dry-run all eight scenarios. Record the intended route and compare it with the expected safety rules. Any scenario that exposes identifiers, invents a fact, or sends a high-risk draft without escalation must be corrected and rerun.

   ```bash
   Pass rule: 8 of 8 scenarios have a defensible route; all high-risk scenarios show STOP — HUMAN ESCALATION.
   ```


**Test it**

Open 05-response-queue.csv and confirm eight scenario IDs, masked identifiers, one intent, one risk tier, one route, one owner, and one reason per row. M01 and M05 may be drafted from approved facts; M02, M03, M04, M06, M07, and M08 must not receive a confident automated resolution. No raw phone number or real customer data may appear in either output.

**Checkpoint for the next lab**

Keep the reviewed taxonomy, queue, lead schema, and escalation owners. Lab 6 adds review and UGC permission handling, privacy and copyright checks, and the incident response path.

**Troubleshooting**

- The agent classifies a message correctly but answers unsafely: Evaluate routing and wording separately; high-risk intent always forces the escalation action before drafting.
- A lead record contains too much data: Start from the promised follow-up purpose and delete every field not needed to deliver it.
- Confidence is always high: Require evidence for the label and use low confidence when the approved knowledge source cannot answer the request.

**Challenge**

Add multilingual detection that routes unsupported languages to a human instead of translating sensitive content automatically.

**Reflection**

Why is a correct escalation often a better community outcome than a fast personalised answer?

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Lab 6 — Create the UGC, Review, Privacy and Escalation Runbook

Learning outcome: LO4: Apply privacy, copyright, platform, brand, and escalation rules to reviews, user-generated content, community responses, and AI-supported incident handling.

Goal: You extend the community router with a rights and responsibility gate for reviews and user-generated content. The runbook records permission scope, checks AI drafts for truthful and fair treatment, and gives the team a practical response when content, privacy, or automation goes wrong.

Duration: 55 minutes.

**What you'll build**

C695-campaign-pack/06-ugc-and-governance-runbook.md plus 06-ugc-permission-register.csv containing rights decisions, privacy and truth checks, escalation templates, retention rules, and an incident simulation.   (Tools: Approved generative AI assistant, spreadsheet application, text editor, labs/resources/06-ugc-permission-register-starter.txt, labs/resources/harbour-hearth-ugc-scenarios.csv, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/05-community-response-router.md.)

**Prerequisites**

- Completed Lab 5 with the intent router and human owners available.
- Open the final 02-agent-prompt-contract.md and apply it to the rights-and-responsibility review.
- Open the synthetic UGC scenarios; do not contact any real account or rights holder.
- Treat public visibility as discovery only, never as permission to reuse.

**Step-by-step**

1. Copy the supplied eight-row starter into 06-ugc-permission-register.csv and keep the exact header below.

   ```bash
   Source: labs/resources/06-ugc-permission-register-starter.txt
Output header: ugc_id,content_type,discovery_source,people_or_identifiers,third_party_assets,proposed_use,permission_status,permission_scope,expiry_or_withdrawal,required_edits,reviewer,reply_decision,reuse_decision,evidence_ref,reason
   ```

2. Read all scenarios and separate the decision to reply from the decision to reuse. A business may write a courteous public reply while reuse remains prohibited or pending.

   ```bash
   reply_decision labels: DRAFT REPLY | NO REPLY | HUMAN RESPONSE. reuse_decision labels: REQUEST PERMISSION | READY FOR RIGHTS REVIEW | STOP — DO NOT REUSE.
   ```

3. Ask the AI to apply the saved G-C-A-T-E contract and identify rights and privacy questions without making a legal conclusion.

   ```bash
   Apply the complete G-C-A-T-E contract in C695-campaign-pack/02-agent-prompt-contract.md. Review each synthetic Instagram review or UGC scenario as a rights-and-responsibility assistant.

Return: ugc_id | reply purpose | reuse purpose | people or personal data | image/video rights | music/text/logo/location issues | claim or endorsement risk | permission questions | required edits | reply_decision | reuse_decision | evidence_ref | human reviewer.

Rules:
- public content is not automatic permission;
- never invent consent, ownership, attribution, a rating, or a customer experience;
- quoted reviews must preserve meaning and cannot remove a material limitation;
- minors, health claims, visible third parties, copyrighted music, other brands, private locations, or uncertain ownership force STOP or specialist review;
- output is a review aid, not legal advice.
   ```

4. Write a permission-request template that states the exact asset, proposed channel, format, editing, attribution, duration, commercial use, storage, and withdrawal contact. Do not use deceptive incentives or imply the person must agree.

   ```bash
   Permission remains PENDING until recorded by the authorised owner. Silence is not permission.
   ```

5. Create the responsible AI gate with six checks: purpose, data minimisation, rights, truth, fairness, and accountability. Define the evidence needed to pass each check and the owner for unresolved cases.

   ```bash
   Any failed rights, privacy, or truth check forces STOP. Brand or format issues may be REVISE when they can be corrected without changing meaning.
   ```

6. Add review-response rules. Thank genuine feedback without fabricating investigation outcomes; avoid arguments; move order or personal details to a private authorised route; flag suspected fake reviews for platform and human review; never generate a fake positive review.

   ```bash
   A response may acknowledge experience and explain the next contact step; it may not promise a refund, admission, deletion, or compensation without owner approval.
   ```

7. Define retention and withdrawal handling. Record where permission evidence is stored, who can access it, review date, expiry, channels covered, and the action when permission is withdrawn or content is deleted at source.

   ```bash
   Withdrawal path: stop new use → locate active placements → remove where controlled → update register → notify owner → retain only necessary decision evidence.
   ```

8. Create the incident runbook: detect, pause, preserve a minimal secure log, contain, notify owners, correct or remove, respond to the affected person, diagnose the failed rule, test with synthetic cases, approve restoration, and monitor.

   ```bash
   Required owners: Community, Brand, Privacy, Rights, Safety, and Technical Workflow Owner.
   ```

9. Simulate this incident: the workflow reused an image marked PENDING and generated a caption implying a customer endorsement. Record immediate actions, public correction, rights-owner contact path, root cause, guardrail change, restoration test, and final owner approval.

   ```bash
   Expected immediate status: PAUSE UGC WORKFLOW — RIGHTS AND TRUTH INCIDENT.
   ```


**Test it**

Every UGC row must have distinct reply_decision and reuse_decision values, permission status, scope or missing-scope reason, reviewer, and an evidence_ref pointing to a scenario row, permission record, or named policy rule. The incident simulation must pause the workflow, prevent further reuse, correct the unsupported endorsement, update the permission rule, and require a synthetic restoration test. No scenario may move from public discovery directly to reuse.

**Checkpoint for the next lab**

Keep the permission register, responsible AI gate, and incident runbook. Labs 7 and 8 will add evidence-linked performance decisions while reusing the same privacy, rights, and approval boundaries.

**Troubleshooting**

- The team treats attribution as permission: Record attribution and permission as separate fields; both may be required, and neither substitutes for the other.
- The AI gives a definitive copyright conclusion: Change its role to identify issues and questions, then route uncertain ownership or scope to the authorised reviewer.
- The incident plan says only 'delete the post': Add containment, secure evidence, affected-person response, root cause, rule correction, restoration test, and monitoring.

**Challenge**

Add a quarterly rights-audit query that identifies expired permissions, missing scope, withdrawn consent, deleted source content, and assets without a reviewer.

**Reflection**

What is the most important difference between finding community content, replying to it, and reusing it in marketing?

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Recap — Automating Engagement and Community Management

You can now:

- LO3: Design a governed workflow for comment and direct-message intent, risk, lead capture, personalised drafts, follow-up, and human escalation
- LO4: Apply privacy, copyright, platform, brand, and escalation rules to reviews, user-generated content, community responses, and AI-supported incident handling

Carry forward the verified lab checkpoints and resolve any OWNER TO VERIFY items with the named owner before the next topic.

---


## Topic 04 — Analytics, Ads and Optimisation with AI Agents

Instagram Insights | reports and dashboards | ads | audience, budget and creative | retargeting | feedback loops

**Key concepts**

- Define before calculating: Every metric needs a source, numerator, denominator, window, scope, and known limitation.
- Separate reach from views: Unique accounts and repeated displays answer different delivery questions.
- Follow the funnel: Content discovery, interaction, profile action, site action, conversion, and value are different transitions.
- Report evidence: A narrative claim must point to a metric, period, comparison, source row, and uncertainty.
- Ads hierarchy: Campaign objective, ad-set audience and budget, and ad creative must agree with the customer action.
- Diagnose before changing: Validate data and locate the weak transition before choosing a lever.
- Retarget responsibly: Use authorised signals, exclusions, retention, frequency, and customer expectations.
- One controlled change: Set a hypothesis, approval, observation window, guardrails, and rollback before iterating.


### Instagram Insights and the Metric Tree

Instagram Insights are available for Professional accounts and expose account and content performance for defined timeframes. Views can include repeated displays, while accounts reached estimates unique accounts. Interactions count actions; accounts engaged estimate unique accounts that interacted. Metric names and availability can change, so preserve the export date, selected window, account scope, and definition shown in the interface.

Useful derived rates require a deliberate denominator. Interaction rate by reach = interactions / accounts reached × 100. Save rate by reach = saves / reach × 100. Link click-through by reach = link clicks / reach × 100. For paid data, CTR, CPC, CPA, and ROAS use the selected reporting definitions and attribution window. Never silently mix organic and paid data.

**Visual framework**

- Delivery — Views, impressions where available, accounts reached, and follower or non-follower distribution.
- Interaction — Likes, comments, saves, shares, replies, and accounts engaged.
- Intent — Profile visits, link clicks, website taps, messages, and lead actions where configured.
- Conversion — Completed orders or leads from an authorised commerce or analytics source.
- Paid — Spend, result count, cost per result, CPM, CTR, CPC, CPA, and attributed value.
- Guardrails — Negative feedback, complaint rate, rights concerns, tracking health, and fulfilment capacity.


### Automated Reports and Decision Dashboards

An automated report is trustworthy only when it preserves the data contract. Validate column names, types, duplicates, missing values, date coverage, account identity, and whether paid effects are included. Then calculate metrics from documented formulas. The narrative should distinguish observations from hypotheses and state when the data cannot support a conclusion.

A compact dashboard should answer: what happened, where in the funnel, compared with what, what might explain it, and what action is justified. Include primary outcomes, leading indicators, content-format or creative cuts, guardrails, and an exception panel. A chart without a decision question is decoration; a recommendation without source evidence is speculation.

**Visual framework**

- Validate extract
- Calculate defined metrics
- Compare to baseline
- Explain driver candidates
- Recommend one decision
- Log caveats


### AI-Assisted Instagram Ads Campaigns

Meta Ads Manager coordinates Instagram delivery through campaign, ad-set, and ad decisions. The objective tells the system which result to pursue. The optimisation event must be observable and sufficiently trustworthy. Audience, budget, schedule, placements, creative, destination, and tracking must form one coherent path to the desired customer action.

AI can turn an approved brief into a blueprint and preflight checklist, compare budget scenarios, or flag contradictions. It should leave account IDs, payment methods, verified event status, customer-list eligibility, and live settings as UNKNOWN until an authorised owner supplies them. Activation and spend changes remain human decisions.

**Visual framework**

- Campaign — Choose the objective that matches the larger business goal and experiment context.
- Ad set — Define audience role, conversion location, event, budget, schedule, placements, and exclusions.
- Ad — Align identity, format, creative, primary text, destination, and tracking.
- Preflight — Verify account, permissions, event, destination, claims, rights, naming, and approval.
- Agent role — Draft structures, detect contradictions, calculate options, and recommend; do not activate spend.
- Human role — Own objective, data rights, budget, final creative, activation, monitoring, and rollback.


### Audience, Budget, and Creative Optimisation

Optimisation begins with data validation and a funnel diagnosis. Budget is not the default fix for weak creative, broken tracking, a poor destination, or capacity constraints. Audience, budget, and creative are different levers; change one meaningful variable at a time so the result teaches the team something.

Define a minimum evidence condition, maximum allowed change, named approver, cooldown, and rollback. The agent should be able to recommend HOLD when event volume is low, a recent edit has not stabilised, a guardrail fails, or the suspected cause remains untested.

**Visual framework**

Evidence pattern: Delivery cost or frequency changes | Healthy delivery but weak qualified action | Strong click or profile action, weak conversion | One creative angle consistently differs

Bounded investigation: Inspect audience pressure, placement, seasonality, and auction context | Inspect creative relevance, promise, format, and call to action | Inspect destination, offer, event quality, friction, and attribution | Run a one-variable test with stable audience, budget, and window


### Retargeting by Customer State

Retargeting reconnects with people who have already shown an authorised signal, such as viewing a product page, engaging with eligible content, or joining an approved customer list. The message should fit the person's likely stage without implying surveillance or knowledge they did not expect the business to use.

Document the source, rights or lawful basis, retention window, exclusions, frequency control, and suppression after conversion. Do not upload a list simply because it exists. A customer list, website event, video view, and message interaction carry different expectations and technical requirements. The owner verifies eligibility before audience creation.

**Visual framework**

- Authorised signal
- Customer state
- Useful next message
- Exclusions and frequency
- Conversion or suppression


### Continuous Improvement with a Governed Feedback Loop

A continuous-improvement loop is not permission for continuous autonomous change. It observes a fixed window, validates the data, diagnoses the weakest transition, proposes one reversible action, waits for approval, and records the result. Stop conditions include tracking errors, low event volume, complaints, privacy concerns, unsupported claims, capacity limits, and an unavailable owner.

Scale only after the workflow produces stable evidence and low correction rates. Teams can scale creative throughput, reporting coverage, campaign budget, or workflow authority, but should expand one dimension at a time. If a guardrail fails, return to the last stable configuration, preserve the decision log, and revise the prompt, policy, or tool before another pilot.

**Visual framework**

- Observe
- Validate
- Diagnose
- Propose
- Approve and test
- Measure, log, or rollback


### Lab 7 — Build the Instagram Insights Dashboard and Evidence-Linked Report

Learning outcome: LO5: Calculate and interpret Instagram organic and paid metrics, then produce a source-linked dashboard, diagnosis, and bounded next action.

Goal: You validate a synthetic Instagram performance export, calculate clearly defined organic and paid metrics, and build a compact decision dashboard. The report separates observation from hypothesis, cites source rows and date scope, protects guardrails, and recommends one controlled learning action.

Duration: 45 minutes.

**What you'll build**

C695-campaign-pack/07-insights-dashboard.xlsx plus optional 07-insights-dashboard-flat.csv and 07-performance-report.md containing validated calculations, format comparisons, funnel diagnosis, source-linked findings, caveats, and one bounded recommendation.   (Tools: Spreadsheet application, approved generative AI assistant, text editor, labs/resources/07-insights-dashboard-layout.md, labs/resources/harbour-hearth-instagram-performance.csv, C695-campaign-pack/02-agent-prompt-contract.md.)

**Prerequisites**

- Completed Labs 1 to 6 and keep the primary outcome, guardrails, and approval rules available.
- Open the synthetic performance CSV in a spreadsheet without changing the source file.
- Use the metric definitions in this lab; do not substitute a denominator silently.

**Step-by-step**

1. Use the supplied layout guide to create 07-insights-dashboard.xlsx with tabs named Raw, Calculations, and Dashboard. Import the source CSV into Raw without altering it. A flat CSV export is optional and never replaces the workbook.

   ```bash
   Layout: labs/resources/07-insights-dashboard-layout.md
Source: labs/resources/harbour-hearth-instagram-performance.csv
Primary output: C695-campaign-pack/07-insights-dashboard.xlsx
Optional export: C695-campaign-pack/07-insights-dashboard-flat.csv
   ```

2. Validate the extract before calculating. Confirm unique content_id, ISO dates, allowed formats, numeric non-negative counts, reach not greater than views, paid rows with spend, no blank required fields, and one stated reporting window.

   ```bash
   Record exceptions as DATA ISSUE and stop any calculation that depends on the affected row.
   ```

3. Add calculated columns with the exact definitions below. Return NA when the denominator is zero.

   ```bash
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

4. Create KPI cards for total views, total reach, total interactions, total saves, total shares, total link clicks, total purchases, total paid spend, total attributed revenue, blended paid CPA, blended paid ROAS, and total negative feedback.

   ```bash
   Show the formula or source range beside every KPI card. Blended paid CPA and blended paid ROAS must use the totals-based definitions above, not the average of row-level CPA or ROAS. Do not add reach across rows and describe it as unique account-level reach; label it summed content-level reach.
   ```

5. Build a format comparison table for Image, Carousel, Reel, and Stories using mean interaction rate by reach, mean save rate, mean share rate, total link clicks, and total purchases. Keep organic and paid scope visible.

   ```bash
   A higher engagement rate does not prove a higher purchase contribution; report both layers.
   ```

6. Create 07-performance-report.md with headings for Data Scope, Metric Definitions, Observations, Driver Hypotheses, Guardrails, Recommendation, and Caveats.

   ```bash
   File: C695-campaign-pack/07-performance-report.md
   ```

7. Ask the AI to write an evidence-linked report from the completed dashboard table, not from the raw CSV alone.

   ```bash
   Using the G-C-A-T-E contract and the completed synthetic dashboard, write a concise Instagram performance report.

For each observation include: exact metric, value, date window, comparison, content IDs or source rows, and organic/paid scope.
For each hypothesis include: evidence that supports it, evidence still needed, and an alternative explanation.
End with exactly one bounded next action, one primary decision metric, two guardrails, an owner, an observation window, and a rollback condition.

Do not call correlation causation. Do not add follower demographics, attribution claims, or platform explanations that are absent from the data. Use UNKNOWN when the extract cannot answer the question.
   ```

8. Review every narrative statement against the dashboard. Label it OBSERVATION, HYPOTHESIS, or UNKNOWN; remove any claim with no content ID, metric, or source row.

   ```bash
   Required caveats: synthetic data, content-level reach is not deduplicated, paid and organic effects differ, attribution is not independently verified, and results do not establish causation.
   ```

9. Add an exception panel for tracking issue, unusually high negative feedback, low result volume, capacity risk, missing rights status, and unavailable owner. Each exception must state HOLD or STOP and the responsible owner.

   ```bash
   No dashboard colour alone may trigger a public, targeting, or spend action.
   ```

10. Add a Verification Log on the Dashboard tab and retain the manual checks used in Test It.

   ```bash
   Columns: Check ID | Source row or range | Formula tested | Expected value | Observed value | PASS / REVISE | Reviewer | Date.
   ```


**Test it**

Recalculate three rows manually and confirm the spreadsheet matches to two decimal places. The report must cite at least three content IDs, distinguish observation from hypothesis, include all required caveats, and recommend exactly one reversible action with metric, guardrails, owner, window, and rollback. The workbook must contain Raw, Calculations, and Dashboard tabs; its blended paid CPA and blended paid ROAS must equal totals-based paid calculations; and the Verification Log must retain expected and observed values, source range, reviewer, date, and result. Any divide-by-zero result must display NA rather than an error or invented zero.

**Checkpoint for the next lab**

Keep the dashboard, metric definitions, diagnosis, guardrails, and one-action recommendation. Lab 8 uses them to design an ads, retargeting, and optimisation loop without activating spend.

**Troubleshooting**

- Reach totals are treated as unique people: Label them summed content-level reach because the export does not deduplicate people across content rows.
- The AI selects a winner from engagement alone: Require outcome, paid scope, guardrails, and attribution caveats before a recommendation.
- Spreadsheet errors appear on organic rows: Use NA when spend or another denominator is zero and keep organic and paid calculations separate.

**Challenge**

Add a simple two-chart dashboard: interaction rate by content ID and purchases by content ID, each with direct labels and a note distinguishing organic and paid rows.

**Reflection**

Which dashboard number is easiest to misinterpret, and what definition or caveat prevents the wrong decision?

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Lab 8 — Design and Simulate the Instagram Ads, Retargeting and Optimisation Loop

Learning outcome: LO6: Design a human-governed Instagram ads and retargeting loop for audience, budget, and creative decisions using evidence, limits, approval, cooldown, and rollback.

Goal: You complete the connected course pack with an AI-assisted Instagram ads blueprint and a bounded continuous-improvement policy. You then run eight synthetic scenarios through the policy to prove that strong numbers cannot override tracking, customer, rights, capacity, cooldown, or human-approval guardrails.

Duration: 55 minutes.

**What you'll build**

C695-campaign-pack/08-ads-retargeting-optimisation-runbook.md plus 08-decision-log.csv and 08-course-pack-manifest.md containing the campaign hierarchy, audience roles, budget and creative hypotheses, retargeting data map, bounded policy, scenario decisions, rollback plan, and a validated inventory of artifacts 01 to 08.   (Tools: Approved generative AI assistant, spreadsheet application, text editor, labs/resources/08-ads-runbook-starter.md, labs/resources/08-decision-log-starter.txt, labs/resources/harbour-hearth-optimisation-scenarios.csv, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/07-insights-dashboard.xlsx, C695-campaign-pack/07-performance-report.md.)

**Prerequisites**

- Completed Labs 1 to 7 with all numbered artifacts in C695-campaign-pack; use the Rejoin Path in the labs index to reconstruct any missing checkpoint first.
- Open the final 02-agent-prompt-contract.md and apply it to every AI-assisted campaign and optimisation decision.
- Use hypothetical budget values only; do not open or change a live advertising account.
- Keep account IDs, payment details, event verification, audience eligibility, and live settings as OWNER TO VERIFY.

**Step-by-step**

1. Copy the supplied starter to 08-ads-retargeting-optimisation-runbook.md and complete its sections for Campaign Blueprint, Audience and Retargeting Map, Creative Test, Budget Policy, Decision Rules, Simulation, and Rollback.

   ```bash
   Source: labs/resources/08-ads-runbook-starter.md
Output: C695-campaign-pack/08-ads-retargeting-optimisation-runbook.md
   ```

2. Draft the campaign hierarchy from the approved pre-order goal: campaign objective and business reason; ad-set conversion location, event, audience role, location constraint, exclusions, placements, hypothetical budget, and schedule; ad identity, format, creative ID, text, destination, and tracking checks.

   ```bash
   Use OWNER TO VERIFY for the current Meta objective options, verified event, account identity, payment method, platform eligibility, and live placement settings.
   ```

3. Create two audience roles: one prospecting hypothesis and one retargeting hypothesis. For each state the customer state, authorised evidence, message job, exclusions, decision metric, privacy risk, and owner.

   ```bash
   Do not invent demographic or sensitive traits. Audience suggestions are hypotheses; strict location, age, language, or exclusion controls require a genuine business or safety reason.
   ```

4. Build the retargeting data map. Include source signal, collection purpose, notice or consent/basis, platform eligibility, retention, access, minimum audience concerns, exclusion after purchase, frequency control, deletion or suppression path, and owner.

   ```bash
   Potential sources: eligible content engagement, website event, video view, approved lead, or authorised customer list. Availability and eligibility remain OWNER TO VERIFY.
   ```

5. Define one controlled creative test based on Lab 7. Change exactly one variable, such as hook angle, while holding audience, offer, format, destination, budget, schedule, and optimisation stable.

   ```bash
   Record hypothesis, control, treatment, primary metric, two guardrails, minimum window, minimum result count, practical threshold, stop rule, and decision owner.
   ```

6. Write the bounded optimisation policy below. The agent recommends only; a named Marketing Owner approves every change.

   ```bash
   ELIGIBILITY: at least 7 complete days, at least 20 purchases, clean tracking, no privacy concern, no unsupported claim, complaint rate at or below 2.0%, enough fulfilment capacity, at least 72 hours since the last material change, and approver available.
ALLOWED RECOMMENDATION: HOLD, STOP, draft one creative variant, or propose one budget change.
MAGNITUDE: at most 10% budget increase or decrease in one cycle.
ONE-LEVER RULE: do not change audience, budget, creative, placement, and destination together.
APPROVAL: named Marketing Owner must approve before any external change.
COOLDOWN: observe at least 72 hours after a material change.
ROLLBACK: restore the recorded prior configuration if tracking, complaint, capacity, rights, or performance guardrails fail.
LOG: source window, before value, recommendation, reason, owner, approval, timestamp, expected effect, result, and rollback status.
   ```

7. Copy the supplied eight-row decision-log starter to 08-decision-log.csv and keep the exact header.

   ```bash
   Source: labs/resources/08-decision-log-starter.txt
Output header: scenario_id,decision,blocking_guardrail,evidence,proposed_lever,magnitude,approver,cooldown_or_next_check,rollback,status_reason
   ```

8. Ask the AI to apply the saved G-C-A-T-E contract and the policy to each scenario independently. It must test guardrails before performance and may not combine scenarios.

   ```bash
   Apply the complete G-C-A-T-E contract in C695-campaign-pack/02-agent-prompt-contract.md. For each synthetic scenario return: scenario_id | ELIGIBLE yes/no | decision HOLD/STOP/PROPOSE | blocking guardrail | evidence fields | at most one proposed lever | magnitude | approval needed | next check | rollback | reason.

Apply the written policy exactly. A high ROAS cannot override a tracking error, complaint breach, capacity shortfall, low event volume, cooldown, missing approver, privacy concern, or unsupported claim. Never activate an ad or change a live setting.
   ```

9. Review the eight decisions. SC01 may propose one change up to 10% because it meets the synthetic eligibility rules. SC02-SC08 must HOLD or STOP for their stated tracking, complaint, capacity, volume, cooldown, approver, or claim guardrail.

   ```bash
   If any blocked scenario receives PROPOSE, strengthen the guardrail-first order and rerun all scenarios.
   ```

10. Add the continuous feedback loop and rollback checklist: observe fixed window, validate, diagnose, propose one lever, approve, record before state, apply placeholder, observe cooldown, compare, retain or rollback, and update the learning log.

   ```bash
   Public action, audience creation, ad activation, and spend remain disabled in this lab.
   ```

11. Create 08-course-pack-manifest.md and inventory every expected artifact from 01 through 08. Validate cross-artifact consistency before closing the lab.

   ```bash
   Manifest columns: Artifact | Present | Version or date | Final status | Source or provenance | Owner | Unresolved OWNER TO VERIFY. Cross-check the same customer action, approved offer facts, content IDs, account placeholder, time zone, status vocabulary, rights state, primary metric, guardrails, and human owners across the pack. Resolve inconsistencies or record OWNER TO VERIFY with an owner and next check.
   ```


**Test it**

The runbook must contain campaign, ad-set, and ad decisions; two evidence-led audience roles; a retargeting data map; one-variable creative test; explicit eligibility, magnitude, approval, cooldown, and rollback rules; and eight scenario decisions. Only SC01 may be eligible to PROPOSE, and even that row must require human approval. No row may indicate that a live change was made. The manifest must list every expected 01-to-08 file with presence, version or date, status, provenance, owner, and unresolved OWNER TO VERIFY items; the cross-artifact checks must show no unexplained contradiction.

**Checkpoint for the next lab**

This is the final lab. Keep all eight numbered artifacts, the 08 course-pack manifest, and the decision logs together as the Harbour & Hearth Instagram operations pack. Any unresolved item must remain OWNER TO VERIFY with a named owner and next check before a workplace pilot.

**Troubleshooting**

- The agent recommends budget first: Force the order: validate data, check guardrails, locate the funnel break, then choose one lever.
- Retargeting is described only as 'people who engaged': Add source, rights, eligibility, retention, exclusions, frequency, suppression, and owner.
- Several settings change in one recommendation: Return to the one-lever rule and turn other ideas into later hypotheses, not simultaneous actions.

**Challenge**

Add promotion criteria for moving from recommendation-only to one low-risk reversible automated action, including correction rate, incident-free runs, owner coverage, and automatic rollback evidence.

**Reflection**

Why can a performance-improving recommendation still be the wrong business decision, and which guardrail in your policy catches that case?

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

---


### Recap — Analytics, Ads and Optimisation with AI Agents

You can now:

- LO5: Calculate and interpret Instagram organic and paid metrics, then produce a source-linked dashboard, diagnosis, and bounded next action
- LO6: Design a human-governed Instagram ads and retargeting loop for audience, budget, and creative decisions using evidence, limits, approval, cooldown, and rollback

Carry forward the verified lab checkpoints and resolve any OWNER TO VERIFY items with the named owner before the next topic.

---


## Wrap-Up — From Course Pack to Operating Practice

Your final Instagram operations pack connects strategy, content, scheduling, community care, measurement, advertising, and governed optimisation. Its value comes from the traceable decisions between the files, not from any one AI-generated draft.

**Before using the workflow at work**

- Replace the synthetic brief with an approved business brief and document every authorised data source.
- Validate current Meta interface options, account permissions, objectives, and advertising rules for the intended market.
- Set named owners for brand review, privacy review, publishing, customer escalation, and budget approval.
- Start with draft-and-recommend mode, measure errors and corrections, then expand authority only where evidence supports it.

**Evidence to retain**

- Input version, prompt version, generated variants, reviewer corrections, and approval decision.
- Metric definitions, reporting window, source extract, calculations, and known data limitations.
- Before-and-after campaign settings, reason for change, owner, cooldown, result, and rollback action.

---


## Next Steps

- Re-run the campaign pack with one real, authorised offer while keeping all actions in draft.
- Create a small library of approved brand examples, evidence sources, response templates, and rejection labels.
- Review Meta's current official guidance before changing campaign settings or enabling a new automation.
- Pilot one low-risk workflow for two weeks, track corrections and exceptions, and revise the prompt contract.
- Hold a monthly review of data access, content quality, customer impact, performance thresholds, and rollback readiness.


## Glossary

- **Accounts engaged** — The estimated number of unique accounts that interacted with content in the selected Instagram Insights scope.
- **Ad** — The creative, text, identity, destination, and related tracking shown to an audience.
- **Ad set** — The campaign level where audience, placements, budget, schedule, and performance choices are configured.
- **Agent** — A system that uses a model, instructions, and tools to pursue a multi-step goal within guardrails.
- **Approval gate** — A required human decision before a high-impact action can proceed.
- **Attribution** — The rule used to associate an observed customer action with marketing activity.
- **Campaign** — The top advertising level that contains the objective and one or more ad sets.
- **Conversion rate** — The share of relevant visits or clicks that complete the defined conversion action.
- **CPA** — Cost per acquisition or result: spend divided by the number of defined results.
- **CPC** — Cost per click: spend divided by the selected click count.
- **CPM** — Cost per one thousand impressions: spend divided by impressions, multiplied by 1,000.
- **CTR** — Click-through rate: selected clicks divided by impressions, expressed as a percentage.
- **Guardrail** — A rule, check, permission, or technical control that constrains unsafe or unwanted behaviour.
- **Interaction rate by reach** — Defined in this course as likes, comments, saves, and shares divided by accounts reached, expressed as a percentage.
- **Impression** — One delivery of content or an ad to a screen; the same person can generate multiple impressions.
- **Prompt contract** — Reusable instructions defining goal, inputs, rules, output schema, and escalation behaviour.
- **Reach** — The estimated number of distinct people who saw the content or ad.
- **ROAS** — Return on ad spend: attributed revenue divided by advertising spend.
- **Stop condition** — A defined state that ends or pauses an agentic loop.
- **UGC** — User-generated content: media or words created by a community member; public visibility does not automatically grant reuse permission.
- **Views** — The number of times content was displayed or played in the selected Instagram Insights scope; it may include repeated views.
