"""Define unit tests for functions."""

__author__ = "730740592"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_edgecase() -> None:
    # Edge Case: Empty list
    input1: list[int] = []
    assert only_evens(input1) == []


def test_only_evens_returns() -> None:
    # Test Case 1: Mixed numbers
    input2 = [10, 3, 4, 8, 7]
    assert only_evens(input2) == [10, 4, 8]


def test_only_evens_returns_all_odds() -> None:
    # Test Case 2: All odd numbers
    input3 = [1, 3, 5, 7]
    assert only_evens(input3) == []


def test_sub_edgecase() -> None:
    # Edge Case: Empty list
    input4 = []
    assert sub(input4, 0, 2) == []


def test_sub_returns() -> None:
    # Test Case 1: Extract sublist
    input5 = [10, 3, 4, 8, 7]
    assert sub(input5, 1, 4) == [3, 4, 8]


def test_sub_invalid_indices() -> None:
    # Test Case 2: Invalid indices (end index greater than list length)
    input6 = [5, 6, 7]
    assert sub(input6, 0, 10) == [5, 6, 7]


def test_add_at_index_edgecase() -> None:
    # Edge Case: Adding to an empty list at index 0
    input7 = []
    add_at_index(input7, 1, 0)
    assert input7 == [1]


def test_add_at_index_one_element() -> None:
    # Test Case 1: Adding to a list with one element
    input8 = [10]
    add_at_index(input8, 5, 1)
    assert input8 == [10, 5]


def test_add_at_index_multiple_elements() -> None:
    # Test Case 2: Adding to a list with multiple elements
    input9 = [1, 2, 3]
    add_at_index(input9, 9, 1)
    assert input9 == [1, 9, 2, 3]
