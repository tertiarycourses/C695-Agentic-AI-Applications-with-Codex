"""Single source of truth for Agentic AI for Instagram Marketing (C695)."""

# ------------------------------------------------------------------ metadata
TITLE = "Agentic AI for Instagram Marketing (C695)"
SHORT_TITLE = "Agentic AI for Instagram Marketing (C695)"
COURSE_CODE = "C695"
VERSION = "v1.0"
VERSION_DATE = "3 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Course Trainer"
TRAINER_CERT = "Digital marketing and applied AI practitioner"
TRAINER_DELIVERS = "Instagram marketing, digital advertising, analytics, and applied AI workflows"
DAYS = 2
MODE = "Instructor-led, concept-first learning with connected hands-on labs"

# The advertised 15 instructional hours are delivered as 7.5 instructional
# hours per day. Each day also contains two 15-minute tea breaks, so the Lesson
# Plan totals 480 scheduled minutes excluding lunch.
DAY_MINUTES = 480
INSTRUCTIONAL_HOURS = 15
CLOCK_HOURS = 16
DAILY_TIMING = "9:00 am - 6:00 pm (1-hour lunch; two 15-minute tea breaks)"
DARK_THEME = False

REJOIN_PATH = [
    ("Before Lab 2", "Complete Lab 1 or reconstruct 01-foundation-and-readiness.md from the brand brief and audience signals; verify the five-stage journey, twelve readiness checks, and approval gates."),
    ("Before Labs 3–8", "Complete Lab 2 or reconstruct and retest 02-agent-prompt-contract.md; its G-C-A-T-E evidence, privacy, rights, and approval rules remain mandatory."),
    ("Before Lab 4", "Use 03-instagram-content-kit-starter.md to reconstruct seven scored content IDs; only READY FOR HUMAN REVIEW items may enter the calendar."),
    ("Before Lab 6", "Reconstruct the Lab 5 intent taxonomy, response queue, minimum-data lead schema, and named escalation owners."),
    ("Before Lab 7", "Confirm artifacts 01–06 are present and their customer action, guardrails, content IDs, status vocabulary, rights state, and owners do not conflict."),
    ("Before Lab 8", "Confirm artifacts 01–07 are present. Use the Lab 7 workbook and report as the evidence baseline, then complete the final 01-to-08 manifest."),
]

ICE_BREAKER = [
    "Your name, role, and the Instagram Professional account or business context you support.",
    "One Instagram content, community, or reporting task that currently takes too much time.",
    "One public-facing or budget decision you would never allow an AI agent to make without approval.",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain AI agents and map an Instagram customer journey, account readiness, tools, prompts, evidence, and human approval gates.",
    "LO2: Generate an on-brand Instagram content system with captions, hashtags, image and Reels briefs, a calendar, and a controlled publishing workflow.",
    "LO3: Design a governed engagement workflow for comments, direct messages, lead capture, follow-up, reviews, and user-generated content.",
    "LO4: Apply privacy, copyright, platform, brand, and escalation rules to Instagram content and community-management decisions.",
    "LO5: Calculate and interpret Instagram organic and paid metrics, then produce an evidence-linked performance report and dashboard.",
    "LO6: Design an AI-assisted Instagram ads and retargeting optimisation loop for audience, budget, and creative decisions with human authority.",
]
LO_TITLES = [
    "Agent Foundations",
    "Content System",
    "Community Workflow",
    "Responsible Practice",
    "Analytics",
    "Ads Optimisation",
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(
        num=1,
        code="01",
        title="Foundations of Agentic AI for Instagram Marketing",
        subtitle="agents and workflows | tool choices | Professional account readiness | prompting | customer journey",
        concepts=[
            ("Outcome before output", "Start with a business result and customer action, not a request to 'make posts'."),
            ("Organic and paid roles", "Organic content builds attention and proof; paid delivery buys controlled reach and learning."),
            ("Agentic loop", "An agent plans, uses tools, checks evidence, and iterates until a stop condition is reached."),
            ("Evidence boundary", "Facts, customer data, and performance numbers need provenance; unknowns remain labelled assumptions."),
            ("Prompt contract", "Role, goal, context, inputs, rules, output schema, and review criteria make work repeatable."),
            ("Audience hypothesis", "A segment is a testable need and behaviour pattern, not a stereotype or invented demographic."),
            ("Human authority", "Publishing, spend, targeting changes, and sensitive replies remain approval-controlled actions."),
            ("Audit trail", "Save the brief, inputs, versions, approvals, and final decision so the workflow can be reviewed."),
        ],
        teaching=[
            dict(
                title="Instagram Marketing as a Connected System",
                kind="flow",
                kicker="TOPIC 01 · SYSTEM VIEW",
                visual=["Business objective", "Audience need", "Useful content", "Organic or paid delivery", "Measured customer action"],
                paragraphs=[
                    "Instagram marketing is a system, not a sequence of unrelated posts. A useful plan begins with a business objective, identifies the customer action that would demonstrate progress, then chooses content and delivery methods that make that action more likely. Organic posts, Reels, Stories, profile information, community conversations, and paid ads should therefore share one message hierarchy and one measurement plan.",
                    "The same content can perform different jobs at different stages. A how-to video may build awareness, a customer proof post may reduce uncertainty, and a limited offer may invite a conversion. An AI agent can help coordinate these jobs, but it cannot decide what success means for the business. The marketer supplies the objective, evidence, constraints, and final judgement.",
                ],
            ),
            dict(
                title="From Generative AI to an Agentic Workflow",
                kind="compare",
                kicker="TOPIC 01 · WHAT MAKES IT AGENTIC",
                left_title="Single AI task",
                right_title="Agentic workflow",
                left=[
                    "One prompt produces one draft",
                    "The user manually supplies every input",
                    "No persistent state or explicit stop rule",
                    "Quality depends on one response",
                ],
                right=[
                    "A goal is decomposed into multiple steps",
                    "Tools retrieve data or create controlled outputs",
                    "State, checks, retries, and stop conditions are explicit",
                    "A person approves high-impact actions",
                ],
                paragraphs=[
                    "Generative AI creates text, images, or analysis from a prompt. An agentic workflow goes further: it manages a multi-step goal, selects or calls tools, observes results, and decides what to do next within defined limits. A content assistant that drafts one caption is useful, but it becomes agentic only when it can work through a plan such as research, draft, check, revise, route for approval, and record the outcome.",
                    "Not every task needs autonomy. Deterministic work such as applying a known naming convention is usually safer as a checklist or rule. Agentic reasoning is more valuable when inputs are unstructured, trade-offs are contextual, or the path changes after new evidence. Begin with the smallest useful loop and add tools only when each tool has a clear purpose and risk level.",
                ],
            ),
            dict(
                title="The Six-Part Marketing Agent",
                kind="tiles",
                kicker="TOPIC 01 · AGENT ANATOMY",
                visual=[
                    ("Goal", "The result, customer action, time horizon, and success threshold."),
                    ("Context", "Brand, offer, audience evidence, channel role, and constraints."),
                    ("Instructions", "Decision rules, required steps, output format, and escalation logic."),
                    ("Tools", "Approved data sources, content tools, calendars, and reporting surfaces."),
                    ("Memory", "Briefs, past variants, decisions, and lessons that should persist."),
                    ("Checks", "Brand, factual, privacy, policy, and performance validation before action."),
                ],
                paragraphs=[
                    "A reliable marketing agent needs more than a clever prompt. Its goal defines the finish line. Context explains the brand and audience. Instructions describe the route and exceptions. Tools determine what the agent may read or change. Memory preserves only the state needed for the next decision. Checks test whether the result is safe and useful before the workflow proceeds.",
                    "A weakness in any one part propagates. If the goal says 'increase engagement' but does not name the customer action or time window, the agent may optimise reactions that have no business value. If the tools include a publishing action without an approval gate, a drafting error becomes a public error. Design the system before choosing the model.",
                ],
            ),
            dict(
                title="Choose Tools by Role, Permission, and Risk",
                kind="tiles",
                kicker="TOPIC 01 Â· TOOL OVERVIEW",
                visual=[
                    ("ChatGPT or Claude", "Develop briefs, structured drafts, critique, classification, and analysis from approved inputs."),
                    ("Image tools", "Explore visual concepts and storyboards; retain provenance and verify product truth."),
                    ("Meta Business Suite", "Review profiles, drafts, Planner, Inbox, and insights with account-based permissions."),
                    ("n8n", "Connect triggers, data, AI steps, review gates, logs, retries, and bounded actions."),
                    ("Spreadsheets", "Hold calendars, response queues, metric definitions, and decision logs in a reviewable form."),
                    ("Instagram API", "Supports approved professional-account publishing, insights, comments, and messaging use cases subject to permissions and limits."),
                ],
                paragraphs=[
                    "A tool belongs in the workflow only when its role is clear. AI assistants interpret and draft; spreadsheets store structured state; Meta surfaces expose account operations; workflow automation coordinates steps. The Instagram API can enable production integrations, but it needs a Professional account, an app, permissions, tokens, and current platform review. These are operational requirements, not details to improvise inside a prompt.",
                    "Rate each tool action by impact and reversibility. Reading a synthetic brief is low risk. Drafting a caption is medium risk because it still needs review. Publishing, replying publicly, handling personal data, changing an audience, or changing spend is high risk. High-risk actions require the named account owner and a recorded approval.",
                ],
            ),
            dict(
                title="Professional Account and Automation Readiness",
                kind="flow",
                kicker="TOPIC 01 Â· SETUP CHECK",
                visual=["Professional account", "Correct business identity", "Linked assets and roles", "Approved permissions", "Draft-mode connection test"],
                paragraphs=[
                    "Instagram Professional accounts are Business or Creator accounts. Professional tools include the dashboard and insights, while some automation paths depend on how the account, Meta assets, app, and permissions are configured. Connecting a Facebook Page can support cross-app management in Meta Business Suite, but current requirements vary by feature and login method, so the owner should verify the official setup for the intended integration.",
                    "Readiness means more than being able to log in. Confirm the account identity, owner, recovery method, authorised roles, connected assets, time zone, data sources, allowed actions, and revoke path. Test with a draft or read-only action first. Never place an access token in a prompt, screenshot, lab file, or public repository.",
                ],
            ),
            dict(
                title="Objective, Customer Action, and KPI Chain",
                kind="flow",
                kicker="TOPIC 01 · MEASUREMENT LOGIC",
                visual=["Business result", "Marketing objective", "Customer action", "Primary KPI", "Guardrail metric"],
                paragraphs=[
                    "A measurement chain prevents vanity metrics from becoming the strategy. The business result might be breakfast-box revenue. The marketing objective could be qualified pre-orders. The customer action is a completed order. The primary KPI may be cost per purchase or return on ad spend, while a guardrail could be refund rate, negative feedback, or response quality.",
                    "Choose the Meta campaign objective that most closely matches the larger business goal and the event that can be measured reliably. An awareness objective is not a cheaper substitute for a sales objective when sales are the real decision criterion. Equally, a sales objective is weak when the business has no trustworthy conversion signal. The objective, data signal, and KPI must agree.",
                ],
            ),
            dict(
                title="Audience Evidence Before Targeting",
                kind="tiles",
                kicker="TOPIC 01 · AUDIENCE DESIGN",
                visual=[
                    ("Observed", "Existing customer questions, purchases, site behaviour, and Instagram interactions."),
                    ("Declared", "Needs and preferences people voluntarily shared through interviews or forms."),
                    ("Inferred", "A labelled hypothesis derived from patterns, never presented as fact."),
                    ("Excluded", "Sensitive traits, unjustified personal data, and segments the offer should not reach."),
                    ("Testable", "A need, trigger, barrier, message angle, and measurable response."),
                    ("Revisable", "A segment changes when evidence contradicts the original hypothesis."),
                ],
                paragraphs=[
                    "Audience research should separate what is known from what is inferred. Observed data may show that weekday pre-orders peak before 9 am. Customer interviews may reveal that convenience matters more than variety. An AI model can propose segment hypotheses, but it must label them as hypotheses and cite the supplied evidence instead of manufacturing demographic detail.",
                    "Meta's delivery systems can work with broad audiences, audience suggestions, and strict controls such as location, minimum age, language, and exclusions. The marketer's job is to provide a commercially meaningful signal without narrowing the audience through stereotypes. Any customer list requires the organisation to have the necessary rights, permissions, and lawful basis for its use.",
                ],
            ),
            dict(
                title="The Prompt Contract",
                kind="flow",
                kicker="TOPIC 01 · REUSABLE INSTRUCTIONS",
                visual=["Role and goal", "Grounded inputs", "Decision rules", "Output schema", "Review and escalation"],
                paragraphs=[
                    "A prompt contract turns an informal request into an operating instruction. It tells the agent who it is helping, what outcome matters, which inputs are authoritative, which choices are allowed, and exactly what form the result must take. A structured output such as a table with evidence, assumptions, risks, and next action is easier to review than a persuasive paragraph.",
                    "Include failure behaviour. The agent should say 'insufficient evidence' when a required input is missing, request clarification when two constraints conflict, and stop when the next action would publish, spend money, change targeting, or expose personal data. These rules reduce silent guessing and make human review faster.",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="AI-Powered Content Creation and Scheduling",
        subtitle="posts, captions and hashtags | images and Reels | content calendar agent | scheduling | brand consistency",
        concepts=[
            ("One message hierarchy", "Audience tension, promise, proof, offer, and action align every content format."),
            ("Content pillars", "Repeatable themes create variety without losing strategic focus."),
            ("Hook with relevance", "Earn attention by naming a useful tension, not by exaggerating or withholding truth."),
            ("Proof before pressure", "Specific evidence reduces uncertainty more effectively than louder claims."),
            ("Format follows job", "Image, carousel, and video choices should match the message and stage of awareness."),
            ("Brand voice rules", "Observable language patterns are easier for AI to follow than vague adjectives."),
            ("Variant discipline", "Change one meaningful variable at a time so later performance can teach you something."),
            ("Human creative review", "Check accuracy, rights, representation, readability, and platform fit before use."),
        ],
        teaching=[
            dict(
                title="The Instagram Message Hierarchy",
                kind="flow",
                kicker="TOPIC 02 · MESSAGE DESIGN",
                visual=["Audience tension", "Relevant promise", "Reason to believe", "Offer or next step", "Clear action"],
                paragraphs=[
                    "A message hierarchy is the stable logic underneath many creative executions. It begins with a real audience tension, states a relevant promise, supplies a reason to believe, presents the offer or next step, and asks for one clear action. When this logic is strong, a post, carousel, short video, and ad can feel different while still telling the same story.",
                    "An AI agent should not invent proof. Give it approved product facts, testimonials with permission, delivery details, prices, and limitations. Ask it to mark any unsupported claim with a placeholder. The marketer then decides whether evidence exists or the claim should be removed.",
                ],
            ),
            dict(
                title="Content Pillars and the Customer Journey",
                kind="tiles",
                kicker="TOPIC 02 · EDITORIAL SYSTEM",
                visual=[
                    ("Teach", "Answer a useful question and build problem awareness."),
                    ("Show", "Demonstrate the product, process, or customer experience."),
                    ("Prove", "Use evidence, reviews, comparisons, or behind-the-scenes detail."),
                    ("Invite", "Present an offer and make the next action unmistakable."),
                    ("Engage", "Ask a meaningful question or respond to community signals."),
                    ("Learn", "Use performance and comments to refine the next content cycle."),
                ],
                paragraphs=[
                    "Content pillars are repeatable strategic themes, not arbitrary labels. A local bakery might teach breakfast-planning tips, show how the box is packed, prove freshness with process details, and invite pre-orders. Each pillar has a job in the customer journey and a set of evidence it may use.",
                    "A calendar balances these jobs across time. It also records format, audience, message angle, call to action, owner, status, and learning question. The learning question is what makes the calendar agent-ready: every item declares what the team hopes to discover, not only what it plans to publish.",
                ],
            ),
            dict(
                title="Brand Voice as Observable Rules",
                kind="compare",
                kicker="TOPIC 02 · CONSISTENCY",
                left_title="Weak instruction",
                right_title="Operational rule",
                left=[
                    "Sound friendly and premium",
                    "Make it engaging",
                    "Use our usual tone",
                    "Avoid sounding robotic",
                ],
                right=[
                    "Use warm, direct sentences of 8-18 words",
                    "Open with a specific customer situation",
                    "Use Singapore English naturally; avoid forced slang",
                    "One helpful detail before one invitation",
                ],
                paragraphs=[
                    "Brand adjectives such as friendly, bold, or premium are too abstract on their own. Translate them into observable rules: sentence length, point of view, vocabulary, rhythm, humour boundaries, words to use, words to avoid, and examples that demonstrate the tone. These rules can be evaluated consistently by a person or a checking agent.",
                    "Examples are powerful but should not become a copying target. Give two or three representative examples and explain why they work. Add negative examples that show exaggeration, pressure, unexplained jargon, or tone that does not fit the brand. This creates a usable boundary around creative variation.",
                ],
            ),
            dict(
                title="Caption and Hashtag System",
                kind="flow",
                kicker="TOPIC 02 · COPY SYSTEM",
                visual=["Specific hook", "Useful value", "Credible proof", "Single call to action", "Relevant hashtag set"],
                paragraphs=[
                    "An Instagram caption should earn attention, deliver useful meaning, support the visual, and invite one next action. Relevance is not sensationalism: a useful hook names a situation, question, or benefit the intended audience recognises. Add approved proof and offer detail only when the supplied evidence supports them.",
                    "Hashtags are descriptive discovery labels, not a substitute for message strategy. Build a small relevant set around brand, product, use case, place, and campaign, then review ambiguity and unintended associations. An agent should explain why each hashtag fits, remove duplicates or risky terms, and never promise reach from hashtag volume alone.",
                ],
            ),
            dict(
                title="Creative System: Image, Carousel, Stories, and Reels",
                kind="tiles",
                kicker="TOPIC 02 · CREATIVE CHOICE",
                visual=[
                    ("Single image", "One idea, one focal point, fast recognition, strong offer or proof."),
                    ("Carousel", "A sequence, comparison, product range, or step-by-step story."),
                    ("Stories", "Timely updates, interaction prompts, reminders, and sequential moments."),
                    ("Reels", "Motion, demonstration, personality, transformation, or process."),
                    ("First-frame clarity", "Make the subject and value understandable without sound; use simple composition and safe cropping."),
                    ("Rights and truth", "Use authorised assets; review generated details, product accuracy, and implied claims."),
                ],
                paragraphs=[
                    "Format should follow the communication job. A single image works when one focal message is enough. A carousel supports sequence, comparison, or multiple proof points. Short video is useful when motion, demonstration, or personality carries meaning. The first frame should communicate subject and relevance even without sound.",
                    "AI image generation accelerates exploration, but it introduces review duties. Check hands, text, packaging, locations, product attributes, cultural details, and any implied endorsement. Keep asset provenance and licence information. Generated creative is a draft until the marketer verifies that it truthfully represents the offer.",
                ],
            ),
            dict(
                title="Content Calendar Agent and Publishing Control",
                kind="flow",
                kicker="TOPIC 02 Â· CALENDAR TO ACTION",
                visual=["Approved brief", "Calendar proposal", "Asset and caption checks", "Human approval", "Schedule or publish", "Log outcome"],
                paragraphs=[
                    "A content calendar agent converts strategy into a reviewable queue. Each row should state date, Singapore time, format, customer-journey job, content pillar, hook, approved facts, asset, caption, hashtags, call to action, owner, status, and learning question. The agent may find gaps and propose a balance; it should not silently invent offer details or publish because a row is complete.",
                    "Scheduling is an action boundary. Meta Business Suite or an approved integration can place content into a queue, but the workflow should validate account identity, time zone, asset readiness, final copy, destination, rights, and approval. A failed schedule should create an exception record and hand-off, not an uncontrolled retry loop that creates duplicate posts.",
                ],
            ),
            dict(
                title="Content Quality Gate",
                kind="flow",
                kicker="TOPIC 02 · BEFORE APPROVAL",
                visual=["Grounded facts", "Brand fit", "Audience value", "Creative and rights check", "Objective and action match"],
                paragraphs=[
                    "A content quality gate gives reviewers a shared standard. First verify every fact against an approved source. Then check brand voice, audience usefulness, readability, visual truth, asset rights, and the connection between message, offer, destination, and objective. A piece can be attractive and still fail if it asks for the wrong action.",
                    "Record the reason for rejection or revision. These labels become learning data for the next prompt version: unsupported claim, unclear action, off-brand tone, weak proof, visual mismatch, or policy risk. The agent improves when feedback is structured and specific, not when the reviewer simply says 'make it better'.",
                ],
            ),
        ],
    ),
    dict(
        num=3,
        code="03",
        title="Automating Engagement and Community Management",
        subtitle="comments and direct messages | lead capture | personalised responses | reviews and UGC | privacy and responsible AI",
        concepts=[
            ("Intent before tone", "Identify what the person needs and the risk of the request before writing a polished reply."),
            ("Public or private", "Keep general information public; move order, contact, payment, and sensitive details to an approved private channel."),
            ("Minimum data", "Capture only the fields needed for the stated follow-up and keep raw personal data out of AI prompts."),
            ("Consent and purpose", "Explain why information is requested and use it only for the authorised purpose and retention period."),
            ("Personalise from context", "Adapt approved facts and language without inferring sensitive traits or inventing familiarity."),
            ("Escalate impact", "Safety, allergy, payment, complaint, privacy, legal, and order-change cases need a named human owner."),
            ("UGC requires permission", "A public mention is not automatic permission to reuse a person's image, words, name, or likeness."),
            ("Learn from labels", "Store intent, risk, decision, correction, and outcome so rules improve without retaining unnecessary content."),
        ],
        teaching=[
            dict(
                title="Engagement Is a Service Workflow",
                kind="flow",
                kicker="TOPIC 03 · COMMUNITY SYSTEM",
                visual=["Comment or message", "Identify intent", "Retrieve approved facts", "Draft or escalate", "Human review", "Reply and log"],
                paragraphs=[
                    "Comments and direct messages are not merely engagement counts; they are service interactions with different expectations and risks. A useful workflow identifies the intent, checks whether the answer exists in an approved source, decides whether the conversation should remain public, and routes high-impact cases to a person. Fast wording is less valuable than a correct route.",
                    "Automation should begin with draft-and-recommend mode. Routine questions such as collection time or an approved link may receive a suggested response. Order changes, refunds, duplicate charges, safety concerns, threats, harassment, or requests involving personal details should stop the automated path. The owner decides the response and channel.",
                ],
            ),
            dict(
                title="Intent and Risk Routing",
                kind="tiles",
                kicker="TOPIC 03 · TRIAGE",
                visual=[
                    ("Informational", "Approved hours, location, product contents, process, or link; draft from the knowledge source."),
                    ("Commercial", "Product fit or availability; answer approved facts and invite one authorised next step."),
                    ("Lead", "A person asks for follow-up; request the minimum fields through an approved private route."),
                    ("Service", "An order-specific request; authenticate and hand off to the service owner."),
                    ("Sensitive", "Health, payment, privacy, legal, or safety content; stop and escalate immediately."),
                    ("Abuse or spam", "Apply documented moderation rules and preserve context for review."),
                ],
                paragraphs=[
                    "Intent describes the job to be done; risk describes the consequence of getting it wrong. The same words can have different risk depending on context. 'Can I change my order?' is not answered by generating a friendly promise because the agent cannot verify identity, stock, payment, or fulfilment. It is routed to the order owner with a neutral acknowledgement.",
                    "A router should return a structured record: intent, confidence, risk tier, approved source, public or private route, response template, owner, and reason. When confidence is low or two rules conflict, the safe result is REVIEW, not a forced guess.",
                ],
            ),
            dict(
                title="Lead Capture and Follow-Up Automation",
                kind="flow",
                kicker="TOPIC 03 · LEAD HAND-OFF",
                visual=["Clear invitation", "Purpose notice", "Minimum fields", "Consent or lawful basis", "Assigned owner", "Timed follow-up and deletion"],
                paragraphs=[
                    "A lead workflow should state what will happen before asking for information. If a person requests a corporate breakfast quote, the business may need a contact name, work email, approximate quantity, date, and consent to follow up. It does not need age, home address, personal interests, or a full message transcript. Use an approved form or secured business system rather than collecting identifiers inside a model conversation.",
                    "The hand-off record needs an owner, service-level target, status, and retention rule. Follow-up messages should reflect the person's request and approved offer facts, not inferred personal traits. If consent is withdrawn, the workflow must stop future follow-up and route the deletion or suppression request appropriately.",
                ],
            ),
            dict(
                title="Personalised Responses and Escalation Rules",
                kind="compare",
                kicker="TOPIC 03 · HUMAN BOUNDARY",
                left_title="Safe personalisation",
                right_title="Escalate or refuse",
                left=[
                    "Use the stated question and approved context",
                    "Mirror formality without imitating identity",
                    "Offer one relevant authorised next step",
                    "Acknowledge uncertainty and hand off clearly",
                ],
                right=[
                    "Do not infer health, wealth, ethnicity, or vulnerability",
                    "Do not confirm refunds, order changes, or compensation",
                    "Do not request credentials or sensitive data in public",
                    "Do not argue about safety, privacy, legal, or crisis claims",
                ],
                paragraphs=[
                    "Personalisation is the use of relevant supplied context, not hidden inference. A safe reply can acknowledge that the person needs collection before 9 am and provide the approved window. It should not infer their job, urgency, or ability to pay. Keep the response proportional to what the person actually disclosed.",
                    "Escalation rules name the trigger, immediate holding message, owner, required context, and response clock. They also define what the agent must not say. Clear negative rules matter because a fluent apology can accidentally admit liability, promise an outcome, or expose an order detail.",
                ],
            ),
            dict(
                title="Reviews and User-Generated Content",
                kind="flow",
                kicker="TOPIC 03 · COMMUNITY RIGHTS",
                visual=["Discover", "Verify context", "Ask permission", "Record scope", "Edit transparently", "Publish with attribution or decline"],
                paragraphs=[
                    "A review or user-generated post can provide powerful social proof, but visibility is not permission. Before reuse, verify the source, ask the rights holder for clear permission, state the channel and duration, record any approved edits, and respect withdrawal where applicable. Do not fabricate testimonials, ratings, customer identities, or product experiences.",
                    "AI can help organise a permission queue, flag potential rights issues, propose a reply, or create a neutral UGC brief. A person should review claims, representation, context, attribution, and whether the content includes other people, music, logos, locations, or personal information that the original poster may not control.",
                ],
            ),
            dict(
                title="Privacy, Copyright, and Responsible AI Gate",
                kind="tiles",
                kicker="TOPIC 03 · BEFORE ANY REPLY OR REUSE",
                visual=[
                    ("Purpose", "Is the use appropriate, explained, and limited to the intended service or marketing purpose?"),
                    ("Data", "Can identifiers, message content, or metadata be minimised, masked, or avoided?"),
                    ("Rights", "Do we have authority to use the image, music, words, name, likeness, and brand assets?"),
                    ("Truth", "Are claims, urgency, endorsements, and product details supported by approved evidence?"),
                    ("Fairness", "Does the output avoid stereotypes, exclusion, manipulation, and unsupported sensitive inference?"),
                    ("Accountability", "Is there a reviewer, decision log, correction path, and disable switch?"),
                ],
                paragraphs=[
                    "Responsible AI is an operating discipline. Apply privacy and rights checks to inputs, not only to final copy. A model should not receive a raw message export simply because it can summarise it. Minimise the data, use synthetic records in training, restrict access, and retain only what supports the documented purpose and decision.",
                    "When a public error occurs, pause the automation, preserve the relevant log securely, notify the owner, correct the public information, and address the affected person through the appropriate channel. Then fix the source, rule, permission, or prompt and test the revised route with synthetic edge cases before restoring operation.",
                ],
            ),
        ],
    ),
    dict(
        num=4,
        code="04",
        title="Analytics, Ads and Optimisation with AI Agents",
        subtitle="Instagram Insights | reports and dashboards | ads | audience, budget and creative | retargeting | feedback loops",
        concepts=[
            ("Define before calculating", "Every metric needs a source, numerator, denominator, window, scope, and known limitation."),
            ("Separate reach from views", "Unique accounts and repeated displays answer different delivery questions."),
            ("Follow the funnel", "Content discovery, interaction, profile action, site action, conversion, and value are different transitions."),
            ("Report evidence", "A narrative claim must point to a metric, period, comparison, source row, and uncertainty."),
            ("Ads hierarchy", "Campaign objective, ad-set audience and budget, and ad creative must agree with the customer action."),
            ("Diagnose before changing", "Validate data and locate the weak transition before choosing a lever."),
            ("Retarget responsibly", "Use authorised signals, exclusions, retention, frequency, and customer expectations."),
            ("One controlled change", "Set a hypothesis, approval, observation window, guardrails, and rollback before iterating."),
        ],
        teaching=[
            dict(
                title="Instagram Insights and the Metric Tree",
                kind="tiles",
                kicker="TOPIC 04 · MEASUREMENT",
                visual=[
                    ("Delivery", "Views, impressions where available, accounts reached, and follower or non-follower distribution."),
                    ("Interaction", "Likes, comments, saves, shares, replies, and accounts engaged."),
                    ("Intent", "Profile visits, link clicks, website taps, messages, and lead actions where configured."),
                    ("Conversion", "Completed orders or leads from an authorised commerce or analytics source."),
                    ("Paid", "Spend, result count, cost per result, CPM, CTR, CPC, CPA, and attributed value."),
                    ("Guardrails", "Negative feedback, complaint rate, rights concerns, tracking health, and fulfilment capacity."),
                ],
                paragraphs=[
                    "Instagram Insights are available for Professional accounts and expose account and content performance for defined timeframes. Views can include repeated displays, while accounts reached estimates unique accounts. Interactions count actions; accounts engaged estimate unique accounts that interacted. Metric names and availability can change, so preserve the export date, selected window, account scope, and definition shown in the interface.",
                    "Useful derived rates require a deliberate denominator. Interaction rate by reach = interactions / accounts reached × 100. Save rate by reach = saves / reach × 100. Link click-through by reach = link clicks / reach × 100. For paid data, CTR, CPC, CPA, and ROAS use the selected reporting definitions and attribution window. Never silently mix organic and paid data.",
                ],
            ),
            dict(
                title="Automated Reports and Decision Dashboards",
                kind="flow",
                kicker="TOPIC 04 · EVIDENCE TO DECISION",
                visual=["Validate extract", "Calculate defined metrics", "Compare to baseline", "Explain driver candidates", "Recommend one decision", "Log caveats"],
                paragraphs=[
                    "An automated report is trustworthy only when it preserves the data contract. Validate column names, types, duplicates, missing values, date coverage, account identity, and whether paid effects are included. Then calculate metrics from documented formulas. The narrative should distinguish observations from hypotheses and state when the data cannot support a conclusion.",
                    "A compact dashboard should answer: what happened, where in the funnel, compared with what, what might explain it, and what action is justified. Include primary outcomes, leading indicators, content-format or creative cuts, guardrails, and an exception panel. A chart without a decision question is decoration; a recommendation without source evidence is speculation.",
                ],
            ),
            dict(
                title="AI-Assisted Instagram Ads Campaigns",
                kind="tiles",
                kicker="TOPIC 04 · CAMPAIGN STRUCTURE",
                visual=[
                    ("Campaign", "Choose the objective that matches the larger business goal and experiment context."),
                    ("Ad set", "Define audience role, conversion location, event, budget, schedule, placements, and exclusions."),
                    ("Ad", "Align identity, format, creative, primary text, destination, and tracking."),
                    ("Preflight", "Verify account, permissions, event, destination, claims, rights, naming, and approval."),
                    ("Agent role", "Draft structures, detect contradictions, calculate options, and recommend; do not activate spend."),
                    ("Human role", "Own objective, data rights, budget, final creative, activation, monitoring, and rollback."),
                ],
                paragraphs=[
                    "Meta Ads Manager coordinates Instagram delivery through campaign, ad-set, and ad decisions. The objective tells the system which result to pursue. The optimisation event must be observable and sufficiently trustworthy. Audience, budget, schedule, placements, creative, destination, and tracking must form one coherent path to the desired customer action.",
                    "AI can turn an approved brief into a blueprint and preflight checklist, compare budget scenarios, or flag contradictions. It should leave account IDs, payment methods, verified event status, customer-list eligibility, and live settings as UNKNOWN until an authorised owner supplies them. Activation and spend changes remain human decisions.",
                ],
            ),
            dict(
                title="Audience, Budget, and Creative Optimisation",
                kind="compare",
                kicker="TOPIC 04 · CHOOSE THE LEVER",
                left_title="Evidence pattern",
                right_title="Bounded investigation",
                left=[
                    "Delivery cost or frequency changes",
                    "Healthy delivery but weak qualified action",
                    "Strong click or profile action, weak conversion",
                    "One creative angle consistently differs",
                ],
                right=[
                    "Inspect audience pressure, placement, seasonality, and auction context",
                    "Inspect creative relevance, promise, format, and call to action",
                    "Inspect destination, offer, event quality, friction, and attribution",
                    "Run a one-variable test with stable audience, budget, and window",
                ],
                paragraphs=[
                    "Optimisation begins with data validation and a funnel diagnosis. Budget is not the default fix for weak creative, broken tracking, a poor destination, or capacity constraints. Audience, budget, and creative are different levers; change one meaningful variable at a time so the result teaches the team something.",
                    "Define a minimum evidence condition, maximum allowed change, named approver, cooldown, and rollback. The agent should be able to recommend HOLD when event volume is low, a recent edit has not stabilised, a guardrail fails, or the suspected cause remains untested.",
                ],
            ),
            dict(
                title="Retargeting by Customer State",
                kind="flow",
                kicker="TOPIC 04 · RELEVANT RE-ENGAGEMENT",
                visual=["Authorised signal", "Customer state", "Useful next message", "Exclusions and frequency", "Conversion or suppression"],
                paragraphs=[
                    "Retargeting reconnects with people who have already shown an authorised signal, such as viewing a product page, engaging with eligible content, or joining an approved customer list. The message should fit the person's likely stage without implying surveillance or knowledge they did not expect the business to use.",
                    "Document the source, rights or lawful basis, retention window, exclusions, frequency control, and suppression after conversion. Do not upload a list simply because it exists. A customer list, website event, video view, and message interaction carry different expectations and technical requirements. The owner verifies eligibility before audience creation.",
                ],
            ),
            dict(
                title="Continuous Improvement with a Governed Feedback Loop",
                kind="flow",
                kicker="TOPIC 04 · LEARN SAFELY",
                visual=["Observe", "Validate", "Diagnose", "Propose", "Approve and test", "Measure, log, or rollback"],
                paragraphs=[
                    "A continuous-improvement loop is not permission for continuous autonomous change. It observes a fixed window, validates the data, diagnoses the weakest transition, proposes one reversible action, waits for approval, and records the result. Stop conditions include tracking errors, low event volume, complaints, privacy concerns, unsupported claims, capacity limits, and an unavailable owner.",
                    "Scale only after the workflow produces stable evidence and low correction rates. Teams can scale creative throughput, reporting coverage, campaign budget, or workflow authority, but should expand one dimension at a time. If a guardrail fails, return to the last stable configuration, preserve the decision log, and revise the prompt, policy, or tool before another pilot.",
                ],
            ),
        ],
    ),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Agent foundations, prompting, Instagram content, and scheduling",
    2: "Community automation, analytics, ads, and governed optimisation",
}

# ------------------------------------------------------------------ schedule
def SCHEDULE(lab_titles):
    return {
        1: (DAY_THEMES[1], [
            ("9:00", "9:20", 20, "admin", "Welcome, outcomes, learning approach, and campaign scenario"),
            ("9:20", "10:10", 50, "topic", "Topic 1 — AI agents, workflows, customer journey, and tool roles"),
            ("10:10", "10:25", 15, "break", "Tea break"),
            ("10:25", "11:10", 45, "topic", "Topic 1 — Professional account readiness, prompting, evidence, and approval gates"),
            ("11:10", "12:00", 50, "lab", "Hands-on: " + lab_titles([1])),
            ("12:00", "13:00", 60, "lab", "Hands-on: " + lab_titles([2])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:00", 60, "topic", "Topic 2 — posts, captions, hashtags, content pillars, and brand voice"),
            ("15:00", "15:45", 45, "lab", "Hands-on: " + lab_titles([3])),
            ("15:45", "16:00", 15, "break", "Tea break"),
            ("16:00", "16:40", 40, "topic", "Topic 2 — images, Reels, calendar agents, scheduling, and quality gates"),
            ("16:40", "17:40", 60, "lab", "Hands-on: " + lab_titles([4])),
            ("17:40", "18:00", 20, "recap", "Day 1 recap, artifact checkpoint, and questions"),
        ]),
        2: (DAY_THEMES[2], [
            ("9:00", "9:15", 15, "recap", "Day 1 retrieval practice and campaign-pack checkpoint"),
            ("9:15", "10:15", 60, "topic", "Topic 3 — comments, direct messages, lead capture, and response routing"),
            ("10:15", "10:30", 15, "break", "Tea break"),
            ("10:30", "11:15", 45, "topic", "Topic 3 — escalation, reviews, UGC rights, privacy, and responsible AI"),
            ("11:15", "12:05", 50, "lab", "Hands-on: " + lab_titles([5])),
            ("12:05", "13:00", 55, "lab", "Hands-on: " + lab_titles([6])),
            ("13:00", "14:00", 60, "lunch", "Lunch break"),
            ("14:00", "15:00", 60, "topic", "Topic 4 — Instagram Insights, performance reports, and dashboards"),
            ("15:00", "15:45", 45, "lab", "Hands-on: " + lab_titles([7])),
            ("15:45", "16:00", 15, "break", "Tea break"),
            ("16:00", "16:45", 45, "topic", "Topic 4 — ads, audience, budget, creative, retargeting, and feedback loops"),
            ("16:45", "17:40", 55, "lab", "Hands-on: " + lab_titles([8])),
            ("17:40", "18:00", 20, "recap", "Course recap, implementation plan, and next steps"),
        ]),
    }

# ------------------------------------------------------------------ optional deck framing
COURSE_OVERVIEW = dict(
    section_title="Agentic Instagram Marketing Operating System",
    concepts_title="The Five Decisions Every Workflow Must Preserve",
    concepts=[
        ("Why", "Which business result and customer action matter?"),
        ("Who", "Which evidence-backed audience need are we serving?"),
        ("What", "Which promise, proof, offer, and creative communicate value?"),
        ("Where", "Should the message use organic, paid, or community delivery?"),
        ("Next", "Which metric and rule determine the next controlled action?"),
    ],
    framework_title="The G-C-A-T-E Agent Framework",
    framework=[
        ("Goal", "Business result, customer action, KPI, time horizon, and finish condition."),
        ("Context", "Brand, offer, audience evidence, channel role, and authorised inputs."),
        ("Actions", "Ordered steps and tools the workflow may use."),
        ("Tests", "Factual, brand, privacy, advertising, and performance checks."),
        ("Escalation", "Approval gates, stop conditions, owner, and recovery path."),
    ],
    statement=dict(
        headline="Let AI accelerate the loop; keep people accountable for the outcome.",
        body="Drafting and analysis can move quickly only when goals, evidence, permissions, and approval gates are explicit.",
        kicker="OPERATING PRINCIPLE",
    ),
    pillars_title="The Instagram Operations Pack You Will Build",
    pillars=[
        ("Foundation Pack", ["Success brief", "Journey map", "Account readiness", "Prompt contract"]),
        ("Content & Community", ["Content kit", "Calendar workflow", "Response router", "UGC register"]),
        ("Insight & Growth", ["Metrics dashboard", "Ads blueprint", "Retargeting and optimisation policy"]),
    ],
    arc_title="How Every Lab Progresses",
    arc=[
        "Start from the shared Harbour & Hearth brand brief and the previous lab checkpoint.",
        "Use AI to propose structured work from authorised inputs, not to invent business facts.",
        "Apply a human quality gate and record corrections in the campaign operations pack.",
        "Verify observable evidence before carrying the artifact into the next lab.",
    ],
)

LAB_SHOTS = {}

# ------------------------------------------------------------------ Learner Guide content
LG_INTRO = (
    "This Learner Guide is the self-contained study text for Agentic AI for Instagram Marketing (C695). "
    "It explains the concepts behind agent design, Instagram content and scheduling, community automation, analytics, advertising, and governed optimisation before guiding you through eight connected labs."
)
LG_INTRO2 = (
    "The course uses the synthetic Harbour & Hearth bakery scenario so every learner can work with the same evidence without exposing customer data or spending live advertising budget. "
    "Save each lab output in one Instagram operations folder; the final lab combines the complete set into a review-ready, human-governed operating pack."
)
LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a modern web browser and spreadsheet application.",
        "Access to an approved generative AI assistant such as ChatGPT, Microsoft Copilot, Claude, or Google Gemini.",
        "The course repository downloaded locally, including labs/resources/.",
        "Optional access to an Instagram Professional account, Meta Business Suite, or an n8n practice workspace for view-only exploration; no live posting, messaging, or ad spend is required.",
        "A new local folder named C695-campaign-pack for the eight lab artifacts.",
    ],
    verify_text="Open the brand brief and performance dataset, create the campaign-pack folder, and confirm your AI assistant can return a Markdown table without using confidential information.",
    verify_code="Open labs/resources/harbour-hearth-brand-brief.md\nOpen labs/resources/harbour-hearth-instagram-performance.csv\nCreate folder: C695-campaign-pack",
    conventions=[
        "Replace placeholders such as <PASTE BRIEF> with the specified synthetic course material.",
        "Never paste real customer identifiers, account secrets, unpublished results, or confidential creative into an unapproved AI tool.",
        "AI output is a proposal. Check facts, calculations, brand voice, rights, audience fairness, and the intended customer action.",
        "Work in draft mode. Do not publish a post, enable an automation, or activate an ad unless your organisation separately authorises it.",
        "Keep filenames exactly as shown so every later lab can find the earlier checkpoint.",
    ],
)
LAB_NOTE = "Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them."

LG_WRAPUP = dict(
    title="Wrap-Up — From Course Pack to Operating Practice",
    intro="Your final Instagram operations pack connects strategy, content, scheduling, community care, measurement, advertising, and governed optimisation. Its value comes from the traceable decisions between the files, not from any one AI-generated draft.",
    sections=[
        dict(
            title="Before using the workflow at work",
            bullets=[
                "Replace the synthetic brief with an approved business brief and document every authorised data source.",
                "Validate current Meta interface options, account permissions, objectives, and advertising rules for the intended market.",
                "Set named owners for brand review, privacy review, publishing, customer escalation, and budget approval.",
                "Start with draft-and-recommend mode, measure errors and corrections, then expand authority only where evidence supports it.",
            ],
        ),
        dict(
            title="Evidence to retain",
            bullets=[
                "Input version, prompt version, generated variants, reviewer corrections, and approval decision.",
                "Metric definitions, reporting window, source extract, calculations, and known data limitations.",
                "Before-and-after campaign settings, reason for change, owner, cooldown, result, and rollback action.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Re-run the campaign pack with one real, authorised offer while keeping all actions in draft.",
    "Create a small library of approved brand examples, evidence sources, response templates, and rejection labels.",
    "Review Meta's current official guidance before changing campaign settings or enabling a new automation.",
    "Pilot one low-risk workflow for two weeks, track corrections and exceptions, and revise the prompt contract.",
    "Hold a monthly review of data access, content quality, customer impact, performance thresholds, and rollback readiness.",
]

LG_GLOSSARY = [
    ("Accounts engaged", "The estimated number of unique accounts that interacted with content in the selected Instagram Insights scope."),
    ("Ad", "The creative, text, identity, destination, and related tracking shown to an audience."),
    ("Ad set", "The campaign level where audience, placements, budget, schedule, and performance choices are configured."),
    ("Agent", "A system that uses a model, instructions, and tools to pursue a multi-step goal within guardrails."),
    ("Approval gate", "A required human decision before a high-impact action can proceed."),
    ("Attribution", "The rule used to associate an observed customer action with marketing activity."),
    ("Campaign", "The top advertising level that contains the objective and one or more ad sets."),
    ("Conversion rate", "The share of relevant visits or clicks that complete the defined conversion action."),
    ("CPA", "Cost per acquisition or result: spend divided by the number of defined results."),
    ("CPC", "Cost per click: spend divided by the selected click count."),
    ("CPM", "Cost per one thousand impressions: spend divided by impressions, multiplied by 1,000."),
    ("CTR", "Click-through rate: selected clicks divided by impressions, expressed as a percentage."),
    ("Guardrail", "A rule, check, permission, or technical control that constrains unsafe or unwanted behaviour."),
    ("Interaction rate by reach", "Defined in this course as likes, comments, saves, and shares divided by accounts reached, expressed as a percentage."),
    ("Impression", "One delivery of content or an ad to a screen; the same person can generate multiple impressions."),
    ("Prompt contract", "Reusable instructions defining goal, inputs, rules, output schema, and escalation behaviour."),
    ("Reach", "The estimated number of distinct people who saw the content or ad."),
    ("ROAS", "Return on ad spend: attributed revenue divided by advertising spend."),
    ("Stop condition", "A defined state that ends or pauses an agentic loop."),
    ("UGC", "User-generated content: media or words created by a community member; public visibility does not automatically grant reuse permission."),
    ("Views", "The number of times content was displayed or played in the selected Instagram Insights scope; it may include repeated views."),
]

NEXT_STEPS = dict(
    title="Put the Workflow into Practice",
    items=[
        "Choose one authorised Instagram offer and rebuild the campaign pack in draft mode.",
        "Measure reviewer corrections and turn repeated failures into clearer rules or examples.",
        "Pilot one low-risk automation with an owner, stop rule, log, and rollback path.",
        "Review performance and customer-impact guardrails before increasing autonomy or spend.",
    ],
)

THANK_YOU = dict(
    body="You can now coordinate Instagram strategy, content, scheduling, community care, analytics, ads, and optimisation as one evidence-led, human-governed system.",
    kicker="C695 · KEEP BUILDING, CHECKING, AND LEARNING",
)

VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial aligned release: 4 topics, 8 connected labs, and 2 days / 15 instructional hours.", "Tertiary Infotech Academy Courseware Team"),
]
