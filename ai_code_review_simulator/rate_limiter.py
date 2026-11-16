"""Sliding-window API rate limiter and request quota tracker."""

from collections import deque
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Deque, Dict, Optional


@dataclass
class RateLimitResult:
    allowed: bool
    remaining: int
    reset_after_seconds: float
    client_id: str


class SlidingWindowRateLimiter:
    """Tracks per-client API requests within a configurable time window."""

    def __init__(self, max_requests: int = 60, window_seconds: int = 60) -> None:
        if max_requests <= 0:
            raise ValueError("max_requests must be greater than zero")
        if window_seconds <= 0:
            raise ValueError("window_seconds must be greater than zero")

        self.max_requests = max_requests
        self.window = timedelta(seconds=window_seconds)
        self._requests: Dict[str, Deque[datetime]] = {}
        self._blocked_counts: Dict[str, int] = {}

    def _evict_expired(self, client_id: str, now: datetime) -> Deque[datetime]:
        timestamps = self._requests.setdefault(client_id, deque())
        cutoff = now - self.window
        while timestamps and timestamps[0] <= cutoff:
            timestamps.popleft()
        return timestamps

    def check_request(
        self, client_id: str, timestamp: Optional[datetime] = None
    ) -> RateLimitResult:
        if not client_id or not client_id.strip():
            raise ValueError("client_id cannot be empty")

        now = timestamp or datetime.now(timezone.utc)
        timestamps = self._evict_expired(client_id, now)

        if len(timestamps) >= self.max_requests:
            self._blocked_counts[client_id] = self._blocked_counts.get(client_id, 0) + 1
            oldest = timestamps[0]
            reset_after = max(0.0, (oldest + self.window - now).total_seconds())
            return RateLimitResult(
                allowed=False,
                remaining=0,
                reset_after_seconds=round(reset_after, 2),
                client_id=client_id,
            )

        timestamps.append(now)
        remaining = self.max_requests - len(timestamps)
        oldest = timestamps[0]
        reset_after = max(0.0, (oldest + self.window - now).total_seconds())
        return RateLimitResult(
            allowed=True,
            remaining=remaining,
            reset_after_seconds=round(reset_after, 2),
            client_id=client_id,
        )

    def reset_client(self, client_id: str) -> None:
        self._requests.pop(client_id, None)
        self._blocked_counts.pop(client_id, None)

    def get_client_stats(self, client_id: str) -> Dict[str, int]:
        now = datetime.now(timezone.utc)
        active = len(self._evict_expired(client_id, now))
        return {
            "active_requests": active,
            "remaining_quota": max(0, self.max_requests - active),
            "blocked_total": self._blocked_counts.get(client_id, 0),
        }
