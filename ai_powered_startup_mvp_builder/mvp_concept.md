# MVP Concept - SprintPulse (Lightweight Team Standup & Blocker Tracker)

## Problem Statement
Remote and hybrid software engineering teams waste valuable synchronous meeting time on repetitive daily status updates, while critical blockers often go unnoticed until late in the sprint. Existing project management tools like Jira are overly complex for quick daily check-ins, and chat threads in Slack easily bury unresolved blockers. Teams need a fast, structured, and asynchronous way to share daily progress and surface blockers immediately.

## Target Users
- **Engineering Team Leads & Tech Leads:** Need an instant overview of team progress and immediate visibility into technical blockers.
- **Software Developers:** Want a frictionless, under-60-second way to log yesterday's progress, today's plan, and any blockers without context-switching into heavy tools.
- **Product & Project Managers:** Need high-level sprint visibility and historical check-in logs without scheduling extra status meetings.

## Core Features
1. **Quick Daily Check-In Form:** A structured 3-field submission form (*Yesterday*, *Today*, *Blockers*) with a severity toggle (`None`, `Minor`, `Critical`) for blockers.
2. **Real-Time Team Feed & Blocker Highlighting:** A clean dashboard displaying daily updates grouped by date, automatically pinning and highlighting active blockers at the top.
3. **Search & Filter Dashboard:** Instant filtering by team member name, date, or blocker status (`All`, `Blocked Only`, `Resolved`).
4. **One-Click Blocker Resolution:** Ability for team members to mark a blocker as resolved with a timestamp, updating the team status board immediately.
5. **Markdown / CSV Summary Export:** Export a selected day's or week's standup updates as formatted Markdown (for Slack/Notion) or CSV for sprint retrospectives.

## Constraints
- **No Complex Authentication (MVP Scope):** Uses simple workspace access codes or lightweight magic-link/guest sessions instead of full OAuth/SSO integration.
- **Single-Workspace Limit:** Supports one active team workspace per deployment with a maximum of 500 stored check-in entries to stay within free-tier database limits.
- **No Third-Party Integrations:** Direct Slack, GitHub, and Jira webhooks are excluded from the MVP to ensure rapid delivery within a single sprint.
- **Web-First Responsive UI:** Delivered strictly as a responsive web application (no native iOS/Android apps in v1).
