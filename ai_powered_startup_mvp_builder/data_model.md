# Data Model - SprintPulse MVP

## Entity-Relationship Diagram

+------------------------+       +------------------------+       +-----------------------------+
|       Workspace        |       |         Member         |       |          CheckIn            |
+------------------------+       +------------------------+       +-----------------------------+
| PK id (UUID)           |--1:N--| PK id (UUID)           |--1:N--| PK id (UUID)                |
|    name (VARCHAR)      |       | FK workspace_id (UUID) |       | FK workspace_id (UUID)      |
|    access_code (VARCHAR|       |    display_name (VARCH)|       | FK member_id (UUID)         |
|    created_at (TIMESTZ)|       |    role (VARCHAR)      |       |    yesterday_text (TEXT)    |
+------------------------+       |    created_at (TIMESTZ)|       |    today_text (TEXT)        |
+------------------------+       |    blocker_text (TEXT)      |
|    blocker_severity (ENUM)  |
|    is_resolved (BOOLEAN)    |
|    resolved_at (TIMESTAMPTZ)|
|    created_at (TIMESTAMPTZ) |
+-----------------------------+


---

## Entity Definitions

### 1. `Workspace`
Represents an isolated team environment where daily standups are logged.
- **`id`** (`UUID`, Primary Key): Unique identifier for the workspace.
- **`name`** (`VARCHAR(100)`, Not Null): Team or project workspace name (e.g., `"Core Platform Team"`).
- **`access_code`** (`VARCHAR(32)`, Unique, Not Null): Lightweight shared code used by team members to join the workspace.
- **`created_at`** (`TIMESTAMPTZ`, Default: `NOW()`): Timestamp when the workspace was created.

### 2. `Member`
Represents a team member participating within a specific workspace.
- **`id`** (`UUID`, Primary Key): Unique identifier for the member.
- **`workspace_id`** (`UUID`, Foreign Key -> `Workspace.id`, Not Null): Links the member to their workspace (`ON DELETE CASCADE`).
- **`display_name`** (`VARCHAR(60)`, Not Null): Name displayed alongside daily check-in entries.
- **`role`** (`VARCHAR(30)`, Default: `'Developer'`): Team role (e.g., `'Developer'`, `'Tech Lead'`, `'PM'`).
- **`created_at`** (`TIMESTAMPTZ`, Default: `NOW()`): Timestamp when the member joined the workspace.

### 3. `CheckIn`
Represents a single daily standup update submitted by a team member.
- **`id`** (`UUID`, Primary Key): Unique identifier for the check-in entry.
- **`workspace_id`** (`UUID`, Foreign Key -> `Workspace.id`, Not Null): Enables fast workspace-wide queries and enforces the 500-entry MVP cap.
- **`member_id`** (`UUID`, Foreign Key -> `Member.id`, Not Null): Author of the check-in (`ON DELETE CASCADE`).
- **`yesterday_text`** (`TEXT`, Not Null): Summary of tasks completed on the previous workday.
- **`today_text`** (`TEXT`, Not Null): Planned tasks for the current workday.
- **`blocker_text`** (`TEXT`, Nullable): Optional description of any technical or process impediment.
- **`blocker_severity`** (`ENUM('none', 'minor', 'critical')`, Default: `'none'`): Severity level used to pin and highlight active blockers.
- **`is_resolved`** (`BOOLEAN`, Default: `FALSE`): Tracks whether a reported blocker has been cleared.
- **`resolved_at`** (`TIMESTAMPTZ`, Nullable): Timestamp recorded when a blocker is marked as resolved.
- **`created_at`** (`TIMESTAMPTZ`, Default: `NOW()`): Timestamp when the check-in was submitted.

## Indexes & Constraints
- Composite index on `CheckIn(workspace_id, created_at DESC)` for fast chronological feed loading.
- Partial index on `CheckIn(workspace_id, blocker_severity)` where `is_resolved = FALSE AND blocker_severity != 'none'` for instant active-blocker pinning.
