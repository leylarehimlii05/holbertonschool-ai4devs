# Team Ideation

## Brainstormed Ideas
1. **Smart Meeting Action-Item Extractor:** An app that transcribes team calls and automatically assigns follow-up tasks with deadlines.
2. **AI Resume & Job-Match Tailoring Assistant:** A tool that analyzes job descriptions and rewrites bullet points on a candidate's resume to highlight relevant skills.
3. **CodePulse — AI Pull Request & Incident Postmortem Helper** ✅ *(chosen)*

## Problem Statement
During fast-paced hackathons and agile sprints, developers spend significant time manually writing clear PR summaries, release notes, and incident postmortems from raw git diffs or error logs. Under tight deadlines, documentation gets skipped or rushed, making code reviews and debugging harder for teammates. An AI-assisted tool that turns raw code diffs or stack traces into structured, actionable summaries solves this bottleneck immediately.

## MVP Features
1. **Diff & Log Input Workspace:** Clean editor where users paste a raw `git diff`, commit log, or error stack trace and select the output mode (`PR Summary`, `Bug Root-Cause`, or `Release Notes`).
2. **AI-Powered Structured Generator:** Uses LLM prompt templates to generate formatted Markdown output including summary, risk level, affected components, and suggested checklist items.
3. **One-Click Copy & Markdown Export:** Allows developers to copy the generated report directly to the clipboard or download it as a `.md` file for GitHub/Notion.
4. **History & Team Snippets Feed:** Stores the latest generated summaries in a lightweight database/local session so teammates can review, filter, and reuse recent analyses.

## Team Roles

| Member | Role | Key Responsibilities |
| :--- | :--- | :--- |
| **Leyla** | Product Lead & AI Prompt Strategist | Defines MVP scope, engineers structured LLM system prompts, and coordinates sprint milestones. |
| **Rashad** | Frontend Developer | Builds the responsive Next.js/Tailwind UI, code/diff editor, and one-click export interactions. |
| **Nigar** | Backend & API Developer | Implements REST endpoints, integrates the AI API, handles rate limiting, and manages data persistence. |
| **Tural** | QA, DevOps & Demo Lead | Writes automated unit/integration tests, manages CI/CD deployment to Vercel/Render, and prepares the final demo. |
