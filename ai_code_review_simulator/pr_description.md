# Pull Request: Add Sliding-Window API Rate Limiter

## Summary
Implements an in-memory sliding-window rate limiter (`SlidingWindowRateLimiter`) to protect public API endpoints from request bursts and abuse. Tracks per-client timestamps, enforces configurable quota limits, calculates retry/reset windows, and exposes per-client usage statistics.

## Changes
- Added `SlidingWindowRateLimiter` and `RateLimitResult` dataclass in `rate_limiter.py` (~95 LOC)
- Implemented automatic timestamp eviction (`_evict_expired`) using `collections.deque` for O(1) pops
- Added client quota reset (`reset_client`) and metrics reporting (`get_client_stats`)
- Added 5 unit tests covering quota enforcement, window expiration, input validation, and stats tracking in `test_rate_limiter.py` (~55 LOC)

## Context
~150 LOC total across feature and test files. Related issue: #18 (API Abuse & Burst Protection).
Motivation: Several unauthenticated endpoints currently lack request throttling, risking degraded latency during traffic spikes. This lightweight module provides deterministic rate limiting with zero external dependencies.
