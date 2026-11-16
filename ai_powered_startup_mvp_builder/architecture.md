# System Architecture - SprintPulse MVP

## Overview
SprintPulse follows a modern, lightweight client-server architecture optimized for rapid MVP deployment and free-tier scalability. The frontend is a responsive Next.js (React + Tailwind CSS) application, communicating via RESTful JSON endpoints with a Node.js/Express backend API backed by PostgreSQL (Supabase).

## High-Level System Diagram

+-------------------------------------------------------------------+
|                        CLIENT (Browser / Mobile)                  |
|  +-------------------------------------------------------------+  |
|  |              Next.js / React + Tailwind CSS UI              |  |
|  |  - Workspace Login   - Check-In Form   - Blocker Highlights  |  |
|  |  - Search & Filter   - Feed View       - CSV/MD Export       |  |
|  +------------------------------+------------------------------+  |
+---------------------------------|---------------------------------+
| HTTPS (REST API / JSON)
v
+-------------------------------------------------------------------+
|                   BACKEND API (Node.js / Express)                 |
|  +-----------------------+  +----------------------------------+  |
|  |  Auth / Workspace     |  |  Check-In & Blocker Controller   |  |
|  |  Session Middleware   |  |  - Validation & Sanitization     |  |
|  +-----------------------+  |  - Blocker Resolution Logic      |  |
|                             |  - CSV / Markdown Exporter       |  |
|                             +-----------------+----------------+  |
+-----------------------------------------------|-------------------+
| SQL / Connection Pool
v
+-------------------------------------------------------------------+
|                   DATABASE (Supabase / PostgreSQL)                |
|  +-------------------+  +-------------------+  +---------------+  |
|  |    workspaces     |  |      members      |  |   check_ins   |  |
|  +-------------------+  +-------------------+  +---------------+  |
+-------------------------------------------------------------------+


## Component Responsibilities
1. **Frontend (Next.js / React):**
   - Renders the responsive single-page dashboard with tab/filter controls.
   - Manages workspace session tokens in `localStorage` and validates form inputs client-side before submission.
   - Generates client-side file downloads from exported CSV/Markdown payloads.
2. **Backend API (Node.js / Express):**
   - Validates workspace access codes and issues lightweight session tokens.
   - Enforces business rules (e.g., max 500 check-ins per workspace, non-empty required fields, severity enum checks).
   - Provides filtering, blocker status updates (`PATCH /api/check-ins/:id/resolve`), and formatted export endpoints (`GET /api/export`).
3. **Database (PostgreSQL via Supabase):**
   - Persists relational data across `workspaces`, `members`, and `check_ins` with foreign key constraints and indexes on `workspace_id` and `created_at`.
