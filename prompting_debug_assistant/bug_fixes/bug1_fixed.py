def get_even_squares(numbers):
    # Fixed syntax error and modulo logic
    squares = []
    for num in numbers:
        if num % 2 == 0:
            squares.append(num ** 2)
    return squares

# Validation Test Block
if __name__ == "__main__":
    sample_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = get_even_squares(sample_nums)
    print("Calculated squares of even numbers:")
    print(result)
    assert result == [4, 16, 36, 64, 100], "Validation Failed!"
