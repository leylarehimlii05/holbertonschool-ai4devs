#!/usr/bin/env python3
"""Reference implementation of the Web Server Log Analyzer."""

from collections import Counter
import json
import re
import sys
from typing import Dict, List, Optional


LOG_PATTERN = re.compile(
    r'^(\S+)\s+\S+\s+\S+\s+\[([^\]]+)\]\s+"(\S+)\s+(\S+)\s+([^"]+)"\s+(\d{3})\s+(\S+)$'
)


class LogAnalyzer:
    """Parses Apache/Nginx Combined Log Format lines and computes traffic metrics."""

    def parse_line(self, line: str) -> Optional[Dict]:
        """Parse a single log line. Returns None if the line is malformed."""
        line = line.strip()
        if not line:
            return None

        match = LOG_PATTERN.match(line)
        if not match:
            return None

        ip, timestamp, method, endpoint, protocol, status_str, bytes_str = match.groups()

        try:
            status = int(status_str)
        except ValueError:
            return None

        if bytes_str == "-":
            byte_size = 0
        else:
            try:
                byte_size = int(bytes_str)
                if byte_size < 0:
                    return None
            except ValueError:
                return None

        return {
            "ip": ip,
            "timestamp": timestamp,
            "method": method,
            "endpoint": endpoint,
            "protocol": protocol,
            "status": status,
            "bytes": byte_size,
        }

    def analyze(self, lines: List[str]) -> Dict:
        """Analyze a list of log lines and return aggregated statistics."""
        total_requests = 0
        unique_ips = set()
        error_count = 0
        total_bandwidth_bytes = 0
        endpoint_counts = Counter()

        for line in lines:
            parsed = self.parse_line(line)
            if parsed is None:
                continue

            total_requests += 1
            unique_ips.add(parsed["ip"])
            if 400 <= parsed["status"] <= 599:
                error_count += 1
            total_bandwidth_bytes += parsed["bytes"]
            endpoint_counts[parsed["endpoint"]] += 1

        error_rate = round((error_count / total_requests) * 100, 2) if total_requests > 0 else 0.0

        # Sort by count descending, then alphabetically by endpoint path ascending
        sorted_endpoints = sorted(
            endpoint_counts.items(),
            key=lambda item: (-item[1], item[0]),
        )[:3]

        top_endpoints = [
            {"path": path, "count": count} for path, count in sorted_endpoints
        ]

        return {
            "total_requests": total_requests,
            "unique_visitors": len(unique_ips),
            "error_count": error_count,
            "error_rate": error_rate,
            "total_bandwidth_bytes": total_bandwidth_bytes,
            "top_endpoints": top_endpoints,
        }

    def analyze_file(self, filepath: str) -> Dict:
        """Stream a log file line-by-line and return aggregated statistics."""
        def _line_generator():
            with open(filepath, "r", encoding="utf-8") as f:
                for line in f:
                    yield line

        return self.analyze(_line_generator())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer.py <path_to_log_file>", file=sys.stderr)
        sys.exit(1)

    analyzer = LogAnalyzer()
    result = analyzer.analyze_file(sys.argv[1])
    print(json.dumps(result, indent=2))
