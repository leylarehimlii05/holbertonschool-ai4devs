# Cross-Language Specification - Web Server Log Analyzer

## 1. Algorithm Description
The **Log Analyzer** parses standard Apache/Nginx Combined Log Format files line by line and aggregates traffic metrics. For each valid log entry, the algorithm extracts the client IP address, HTTP status code, requested endpoint path, and response size in bytes.

It computes:
1. **Total Requests:** Count of all valid parsed log lines.
2. **Unique Visitors:** Count of distinct client IP addresses.
3. **Error Rate:** Percentage of requests returning HTTP status codes `400`–`599` (`(error_count / total_requests) * 100`), rounded to 2 decimal places (`0.0` if total requests is 0).
4. **Top Endpoints:** Top 3 most frequently requested paths, sorted by request count descending (tie-breaker: alphabetical order by path).
5. **Total Bandwidth:** Sum of response bytes across all valid requests (`-` treated as `0`).

---

## 2. Input Format
- **Source:** Plain-text UTF-8 log file (`.log` or `.txt`) passed via file path argument or standard input.
- **Line Pattern (Apache/Nginx Combined Log Format):**
  `<IP> - - [<TIMESTAMP>] "<METHOD> <ENDPOINT> <PROTOCOL>" <STATUS_CODE> <BYTES>`
- **Example Line:**
  `192.168.1.10 - - [17/Nov/2026:10:15:32 +0000] "GET /api/users HTTP/1.1" 200 1024`

---

## 3. Output Format
A deterministic JSON object printed to `stdout` (or written to a specified output file):

```json
{
  "total_requests": 4,
  "unique_visitors": 2,
  "error_count": 1,
  "error_rate": 25.0,
  "total_bandwidth_bytes": 3584,
  "top_endpoints": [
    { "path": "/api/users", "count": 2 },
    { "path": "/index.html", "count": 1 },
    { "path": "/login", "count": 1 }
  ]
}
