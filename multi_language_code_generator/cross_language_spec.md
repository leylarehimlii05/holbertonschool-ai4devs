# Cross-Language Specification - Log Analyzer

## Algorithm
Parse Apache/Nginx access log files line by line and compute the following metrics:
- **Total requests:** Count of all valid log entries.
- **Unique visitors:** Count of distinct client IP addresses.
- **Error rate:** Percentage of requests with HTTP status codes 400 to 599 (`(error_count / total_requests) * 100`), rounded to 2 decimal places (`0.0` when total requests is `0`).
- **Top endpoints:** Top 3 most requested URL paths sorted by count descending (alphabetical tie-breaker).
- **Total bandwidth:** Sum of response byte sizes (`-` treated as `0`).

## Inputs
- Plain-text UTF-8 Apache/Nginx Combined Log Format file (`.log` or `.txt`) passed via file path.
- Line format: `IP - - [TIMESTAMP] "METHOD ENDPOINT PROTOCOL" STATUS_CODE BYTES`
- Sample line: `192.168.1.10 - - [17/Nov/2026:10:15:32 +0000] "GET /api/users HTTP/1.1" 200 1024`

## Outputs
- JSON object printed to stdout with aggregated statistics:

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
Edge Cases
Empty file: log_empty.txt (0 bytes or whitespace only) returns 0 for all numeric metrics and an empty top_endpoints list without division-by-zero errors.

Malformed entry: Corrupted or incomplete lines are skipped gracefully without crashing the program.

Missing byte size (-): Response sizes recorded as - (such as HTTP 204/304) are parsed as 0 bytes.

Tie-breaking: Endpoints with equal request counts are sorted lexicographically (A-Z) for deterministic cross-language output.

Large files: Processed line-by-line as a stream rather than loading the entire file into memory.

Test Cases
log_empty.txt -> 0 total requests, 0 unique visitors, 0.0 error rate, 0 bandwidth, [] top endpoints.

log_single.txt -> 1 valid 200 line (10.0.0.1, /home, 512 bytes) -> 1 request, 1 unique visitor, 0.0 error rate, 512 bytes.

log_small.txt -> 100 requests across 15 unique IPs with 20 500/404 errors -> 100 requests, 15 unique visitors, 20.0 error rate.

log_malformed.txt -> 2 valid lines (one with - bytes, one with 2048 bytes) + 2 malformed lines -> 2 valid requests, 2048 bytes (malformed lines ignored).

log_tie.txt -> /b (2 hits), /a (2 hits), /c (1 hit), /d (1 hit) -> top_endpoints returns /a (2), /b (2), /c (1) in exact order.
