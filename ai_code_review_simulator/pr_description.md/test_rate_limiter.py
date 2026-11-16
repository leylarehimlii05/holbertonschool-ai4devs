"""Unit tests for SlidingWindowRateLimiter."""

from datetime import datetime, timedelta, timezone
import unittest
from rate_limiter import SlidingWindowRateLimiter


class TestSlidingWindowRateLimiter(unittest.TestCase):
    def setUp(self) -> None:
        self.base_time = datetime(2026, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        self.limiter = SlidingWindowRateLimiter(max_requests=3, window_seconds=60)

    def test_allows_requests_under_limit(self) -> None:
        res1 = self.limiter.check_request("user_1", self.base_time)
        res2 = self.limiter.check_request("user_1", self.base_time + timedelta(seconds=10))
        self.assertTrue(res1.allowed)
        self.assertEqual(res1.remaining, 2)
        self.assertTrue(res2.allowed)
        self.assertEqual(res2.remaining, 1)

    def test_blocks_requests_exceeding_limit(self) -> None:
        for i in range(3):
            self.limiter.check_request("user_1", self.base_time + timedelta(seconds=i))
        blocked = self.limiter.check_request("user_1", self.base_time + timedelta(seconds=10))
        self.assertFalse(blocked.allowed)
        self.assertEqual(blocked.remaining, 0)
        self.assertEqual(blocked.reset_after_seconds, 50.0)

    def test_window_expiration_restores_quota(self) -> None:
        for i in range(3):
            self.limiter.check_request("user_1", self.base_time + timedelta(seconds=i))
        after_window = self.base_time + timedelta(seconds=61)
        res = self.limiter.check_request("user_1", after_window)
        self.assertTrue(res.allowed)
        self.assertEqual(res.remaining, 2)

    def test_invalid_inputs_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            SlidingWindowRateLimiter(max_requests=0, window_seconds=60)
        with self.assertRaises(ValueError):
            self.limiter.check_request("   ")

    def test_reset_and_stats(self) -> None:
        self.limiter.check_request("user_2", self.base_time)
        self.limiter.reset_client("user_2")
        stats = self.limiter.get_client_stats("user_2")
        self.assertEqual(stats["active_requests"], 0)
        self.assertEqual(stats["remaining_quota"], 3)


if __name__ == "__main__":
    unittest.main()
