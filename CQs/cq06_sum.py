"""Summing the elements of a list using different loops"""

__author__ = "730740592"


def w_sum(vals: list[float]) -> float:
    """Takes list of floats and returns the sum
    of all the elements."""
    i: int = 0
    sum: float = 0.0
    # While loop that loops through the list to add each number
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Calculates the sum using a for...in... loop"""
    sum: float = 0.0
    # For... in... loop that loops through and adds each element together
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Calculates the sum through a range loop"""
    sum: float = 0.0
    # For...in range(...) loop that adds all elements
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum
