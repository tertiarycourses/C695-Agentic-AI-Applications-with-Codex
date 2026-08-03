"""Topic 3 — Automating Engagement and Community Management."""

DOMAIN3 = [
    dict(
        num=5,
        topic=3,
        title="Build the Comment and Direct-Message Response Router",
        objective="LO3: Design a governed workflow for comment and direct-message intent, risk, lead capture, personalised drafts, follow-up, and human escalation",
        duration="50 minutes",
        desc=(
            "You design a community agent that routes eight synthetic Instagram comments and direct messages without exposing identifiers or promising unauthorised outcomes. "
            "The router drafts from approved facts for routine cases, captures only minimum lead fields, and stops for safety, allergy, payment, refund, privacy, or order-specific requests."
        ),
        build="C695-campaign-pack/05-community-response-router.md plus 05-response-queue.csv containing the intent taxonomy, risk rules, minimum-data lead schema, reviewed response drafts, escalation owners, and a workflow dry-run.",
        services="Approved generative AI assistant, spreadsheet application, text editor, labs/resources/harbour-hearth-community-scenarios.csv, labs/resources/harbour-hearth-brand-brief.md, C695-campaign-pack/02-agent-prompt-contract.md",
        prerequisites=[
            "Completed Labs 1 to 4 and keep the G-C-A-T-E contract active.",
            "Use only the synthetic messages; do not paste a real Inbox export.",
            "All responses remain drafts and no direct message is sent.",
        ],
        deck_steps=[
            "Define intent, risk, public/private route, and escalation ownership.",
            "Mask identifiers and classify eight synthetic community scenarios.",
            "Draft only from approved facts and design minimum-data lead capture.",
            "Dry-run routing, confidence, approval, logging, and exception paths.",
        ],
        steps=[
            (
                "Create 05-community-response-router.md with sections for Intent Taxonomy, Risk Rules, Lead Capture, Response Templates, Workflow, and Review Log.",
                "File: C695-campaign-pack/05-community-response-router.md",
            ),
            (
                "Define six intent categories: informational, commercial question, lead request, order service, sensitive issue, and abuse or spam. Assign each a default public/private route, risk tier, owner, and response-time target.",
                "Sensitive includes health, allergy, safety, payment, privacy, legal, threat, and crisis content. Order-specific changes require identity and order verification outside the AI workflow.",
            ),
            (
                "Create the response queue with the exact header below. Copy scenario IDs and messages from the synthetic CSV, then mask any phone number or order reference before AI classification.",
                "scenario_id,masked_message,intent,confidence,risk_tier,public_or_private,approved_source,response_action,owner,draft_status,reason",
            ),
            (
                "Ask the AI to classify the masked scenarios and propose a draft or escalation record.",
                """Apply the G-C-A-T-E contract to each synthetic Instagram message.

Return: scenario_id | intent | confidence high/medium/low | risk low/medium/high | public/private route | exact approved source | response action DRAFT/ASK ONE QUESTION/ESCALATE/NO RESPONSE | draft wording | human owner | reason.

Rules:
- use only approved brand-brief facts;
- do not repeat identifiers or request credentials;
- do not confirm order changes, refunds, compensation, medical advice, liability, or account outcomes;
- move personal, order, payment, allergy, safety, and complaint details to an approved private human channel;
- low confidence or missing facts = ESCALATE;
- all wording remains DRAFT — HUMAN REVIEW REQUIRED.""",
            ),
            (
                "Review each result against the message and brand brief. Routine collection-window and pre-order-link questions may receive a sourced draft. Allergy, refund, order change, duplicate charge, weekend uncertainty, and illness reports must escalate without an invented answer.",
                "Expected high-risk owners: Service Owner for order/refund/payment; Safety Owner for allergy or illness; Privacy Owner for personal-data concerns.",
            ),
            (
                "Write the minimum-data lead-capture schema for a person who explicitly asks for a corporate breakfast quote. Use an approved form rather than the AI chat.",
                "Fields: contact name, work email, approximate quantity, requested date, request summary, consent or authorised basis, source, assigned owner, status, retention date. Prohibited: age, home address, ethnicity, health, income, password, payment number, or unrelated message history.",
            ),
            (
                "Add follow-up rules. State the purpose before collection, send only the promised response, record consent or basis, assign an owner, suppress further marketing when consent is withdrawn, and remove the lead when the retention rule expires.",
                "A lead response may be personalised from the stated request and approved offer facts; it may not infer a person's role, urgency, budget, or preferences.",
            ),
            (
                "Design the node-by-node community workflow: receive event, minimise and mask, deterministic sensitive-keyword check, AI intent classification, confidence gate, retrieve approved response, human review, reply placeholder, lead hand-off, log, and error path.",
                "Instagram messaging conversations and API capabilities have platform permissions and interaction limits. Record OWNER TO VERIFY CURRENT PLATFORM RULES rather than hard-coding an unverified production assumption.",
            ),
            (
                "Dry-run all eight scenarios. Record the intended route and compare it with the expected safety rules. Any scenario that exposes identifiers, invents a fact, or sends a high-risk draft without escalation must be corrected and rerun.",
                "Pass rule: 8 of 8 scenarios have a defensible route; all high-risk scenarios show STOP — HUMAN ESCALATION.",
            ),
        ],
        test=(
            "Open 05-response-queue.csv and confirm eight scenario IDs, masked identifiers, one intent, one risk tier, one route, one owner, and one reason per row. M01 and M05 may be drafted from approved facts; M02, M03, M04, M06, M07, and M08 must not receive a confident automated resolution. "
            "No raw phone number or real customer data may appear in either output."
        ),
        checkpoint="Keep the reviewed taxonomy, queue, lead schema, and escalation owners. Lab 6 adds review and UGC permission handling, privacy and copyright checks, and the incident response path.",
        troubleshooting=[
            ("The agent classifies a message correctly but answers unsafely", "Evaluate routing and wording separately; high-risk intent always forces the escalation action before drafting."),
            ("A lead record contains too much data", "Start from the promised follow-up purpose and delete every field not needed to deliver it."),
            ("Confidence is always high", "Require evidence for the label and use low confidence when the approved knowledge source cannot answer the request."),
        ],
        challenge="Add multilingual detection that routes unsupported languages to a human instead of translating sensitive content automatically.",
        reflection="Why is a correct escalation often a better community outcome than a fast personalised answer?",
    ),
    dict(
        num=6,
        topic=3,
        title="Create the UGC, Review, Privacy and Escalation Runbook",
        objective="LO4: Apply privacy, copyright, platform, brand, and escalation rules to reviews, user-generated content, community responses, and AI-supported incident handling",
        duration="55 minutes",
        desc=(
            "You extend the community router with a rights and responsibility gate for reviews and user-generated content. "
            "The runbook records permission scope, checks AI drafts for truthful and fair treatment, and gives the team a practical response when content, privacy, or automation goes wrong."
        ),
        build="C695-campaign-pack/06-ugc-and-governance-runbook.md plus 06-ugc-permission-register.csv containing rights decisions, privacy and truth checks, escalation templates, retention rules, and an incident simulation.",
        services="Approved generative AI assistant, spreadsheet application, text editor, labs/resources/06-ugc-permission-register-starter.txt, labs/resources/harbour-hearth-ugc-scenarios.csv, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/05-community-response-router.md",
        prerequisites=[
            "Completed Lab 5 with the intent router and human owners available.",
            "Open the final 02-agent-prompt-contract.md and apply it to the rights-and-responsibility review.",
            "Open the synthetic UGC scenarios; do not contact any real account or rights holder.",
            "Treat public visibility as discovery only, never as permission to reuse.",
        ],
        deck_steps=[
            "Separate discovery, response, permission request, reuse, and withdrawal decisions.",
            "Record image, music, words, names, likeness, brand, and location rights.",
            "Apply privacy, truth, fairness, platform, and human-review gates.",
            "Simulate an incident, contain impact, correct the source, and test restoration.",
        ],
        steps=[
            (
                "Copy the supplied eight-row starter into 06-ugc-permission-register.csv and keep the exact header below.",
                "Source: labs/resources/06-ugc-permission-register-starter.txt\nOutput header: ugc_id,content_type,discovery_source,people_or_identifiers,third_party_assets,proposed_use,permission_status,permission_scope,expiry_or_withdrawal,required_edits,reviewer,reply_decision,reuse_decision,evidence_ref,reason",
            ),
            (
                "Read all scenarios and separate the decision to reply from the decision to reuse. A business may write a courteous public reply while reuse remains prohibited or pending.",
                "reply_decision labels: DRAFT REPLY | NO REPLY | HUMAN RESPONSE. reuse_decision labels: REQUEST PERMISSION | READY FOR RIGHTS REVIEW | STOP — DO NOT REUSE.",
            ),
            (
                "Ask the AI to apply the saved G-C-A-T-E contract and identify rights and privacy questions without making a legal conclusion.",
                """Apply the complete G-C-A-T-E contract in C695-campaign-pack/02-agent-prompt-contract.md. Review each synthetic Instagram review or UGC scenario as a rights-and-responsibility assistant.

Return: ugc_id | reply purpose | reuse purpose | people or personal data | image/video rights | music/text/logo/location issues | claim or endorsement risk | permission questions | required edits | reply_decision | reuse_decision | evidence_ref | human reviewer.

Rules:
- public content is not automatic permission;
- never invent consent, ownership, attribution, a rating, or a customer experience;
- quoted reviews must preserve meaning and cannot remove a material limitation;
- minors, health claims, visible third parties, copyrighted music, other brands, private locations, or uncertain ownership force STOP or specialist review;
- output is a review aid, not legal advice.""",
            ),
            (
                "Write a permission-request template that states the exact asset, proposed channel, format, editing, attribution, duration, commercial use, storage, and withdrawal contact. Do not use deceptive incentives or imply the person must agree.",
                "Permission remains PENDING until recorded by the authorised owner. Silence is not permission.",
            ),
            (
                "Create the responsible AI gate with six checks: purpose, data minimisation, rights, truth, fairness, and accountability. Define the evidence needed to pass each check and the owner for unresolved cases.",
                "Any failed rights, privacy, or truth check forces STOP. Brand or format issues may be REVISE when they can be corrected without changing meaning.",
            ),
            (
                "Add review-response rules. Thank genuine feedback without fabricating investigation outcomes; avoid arguments; move order or personal details to a private authorised route; flag suspected fake reviews for platform and human review; never generate a fake positive review.",
                "A response may acknowledge experience and explain the next contact step; it may not promise a refund, admission, deletion, or compensation without owner approval.",
            ),
            (
                "Define retention and withdrawal handling. Record where permission evidence is stored, who can access it, review date, expiry, channels covered, and the action when permission is withdrawn or content is deleted at source.",
                "Withdrawal path: stop new use → locate active placements → remove where controlled → update register → notify owner → retain only necessary decision evidence.",
            ),
            (
                "Create the incident runbook: detect, pause, preserve a minimal secure log, contain, notify owners, correct or remove, respond to the affected person, diagnose the failed rule, test with synthetic cases, approve restoration, and monitor.",
                "Required owners: Community, Brand, Privacy, Rights, Safety, and Technical Workflow Owner.",
            ),
            (
                "Simulate this incident: the workflow reused an image marked PENDING and generated a caption implying a customer endorsement. Record immediate actions, public correction, rights-owner contact path, root cause, guardrail change, restoration test, and final owner approval.",
                "Expected immediate status: PAUSE UGC WORKFLOW — RIGHTS AND TRUTH INCIDENT.",
            ),
        ],
        test=(
            "Every UGC row must have distinct reply_decision and reuse_decision values, permission status, scope or missing-scope reason, reviewer, and an evidence_ref pointing to a scenario row, permission record, or named policy rule. The incident simulation must pause the workflow, prevent further reuse, correct the unsupported endorsement, update the permission rule, and require a synthetic restoration test. "
            "No scenario may move from public discovery directly to reuse."
        ),
        checkpoint="Keep the permission register, responsible AI gate, and incident runbook. Labs 7 and 8 will add evidence-linked performance decisions while reusing the same privacy, rights, and approval boundaries.",
        troubleshooting=[
            ("The team treats attribution as permission", "Record attribution and permission as separate fields; both may be required, and neither substitutes for the other."),
            ("The AI gives a definitive copyright conclusion", "Change its role to identify issues and questions, then route uncertain ownership or scope to the authorised reviewer."),
            ("The incident plan says only 'delete the post'", "Add containment, secure evidence, affected-person response, root cause, rule correction, restoration test, and monitoring."),
        ],
        challenge="Add a quarterly rights-audit query that identifies expired permissions, missing scope, withdrawn consent, deleted source content, and assets without a reviewer.",
        reflection="What is the most important difference between finding community content, replying to it, and reusing it in marketing?",
    ),
]
