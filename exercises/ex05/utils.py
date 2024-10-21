"""Implement list utility functions."""

__author__ = "730740592"


def only_evens(list: list[int]) -> list[int]:
    evens = []
    i = 0
    while i < len(list):
        if (list[i] % 2) == 0:
            evens.append(list[i])
        i += 1
    return evens


def sub(list: list[int], start: int, end: int) -> list[int]:
    sublist = []

    if start < 0:
        start = 0
    if end >= len(list):
        end = len(list)
    if len(list) == 0:
        return []

    while start < end:
        sublist.append(list[start])
        start += 1
    return sublist


def add_at_index(list: list[int], elem: int, index: int) -> None:
    if (index >= len(list)) or (index < 0):
        raise IndexError("Index is out of bounds for the input list")
    list.insert(index, elem)
