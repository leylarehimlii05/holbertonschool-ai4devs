# High-Level Architecture Plan - CodePulse Hackathon MVP

## System Overview
CodePulse is designed as a lightweight, three-tier web application optimized for rapid 24-hour hackathon delivery and zero-config cloud deployment. A Next.js + Tailwind CSS frontend communicates over RESTful JSON endpoints with a FastAPI (Python) backend service that orchestrates LLM prompt execution and persists reports in PostgreSQL (Supabase).

## Architecture Diagram

+-----------------------------------------------------------------------+
|                       CLIENT (Desktop & Mobile Browser)               |
|  +-----------------------------------------------------------------+  |
|  |                 Next.js + React + Tailwind CSS                  |  |
|  |  - Diff/Log Editor      - Mode Selector     - Markdown Preview  |  |
|  |  - One-Click Copy/.md   - Search & Filter   - Team Feed         |  |
|  +--------------------------------+--------------------------------+  |
+-----------------------------------|-----------------------------------+
| HTTPS (REST / JSON)
v
+-----------------------------------------------------------------------+
|                     BACKEND API (Python / FastAPI)                    |
|  +-------------------------+   +-----------------------------------+  |
|  | Request Validator &     |   | AI Orchestration & Prompt Engine  |  |
|  | Rate Limiter Middleware |   | - Loads PromptTemplate by mode    |  |
|  +-------------------------+   | - Parses risk_level & Markdown    |  |
|                                +-----------------+-----------------+  |
+--------------------------------------------------|--------------------+
| HTTPS (LLM API)         | SQL / Async Pool
v                         v
+--------------------------------+   +--------------------------+
|     External LLM Provider      |   | Database (PostgreSQL)    |
|   (OpenAI / Anthropic API)     |   | - team_members           |
+--------------------------------+   | - prompt_templates       |
| - generated_reports      |
+--------------------------+


## Layer Responsibilities & Tech Stack
1. **Frontend Layer (Next.js, React, Tailwind CSS — Deployed on Vercel):**
   - Provides a split-pane workspace: raw diff/log input on the left, live rendered Markdown preview on the right.
   - Implements client-side character count checks (max 15,000 chars), toast feedback, clipboard copy, and `.md` file blob downloads.
2. **Backend API Layer (FastAPI, Pydantic — Deployed on Render/Railway):**
   - `POST /api/generate`: Validates input payload, fetches the active `PromptTemplate`, calls the LLM provider with a deterministic JSON/Markdown schema prompt, saves the resulting `GeneratedReport`, and returns it to the client.
   - `GET /api/reports`: Supports query parameters (`?mode=...&repo=...&q=...`) to power the team history feed.
   - Protects endpoints with basic IP rate limiting and graceful fallback error handling if the upstream LLM times out.
3. **Data & AI Layer (PostgreSQL via Supabase + LLM API):**
   - Seeds 3 default `PromptTemplate` rows on startup (`pr_summary`, `bug_root_cause`, `release_notes`).
   - Uses low temperature (`0.2`) for consistent, structured technical summaries.

## Hackathon Sprint Execution Plan (24 Hours)
- **Hours 0–4:** Repo setup, database schema migration, seed prompt templates, and FastAPI skeleton (`Nigar` & `Leyla`).
- **Hours 4–12:** LLM integration endpoint + Next.js split-pane editor and team feed UI (`Rashad` & `Nigar`).
- **Hours 12–18:** Filtering, `.md` export, responsive polish, and automated API/UI tests (`Tural` & `Rashad`).
- **Hours 18–24:** Production deployment (Vercel + Render + Supabase), end-to-end smoke testing, and demo pitch prep (`All`).
