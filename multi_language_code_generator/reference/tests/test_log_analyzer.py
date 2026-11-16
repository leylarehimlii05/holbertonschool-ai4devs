#!/usr/bin/env python3
"""Unit tests for the reference LogAnalyzer implementation (12 test cases)."""

import os
import sys
import tempfile
import unittest

# Ensure parent directory is in sys.path so log_analyzer can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    # Test 1: Empty input list
    def test_01_empty_logs(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["total_bandwidth_bytes"], 0)
        self.assertEqual(result["top_endpoints"], [])

    # Test 2: Whitespace-only lines
    def test_02_whitespace_lines(self):
        result = self.analyzer.analyze(["   ", "\n", "\t\n"])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    # Test 3: Single valid 200 OK request
    def test_03_single_valid_request(self):
        lines = ['10.0.0.1 - - [17/Nov/2026:10:00:00 +0000] "GET /home HTTP/1.1" 200 512']
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["unique_visitors"], 1)
        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["total_bandwidth_bytes"], 512)
        self.assertEqual(result["top_endpoints"], [{"path": "/home", "count": 1}])

    # Test 4: Mixed 2xx, 4xx, and 5xx status codes
    def test_04_mixed_errors_and_error_rate(self):
        lines = [
            '192.168.1.1 - - [17/Nov/2026:10:01:00 +0000] "GET /index.html HTTP/1.1" 200 1024',
            '192.168.1.1 - - [17/Nov/2026:10:02:00 +0000] "POST /login HTTP/1.1" 401 256',
            '192.168.1.2 - - [17/Nov/2026:10:03:00 +0000] "GET /api/data HTTP/1.1" 500 512',
            '192.168.1.3 - - [17/Nov/2026:10:04:00 +0000] "GET /index.html HTTP/1.1" 200 1024',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 4)
        self.assertEqual(result["unique_visitors"], 3)
        self.assertEqual(result["error_count"], 2)
        self.assertEqual(result["error_rate"], 50.0)
        self.assertEqual(result["total_bandwidth_bytes"], 2816)

    # Test 5: Missing byte size represented by '-'
    def test_05_dash_byte_size(self):
        lines = [
            '10.0.0.5 - - [17/Nov/2026:10:05:00 +0000] "HEAD /health HTTP/1.1" 204 -',
            '10.0.0.5 - - [17/Nov/2026:10:06:00 +0000] "GET /about HTTP/1.1" 200 2048',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["total_bandwidth_bytes"], 2048)

    # Test 6: Malformed lines are skipped gracefully
    def test_06_malformed_lines_skipped(self):
        lines = [
            "INVALID_LOG_LINE",
            "127.0.0.1 broken entry",
            '10.0.0.2 - - [17/Nov/2026:10:07:00 +0000] "GET /valid HTTP/1.1" 200 100',
            '10.0.0.3 - - [17/Nov/2026:10:08:00 +0000] "GET /badstatus HTTP/1.1" ABC 100',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["unique_visitors"], 1)
        self.assertEqual(result["total_bandwidth_bytes"], 100)

    # Test 7: Top 3 endpoints sorting and alphabetical tie-breaking
    def test_07_top_endpoints_tie_breaking(self):
        lines = [
            '10.0.0.1 - - [17/Nov/2026:10:09:00 +0000] "GET /b HTTP/1.1" 200 100',
            '10.0.0.1 - - [17/Nov/2026:10:09:01 +0000] "GET /b HTTP/1.1" 200 100',
            '10.0.0.1 - - [17/Nov/2026:10:09:02 +0000] "GET /a HTTP/1.1" 200 100',
            '10.0.0.1 - - [17/Nov/2026:10:09:03 +0000] "GET /a HTTP/1.1" 200 100',
            '10.0.0.1 - - [17/Nov/2026:10:09:04 +0000] "GET /d HTTP/1.1" 200 100',
            '10.0.0.1 - - [17/Nov/2026:10:09:05 +0000] "GET /c HTTP/1.1" 200 100',
        ]
        result = self.analyzer.analyze(lines)
        expected_top = [
            {"path": "/a", "count": 2},
            {"path": "/b", "count": 2},
            {"path": "/c", "count": 1},
        ]
        self.assertEqual(result["top_endpoints"], expected_top)

    # Test 8: Error rate rounding to 2 decimal places
    def test_08_error_rate_rounding(self):
        lines = [
            '10.0.0.1 - - [17/Nov/2026:10:10:00 +0000] "GET /ok1 HTTP/1.1" 200 100',
            '10.0.0.1 - - [17/Nov/2026:10:10:01 +0000] "GET /ok2 HTTP/1.1" 200 100',
            '10.0.0.1 - - [17/Nov/2026:10:10:02 +0000] "GET /err HTTP/1.1" 404 100',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["error_rate"], 33.33)

    # Test 9: 3xx redirects are NOT counted as errors
    def test_09_redirects_not_errors(self):
        lines = [
            '10.0.0.1 - - [17/Nov/2026:10:11:00 +0000] "GET /old HTTP/1.1" 301 0',
            '10.0.0.1 - - [17/Nov/2026:10:11:01 +0000] "GET /temp HTTP/1.1" 302 0',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    # Test 10: All requests failing gives 100.0% error rate
    def test_10_all_errors(self):
        lines = [
            '10.0.0.1 - - [17/Nov/2026:10:12:00 +0000] "GET /fail1 HTTP/1.1" 502 0',
            '10.0.0.2 - - [17/Nov/2026:10:12:01 +0000] "GET /fail2 HTTP/1.1" 503 0',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["error_count"], 2)
        self.assertEqual(result["error_rate"], 100.0)

    # Test 11: parse_line returns expected dictionary structure
    def test_11_parse_line_structure(self):
        line = '172.16.0.1 - - [17/Nov/2026:10:13:00 +0000] "DELETE /api/item/5 HTTP/1.1" 200 64'
        parsed = self.analyzer.parse_line(line)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed["ip"], "172.16.0.1")
        self.assertEqual(parsed["method"], "DELETE")
        self.assertEqual(parsed["endpoint"], "/api/item/5")
        self.assertEqual(parsed["status"], 200)
        self.assertEqual(parsed["bytes"], 64)

    # Test 12: File streaming via analyze_file
    def test_12_analyze_file(self):
        content = (
            '10.0.0.1 - - [17/Nov/2026:10:14:00 +0000] "GET /a HTTP/1.1" 200 300\n'
            '10.0.0.2 - - [17/Nov/2026:10:14:01 +0000] "GET /b HTTP/1.1" 404 150\n'
        )
        with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        try:
            result = self.analyzer.analyze_file(tmp_path)
            self.assertEqual(result["total_requests"], 2)
            self.assertEqual(result["unique_visitors"], 2)
            self.assertEqual(result["error_count"], 1)
            self.assertEqual(result["total_bandwidth_bytes"], 450)
        finally:
            os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
