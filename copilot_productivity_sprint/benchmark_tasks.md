# Benchmark Tasks

This document defines three benchmark coding tasks designed to be solved within 15–30 minutes each, used to compare manual vs. AI-assisted development workflows.

---

## Task 1 - User Registration CRUD Endpoint

**Requirements**: Implement a REST API endpoint `POST /users` (using Python FastAPI/Flask or Node.js Express) that validates incoming user data, stores the user in memory or a lightweight database, and returns the created record.

**Inputs**: JSON payload containing `{ "name": string, "email": string, "role": string (optional, defaults to "user") }`

**Outputs**: JSON object of the created user with a generated unique `id` and `created_at` timestamp.

**Acceptance Criteria**:
- Returns HTTP `201 Created` with the stored user object on valid input.
- Returns HTTP `400 Bad Request` if `name` is empty or `email` format is invalid.
- Returns HTTP `409 Conflict` if the email is already registered.
- Includes at least 3 unit/integration tests covering success and error cases.

---

## Task 2 - Log File Error Aggregator CLI

**Requirements**: Write a command-line script that parses a server log file, filters entries by severity level (`ERROR` and `WARN`), groups recurring error messages, and outputs a summary report sorted by frequency.

**Inputs**: Path to a `.log` file where each line follows the format `[YYYY-MM-DD HH:MM:SS] [LEVEL] Message`.

**Outputs**: A formatted summary printed to the console (and optionally saved to `summary.json`) listing total counts per severity level and the top 5 most frequent error messages.

**Acceptance Criteria**:
- Accurately parses valid log lines and gracefully skips malformed lines without crashing.
- Correctly counts and sorts duplicate messages in descending order.
- Handles missing or unreadable file paths with a clear error message and non-zero exit code.
- Includes unit tests verifying parsing, sorting, and edge cases (empty file, malformed lines).

---

## Task 3 - Rate Limiter Utility (Token Bucket / Sliding Window)

**Requirements**: Implement a reusable in-memory rate limiter class/module that restricts how many requests a specific client identifier (e.g., IP address or user ID) can make within a given time window.

**Inputs**: Configuration parameters (`max_requests: int`, `window_seconds: int`) and method calls `allow_request(client_id: str)`.

**Outputs**: Boolean (`True` if the request is permitted, `False` if the rate limit is exceeded).

**Acceptance Criteria**:
- Allows up to `max_requests` within `window_seconds` for a given `client_id`.
- Blocks excess requests (`False`) until the time window resets or old timestamps expire.
- Tracks different `client_id` values independently.
- Includes automated tests simulating time progression and concurrent/burst requests.
