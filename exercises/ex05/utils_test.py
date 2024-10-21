"""Define unit tests for functions."""

__author__ = "730740592"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_edgecase():
    # Edge Case: Ensure the function handles unconventional input (empty list)
    list = []
    print("Edge Case")
    evens_list = only_evens(list)
    print("Returned value:", evens_list)  # Expected: []


def test_only_evens_returns():
    # Use Case 1: Tests what the function should return
    list = [10, 3, 4, 8, 7]
    print("Use Case 1")
    even_list = only_evens(list)
    print("Returned value: ", even_list)  # Expected: [10, 4, 8]


def test_only_evens_mutate():
    # Use Case 2: Tests how the function does not mutate its input
    list = [4, 7, 1, 7, 6]
    print("Use Case 2")
    only_evens(list)
    print("List after mutation:", list)  # Expected: [4, 7, 1, 7, 6]


def test_sub_edgecase():
    # Edge Case: Ensure function can handle unconventional input (empty list)
    list = []
    print("Edge Case")
    sub_list = sub(list, 0, 2)
    print("Returned list: ", sub_list)  # Expected: []


def test_sub_returns():
    # Use Case 1: Tests what the function should return
    list = [10, 3, 4, 8, 7]
    print("Use Case 1")
    sub_list = sub(list, 1, 4)
    print("Returned list: ", sub_list)  # Expected: [3, 4, 8]


def test_sub_mutate():
    # Use Case 2: Tests how the function does not mutate its input
    list = [4, 7, 1, 7, 6]
    print("Use Case 2")
    sub(list, 1, 3)
    print("List after mutation: ", list)  # Expected: [4, 7, 1, 7, 6]


def test_add_at_index_edgecase():
    # Edge Case: Ensure function can handle unconventional inputs
    print("Edge Case")
    list = [1, 2, 3]
    add_at_index(list, 5, 4)  # Expected: raise IndexError


def test_add_at_index_returns():
    # Use Case 1: Tests what function should return
    list = [10, 3, 4, 6, 9]
    print("Use Case 1")
    add_at_index(list, 5, 2)
    print("Returned list: ", list)  # Expected: [10, 3, 5, 4, 6, 9]


def test_add_at_index_mutate():
    # Use Case 2: Tests how the function mutates its input
    list = [4, 7, 1, 6]
    print("Use Case 2")
    add_at_index(list, 2, 1)
    print("List after mutation: ", list)  # Expected: [4, 2, 7, 1, 6]
