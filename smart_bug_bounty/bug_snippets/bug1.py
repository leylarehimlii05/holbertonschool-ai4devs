def get_last_n_items(items, n):
    """Return the last n items from the given list in original order."""
    if not items or n <= 0:
        return []
    if n >= len(items):
        return items[:]
    # Bug: slicing with -(n - 1) drops the first required element (off-by-one)
    return items[-(n - 1):]


if __name__ == "__main__":
    sample = [10, 20, 30, 40, 50]
    print("Expected [30, 40, 50], Got:", get_last_n_items(sample, 3))
