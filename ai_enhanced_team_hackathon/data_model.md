# Data Model - CodePulse Hackathon MVP

## Entity-Relationship Diagram

+------------------------+       +-----------------------------+       +------------------------+
|       TeamMember       |       |       GeneratedReport       |       |     PromptTemplate     |
+------------------------+       +-----------------------------+       +------------------------+
| PK id (UUID)           |--1:N--| PK id (UUID)                |--N:1--| PK id (UUID)           |
|    display_name (VARCH)|       | FK author_id (UUID)         |       |    mode_key (VARCHAR)  |
|    role (VARCHAR)      |       | FK template_id (UUID)       |       |    title (VARCHAR)     |
|    created_at (TIMESTZ)|       |    repo_tag (VARCHAR)       |       |    system_prompt (TEXT)|
+------------------------+       |    raw_input (TEXT)         |       |    is_active (BOOLEAN) |
|    markdown_output (TEXT)   |       +------------------------+
|    risk_level (ENUM)        |
|    created_at (TIMESTAMPTZ) |
+-----------------------------+


---

## Entity Definitions

### 1. `TeamMember`
Represents a hackathon participant or developer creating and reviewing AI-generated reports.
- **`id`** (`UUID`, Primary Key): Unique identifier for the team member.
- **`display_name`** (`VARCHAR(60)`, Not Null): Name shown alongside generated reports in the team feed.
- **`role`** (`VARCHAR(40)`, Default: `'Developer'`): Team role (e.g., `'Product Lead'`, `'Frontend Dev'`, `'Backend Dev'`, `'QA Lead'`).
- **`created_at`** (`TIMESTAMPTZ`, Default: `NOW()`): Timestamp when the member profile was initialized.

### 2. `PromptTemplate`
Stores structured system prompts mapped to each supported generation mode.
- **`id`** (`UUID`, Primary Key): Unique identifier for the prompt template.
- **`mode_key`** (`VARCHAR(32)`, Unique, Not Null): Machine-readable mode identifier (`'pr_summary'`, `'bug_root_cause'`, `'release_notes'`).
- **`title`** (`VARCHAR(80)`, Not Null): Human-readable label shown in the UI mode selector.
- **`system_prompt`** (`TEXT`, Not Null): Engineered LLM instruction enforcing Markdown structure, risk assessment, and checklists.
- **`is_active`** (`BOOLEAN`, Default: `TRUE`): Allows toggling templates without deleting historical references.

### 3. `GeneratedReport`
Represents an AI-generated PR summary, bug root-cause analysis, or release note stored in the team history feed.
- **`id`** (`UUID`, Primary Key): Unique identifier for the report.
- **`author_id`** (`UUID`, Foreign Key -> `TeamMember.id`, Not Null): Links the report to its creator (`ON DELETE CASCADE`).
- **`template_id`** (`UUID`, Foreign Key -> `PromptTemplate.id`, Not Null): Identifies which prompt mode generated the report.
- **`repo_tag`** (`VARCHAR(80)`, Default: `'general'`): Optional repository or microservice tag for filtering.
- **`raw_input`** (`TEXT`, Not Null): Original `git diff`, commit log, or stack trace submitted by the user (capped at 15,000 characters).
- **`markdown_output`** (`TEXT`, Not Null): Structured Markdown response returned by the LLM.
- **`risk_level`** (`ENUM('low', 'medium', 'high')`, Default: `'low'`): Extracted risk severity badge displayed in the feed.
- **`created_at`** (`TIMESTAMPTZ`, Default: `NOW()`): Timestamp when the report was generated.

## Indexes & Constraints
- Index on `GeneratedReport(created_at DESC)` for fast chronological rendering of the team snippets feed.
- Index on `GeneratedReport(template_id, repo_tag)` for rapid mode and repository filtering.
