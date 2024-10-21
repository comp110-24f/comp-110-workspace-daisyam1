__author__ = "730740592"

from CQs.cq07.find_max import find_and_remove_max


def test_expected_returns():
    # Use Case 1: Ensure the function returns the expected value
    numbers = [10, 2, 3, 10, 5]
    print("Use Case 1 - Input: [10, 2, 3, 10, 5]")
    max_value = find_and_remove_max(numbers)
    print("Returned value:", max_value)  # Expected: 10
    print()


def test_mutate_input():
    # Use Case 2: Ensure the function mutates the input correctly
    numbers = [4, 7, 1, 7, 6]
    print("Use Case 2 - Input: [4, 7, 1, 7, 6]")
    find_and_remove_max(numbers)
    print("List after removal:", numbers)  # Expected: [4, 1, 6]
    print()


def test_unconventional_input():
    # Edge Case: Ensure the function handles unconventional input (empty list)
    numbers = []
    print("Edge Case - Input: []")
    max_value = find_and_remove_max(numbers)
    print("Returned value:", max_value)  # Expected: -1
    print("List after removal:", numbers)  # Expected: []
    print()
