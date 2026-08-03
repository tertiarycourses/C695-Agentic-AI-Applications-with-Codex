# C695 — Agentic AI for Instagram Marketing

Aligned non-WSQ courseware for Tertiary Infotech Academy's two-day course.

## Package

- Trainer slide deck and learner-slide PDF
- Learner Guide in DOCX, PDF, and Markdown
- Lesson Plan in DOCX and PDF
- Eight connected hands-on labs with synthetic resources

The local single-source generator lives in `.agents/skills/non-wsq-courseware-build/`. Its `course_data.py` and four `data_domainN.py` modules drive the deck, Learner Guide, Lesson Plan, and lab set so titles, outcomes, topics, timing, and lab sequence remain aligned.

## Build

From Git Bash on Windows:

```bash
COURSE_REPO="$PWD" bash ".agents/skills/non-wsq-courseware-build/build/build_courseware.sh"
```

## Course identity

- Course: Agentic AI for Instagram Marketing
- Code: C695
- Duration: 2 days / 15 instructional hours
- Level: Beginner
- Current courseware version: v1.0

Research sources are recorded in `reference/SOURCES.md`.
