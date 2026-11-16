def get_last_n_items(items, n):
    """Return the last n items from the given list in original order."""
    if not items or n <= 0:
        return []
    if n >= len(items):
        return items[:]
    return items[-n:]


if __name__ == "__main__":
    sample = [10, 20, 30, 40, 50]
    assert get_last_n_items(sample, 3) == [30, 40, 50]
    assert get_last_n_items(sample, 1) == [50]
    assert get_last_n_items(sample, 10) == [10, 20, 30, 40, 50]
    assert get_last_n_items(sample, 0) == []
    print("bug1_fixed.py: All 4 test cases passed!")
