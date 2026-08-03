"""Topic 2 — AI-Powered Content Creation and Scheduling."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Create the Instagram Content and Creative Kit",
        objective="LO2: Generate an on-brand Instagram content system with captions, hashtags, image briefs, and Reels ideas grounded in approved evidence",
        duration="45 minutes",
        desc=(
            "You use the approved journey and prompt contract to create a seven-item Instagram content kit for Harbour & Hearth. "
            "The kit covers feed posts, a carousel, Stories, and Reels while preserving one message hierarchy, observable brand-voice rules, relevant hashtags, creative rights checks, and a clear customer action."
        ),
        build="C695-campaign-pack/03-instagram-content-kit.md containing seven content briefs, reviewed captions, hashtag rationales, image or storyboard directions, a brand consistency score, and a rights log.",
        services="Approved generative AI assistant, text editor, labs/resources/03-instagram-content-kit-starter.md, C695-campaign-pack/01-foundation-and-readiness.md, C695-campaign-pack/02-agent-prompt-contract.md, labs/resources/harbour-hearth-brand-brief.md",
        prerequisites=[
            "Completed Labs 1 and 2 with the customer journey and final prompt contract available.",
            "Keep all content in draft; do not post or schedule anything.",
            "Use only the synthetic product facts, offer, link, and visual direction in the brand brief.",
        ],
        deck_steps=[
            "Define content pillars and a stable tension-promise-proof-action hierarchy.",
            "Generate seven format-specific captions and relevant hashtag sets.",
            "Create image, carousel, Stories, and Reels briefs with mobile-first checks.",
            "Score grounding, voice, customer value, rights, and action alignment.",
        ],
        steps=[
            (
                "Copy the supplied starter to 03-instagram-content-kit.md. Add the approved audience hypothesis, customer action, brand rules, factual evidence, and the G-C-A-T-E contract as the content guardrail.",
                "Source: labs/resources/03-instagram-content-kit-starter.md\nOutput: C695-campaign-pack/03-instagram-content-kit.md",
            ),
            (
                "Define four content pillars: Teach, Show, Prove, and Invite. For each, state its customer-journey job, approved evidence, suitable formats, and one learning question.",
                "Required columns: Pillar | Journey stage | Customer question | Approved evidence | Format choices | Learning question.",
            ),
            (
                "Write one stable message hierarchy for the Sunrise Breakfast Box before generating individual posts.",
                "Audience tension → relevant promise → approved proof → offer detail → completed pre-order action. Unsupported testimonials, health claims, popularity claims, and artificial urgency are forbidden.",
            ),
            (
                "Ask the AI to create exactly seven content briefs: two single-image posts, two Reels, one carousel, and two Stories sequences.",
                """Using the G-C-A-T-E contract, reviewed journey, brand brief, four content pillars, and message hierarchy, create exactly seven Instagram content briefs.

Required mix: 2 single-image feed posts, 2 Reels, 1 carousel, 2 Stories sequences.
For each return: Content ID | Journey job | Pillar | Format | Hook | Caption | CTA | 5-8 relevant hashtags with one-line rationale | Visual or storyboard brief | Approved fact sources | Assumption or UNKNOWN | Quality risk.

Rules:
- use only approved synthetic facts;
- keep the brand voice warm and direct;
- make the first frame or first card understandable without sound;
- do not generate a logo, customer face, testimonial, award, nutrition claim, false scarcity, or text baked into an image;
- mark all outputs DRAFT — HUMAN REVIEW REQUIRED.""",
            ),
            (
                "Review every caption against the brand brief. Mark each factual phrase with its source heading, remove duplicate ideas, and ensure each post has one customer action rather than several competing calls to action.",
                "Reviewer labels: GROUNDED | REVISE — <REASON> | STOP — <REASON>.",
            ),
            (
                "Audit each hashtag set. Keep only terms that accurately describe the brand, product, use case, location, or campaign. Remove ambiguous, unrelated, duplicate, banned, or promise-like tags.",
                "Hashtag note format: #Tag — relevant because <SOURCE OR CONTENT PURPOSE>; risk checked on <DATE>.",
            ),
            (
                "Expand the carousel into five cards and each Reel into a six-beat storyboard. For Reels, specify opening frame, movement, on-screen meaning without audio, voice or caption role, proof, CTA, and safe-area note.",
                "Do not put long prose into the visual. Captions carry detail; visuals carry one recognisable idea at a time.",
            ),
            (
                "Add a creative rights and truth log for every asset. Record source type, owner, licence or permission status, AI-generation disclosure requirement if any, product-accuracy review, and final human reviewer.",
                "If rights or product accuracy are UNKNOWN, the asset status is STOP — DO NOT USE.",
            ),
            (
                "Score all seven items from 0 to 2 for grounding, brand voice, customer value, mobile format fit, rights, and action alignment. Revise any item with a zero or a total below 10 of 12.",
                "Score rule: 0 = fails or unknown; 1 = usable with revision; 2 = meets the reviewed standard.",
            ),
            (
                "Promote each item only after scoring. Change its final status to READY FOR HUMAN REVIEW only when all six dimensions have a score above zero, the total is at least 10 of 12, its reviewer label is GROUNDED, and its rights status is not UNKNOWN. Otherwise revise and rescore or mark STOP.",
                "Promotion record: Content ID | Score | Reviewer label | Rights status | Final status | Reviewer | Date. Allowed final status: READY FOR HUMAN REVIEW | REVISE — <REASON> | STOP — <REASON>.",
            ),
        ],
        test=(
            "The file must contain exactly seven briefs in the required format mix, each with a caption, one CTA, 5-8 justified hashtags, a visual or storyboard brief, source references, rights status, and reviewer status. "
            "All seven items must pass the six-part score rule and show an explicit READY FOR HUMAN REVIEW promotion record before Lab 4; otherwise revise them before continuing. Search for unsupported discount, testimonial, health, award, popularity, and urgency claims; the count must be zero. Retain the score, source check, expected result, observed result, reviewer, and date as verification evidence."
        ),
        checkpoint="Keep the seven reviewed content IDs and their status. Lab 4 will place only items marked READY FOR HUMAN REVIEW into a dated calendar and scheduling workflow.",
        troubleshooting=[
            ("All captions sound identical", "Hold the message hierarchy stable but vary the customer question, content pillar, format job, and hook angle."),
            ("Hashtags are generic or excessive", "Require a relevance rationale and remove every tag that cannot be tied to the brand, offer, place, or content purpose."),
            ("The Reel depends on spoken audio", "Rewrite the first frame and visual beats so the subject and value remain clear when muted."),
        ],
        challenge="Create one alternative Reel hook that changes only the hook angle while keeping offer, storyboard beats, CTA, and evidence stable for later comparison.",
        reflection="Which content-format decision is strategic rather than cosmetic, and what evidence would make you choose a different format?",
    ),
    dict(
        num=4,
        topic=2,
        title="Build the Content Calendar Agent and Publishing Workflow",
        objective="LO2: Build a brand-consistent calendar agent and controlled scheduling workflow with approval, duplicate prevention, failure handling, and verification",
        duration="60 minutes",
        desc=(
            "You convert the reviewed content kit into a seven-day Instagram calendar and a draft-first publishing workflow. "
            "The workflow can prepare and validate a schedule, but it stops at the human approval gate before Meta Business Suite or an API publishing action."
        ),
        build="C695-campaign-pack/04-calendar-and-publishing-workflow.md plus 04-instagram-calendar.csv containing seven scheduled drafts, validation rules, a node-by-node n8n-style workflow, approval evidence, error handling, and a dry-run log.",
        services="Approved generative AI assistant, spreadsheet application, text editor, C695-campaign-pack/02-agent-prompt-contract.md, C695-campaign-pack/03-instagram-content-kit.md, optional Meta Business Suite or n8n view-only access",
        prerequisites=[
            "Completed Lab 3 with seven content IDs explicitly promoted to READY FOR HUMAN REVIEW.",
            "Open the final 02-agent-prompt-contract.md and apply it to every AI-assisted workflow step.",
            "Use Asia/Singapore as the calendar time zone.",
            "Keep the publishing step disabled or represented by a placeholder; do not connect credentials.",
        ],
        deck_steps=[
            "Turn reviewed content into a seven-day queue with content and learning balance.",
            "Define required fields, status transitions, approval evidence, and duplicate keys.",
            "Design the trigger, validation, review, publish-placeholder, logging, and error paths.",
            "Run safe and unsafe dry-run rows and verify the workflow stops correctly.",
        ],
        steps=[
            (
                "Create 04-instagram-calendar.csv with exactly the required header and seven rows, one for each reviewed content ID.",
                "content_id,date_sgt,time_sgt,format,journey_stage,pillar,asset_ref,caption_status,hashtag_status,rights_status,cta,destination,reviewer,approval_status,publish_status,learning_question",
            ),
            (
                "Assign each content item to one day in a seven-day window. Balance customer-journey jobs, pillars, and formats; do not schedule two items for the same minute.",
                "Use ISO dates and 24-hour Singapore time. Keep publish_status=DRAFT for all rows.",
            ),
            (
                "Create 04-calendar-and-publishing-workflow.md. Define allowed status transitions and the composite duplicate key.",
                "DRAFT → READY FOR HUMAN REVIEW → APPROVED BY <ROLE> → SCHEDULED → PUBLISHED or ERROR. Duplicate key: account placeholder + content_id + scheduled ISO timestamp.",
            ),
            (
                "Write deterministic preflight rules. A row may reach the publishing placeholder only when content ID, asset, caption, hashtags, rights, CTA, destination, reviewer, approval evidence, time zone, and timestamp are present and compatible.",
                "Fail closed on UNKNOWN rights, missing reviewer, missing approval, past timestamp, duplicate key, conflicting destination, or invalid status transition.",
            ),
            (
                "Ask the AI to apply the saved G-C-A-T-E contract and turn the rules into a node-by-node n8n-style workflow specification.",
                """Apply the complete G-C-A-T-E contract in C695-campaign-pack/02-agent-prompt-contract.md. Create a recommendation-only workflow specification with these nodes:
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

For each node return: purpose, input fields, deterministic rule, output fields, credential requirement, error path, and evidence retained. Do not include a real token or executable publishing request.""",
            ),
            (
                "Add a publishing checklist for an authorised owner using the current approved interface. It must verify account identity, final asset, caption, link, time zone, date and time, preview, permissions, reviewer, and rollback owner.",
                "Optional view-only exploration: locate Planner or draft controls in Meta Business Suite and record interface differences; close without saving or scheduling.",
            ),
            (
                "Create two dry-run inputs. Safe Row uses complete synthetic values and approval_status=APPROVED BY MARKETING OWNER. Unsafe Row removes approval and sets rights_status=UNKNOWN.",
                "Expected Safe Row result: READY AT PUBLISH PLACEHOLDER — EXTERNAL ACTION DISABLED. Expected Unsafe Row result: STOP — APPROVAL AND RIGHTS REQUIRED.",
            ),
            (
                "Add duplicate protection and retry behaviour. Replaying the same Safe Row must produce SKIP — DUPLICATE KEY, and a simulated publish error may retry once before ERROR — HUMAN HAND-OFF.",
                "Never retry an unknown outcome in a way that could create a duplicate public post.",
            ),
            (
                "Record all three dry-run results in a log with input hash or filename, validation outcome, approval status, proposed action, timestamp, and owner.",
                "## Dry-Run Log\n| Run | Input | Validation | Approval | Result | Owner |\n|---|---|---|---|---|---|",
            ),
        ],
        test=(
            "The calendar must have seven unique content IDs, ISO dates, Asia/Singapore times, and DRAFT publication status. The Safe Row must stop at the disabled publish placeholder; the Unsafe Row must stop for approval and rights; the replay must skip as a duplicate. "
            "No credential, token, real account ID, or live scheduling action may appear in the files."
        ),
        checkpoint="Keep 04-instagram-calendar.csv and the workflow dry-run log. Labs 5 and 6 add community events, response routing, and rights governance to the same operating system.",
        troubleshooting=[
            ("The workflow relies on the AI to decide if fields are missing", "Move schema, timestamp, status, rights, approval, and duplicate checks into deterministic validation nodes."),
            ("A failed publish could create duplicates", "Use an idempotency key, inspect the action log, and hand off after one uncertain result instead of retrying blindly."),
            ("Calendar balance is arbitrary", "Use the customer-journey job, pillar, format, and learning question columns to justify every date choice."),
        ],
        challenge="Add an expiry rule that returns an approved row to REVIEW when the scheduled time changes, the asset changes, or more than seven days pass after approval.",
        reflection="Which validation belongs in a fixed rule rather than an AI judgement, and what failure would occur if the boundary were reversed?",
    ),
]
