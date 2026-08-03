# Lab 3 — Create the Instagram Content and Creative Kit

- **Course:** Agentic AI for Instagram Marketing (C695)
- **Version:** v1.0 (3 August 2026)
- **Topic 2:** AI-Powered Content Creation and Scheduling
- **Maps to:** LO2: Generate an on-brand Instagram content system with captions, hashtags, image briefs, and Reels ideas grounded in approved evidence
- **Tools:** Approved generative AI assistant, text editor, labs/resources/03-instagram-content-kit-starter.md, C695-campaign-pack/01-foundation-and-readiness.md, C695-campaign-pack/02-agent-prompt-contract.md, labs/resources/harbour-hearth-brand-brief.md

**Duration:** 45 minutes

---

## What You Will Do

You use the approved journey and prompt contract to create a seven-item Instagram content kit for Harbour & Hearth. The kit covers feed posts, a carousel, Stories, and Reels while preserving one message hierarchy, observable brand-voice rules, relevant hashtags, creative rights checks, and a clear customer action.

## What You Will Build

C695-campaign-pack/03-instagram-content-kit.md containing seven content briefs, reviewed captions, hashtag rationales, image or storyboard directions, a brand consistency score, and a rights log.

## Prerequisites

- Completed Labs 1 and 2 with the customer journey and final prompt contract available.
- Keep all content in draft; do not post or schedule anything.
- Use only the synthetic product facts, offer, link, and visual direction in the brand brief.

> **Rejoin path.** If a prerequisite artifact is missing, use the Rejoin Path in [the labs index](README.md), reconstruct the named checkpoint, and verify it before continuing.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Copy the supplied starter to 03-instagram-content-kit.md. Add the approved audience hypothesis, customer action, brand rules, factual evidence, and the G-C-A-T-E contract as the content guardrail.**

```text
Source: labs/resources/03-instagram-content-kit-starter.md
Output: C695-campaign-pack/03-instagram-content-kit.md
```

**2. Define four content pillars: Teach, Show, Prove, and Invite. For each, state its customer-journey job, approved evidence, suitable formats, and one learning question.**

```text
Required columns: Pillar | Journey stage | Customer question | Approved evidence | Format choices | Learning question.
```

**3. Write one stable message hierarchy for the Sunrise Breakfast Box before generating individual posts.**

```text
Audience tension → relevant promise → approved proof → offer detail → completed pre-order action. Unsupported testimonials, health claims, popularity claims, and artificial urgency are forbidden.
```

**4. Ask the AI to create exactly seven content briefs: two single-image posts, two Reels, one carousel, and two Stories sequences.**

```text
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

**5. Review every caption against the brand brief. Mark each factual phrase with its source heading, remove duplicate ideas, and ensure each post has one customer action rather than several competing calls to action.**

```text
Reviewer labels: GROUNDED | REVISE — <REASON> | STOP — <REASON>.
```

**6. Audit each hashtag set. Keep only terms that accurately describe the brand, product, use case, location, or campaign. Remove ambiguous, unrelated, duplicate, banned, or promise-like tags.**

```text
Hashtag note format: #Tag — relevant because <SOURCE OR CONTENT PURPOSE>; risk checked on <DATE>.
```

**7. Expand the carousel into five cards and each Reel into a six-beat storyboard. For Reels, specify opening frame, movement, on-screen meaning without audio, voice or caption role, proof, CTA, and safe-area note.**

```text
Do not put long prose into the visual. Captions carry detail; visuals carry one recognisable idea at a time.
```

**8. Add a creative rights and truth log for every asset. Record source type, owner, licence or permission status, AI-generation disclosure requirement if any, product-accuracy review, and final human reviewer.**

```text
If rights or product accuracy are UNKNOWN, the asset status is STOP — DO NOT USE.
```

**9. Score all seven items from 0 to 2 for grounding, brand voice, customer value, mobile format fit, rights, and action alignment. Revise any item with a zero or a total below 10 of 12.**

```text
Score rule: 0 = fails or unknown; 1 = usable with revision; 2 = meets the reviewed standard.
```

**10. Promote each item only after scoring. Change its final status to READY FOR HUMAN REVIEW only when all six dimensions have a score above zero, the total is at least 10 of 12, its reviewer label is GROUNDED, and its rights status is not UNKNOWN. Otherwise revise and rescore or mark STOP.**

```text
Promotion record: Content ID | Score | Reviewer label | Rights status | Final status | Reviewer | Date. Allowed final status: READY FOR HUMAN REVIEW | REVISE — <REASON> | STOP — <REASON>.
```

## Test It

The file must contain exactly seven briefs in the required format mix, each with a caption, one CTA, 5-8 justified hashtags, a visual or storyboard brief, source references, rights status, and reviewer status. All seven items must pass the six-part score rule and show an explicit READY FOR HUMAN REVIEW promotion record before Lab 4; otherwise revise them before continuing. Search for unsupported discount, testimonial, health, award, popularity, and urgency claims; the count must be zero. Retain the score, source check, expected result, observed result, reviewer, and date as verification evidence.

## Checkpoint for the Next Lab

Keep the seven reviewed content IDs and their status. Lab 4 will place only items marked READY FOR HUMAN REVIEW into a dated calendar and scheduling workflow.

## Troubleshooting

- **All captions sound identical:** Hold the message hierarchy stable but vary the customer question, content pillar, format job, and hook angle.
- **Hashtags are generic or excessive:** Require a relevance rationale and remove every tag that cannot be tied to the brand, offer, place, or content purpose.
- **The Reel depends on spoken audio:** Rewrite the first frame and visual beats so the subject and value remain clear when muted.

## Challenge

Create one alternative Reel hook that changes only the hook angle while keeping offer, storyboard beats, CTA, and evidence stable for later comparison.

## Reflection

Which content-format decision is strategic rather than cosmetic, and what evidence would make you choose a different format?

---

[← Lab 2](lab-02-write-and-test-the-instagram-agent-prompt-contract.md) · [Lab 4 →](lab-04-build-the-content-calendar-agent-and-publishing-workflow.md)
