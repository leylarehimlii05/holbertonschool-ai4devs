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
4. Edge CasesEmpty File: Contains 0 bytes or only whitespace/newlines; must return zeroed metrics and an empty top_endpoints list without division-by-zero errors.Malformed Entries: Corrupted lines, missing fields, or non-numeric status codes must be skipped gracefully while incrementing a separate internal warning/skipped counter (must not crash).Missing Byte Size (-): Servers often log - instead of 0 when no body is returned (e.g., HTTP 204 or 304); - must be parsed as 0 bytes.Tie-Breaking in Top Endpoints: When multiple endpoints have the exact same hit count, they must be sorted lexicographically (A–Z) so outputs match identically across all target languages.Large Files / Memory Efficiency: Streaming line-by-line processing is preferred over loading entire multi-gigabyte files into memory at once.5. Test CasesTest Case IDInput ScenarioSample Input / ConditionExpected Output SummaryTC-01log_empty.txtCompletely empty file (0 lines)total_requests: 0, unique_visitors: 0, error_rate: 0.0, total_bandwidth_bytes: 0, top_endpoints: []TC-02log_single_valid.txt1 valid 200 OK line (10.0.0.1, /home, 512 bytes)total_requests: 1, unique_visitors: 1, error_count: 0, error_rate: 0.0, total_bandwidth_bytes: 512, top_endpoints: [{"path": "/home", "count": 1}]TC-03log_mixed_errors.txt4 requests from 2 unique IPs: three 200s and one 500 error (1024 bytes each)total_requests: 4, unique_visitors: 2, error_count: 1, error_rate: 25.0, total_bandwidth_bytes: 4096TC-04log_malformed_and_dash.txt2 valid lines (one with - bytes, one with 2048 bytes) + 2 corrupted lines (INVALID_LINE, 127.0.0.1 broken)total_requests: 2 (malformed lines ignored), total_bandwidth_bytes: 2048TC-05log_top_endpoints_tie.txt5 requests across 4 endpoints: /b (2), /a (2), /c (1), /d (1)top_endpoints returns top 3 in exact order: [{"path": "/a", "count": 2}, {"path": "/b", "count": 2}, {"path": "/c", "count": 1}]
