__author__ = "730740592"


def find_and_remove_max(list: list[int]) -> int:
    """
    Finds the maximum value in a list, removes all occurences of that
    value from the list, and returns the maximum value.
    If the list is empty, returns -1.

    Args:
    list (list[int]): a list of integers from which the max value
        will be found and removed.

    Returns:
    int: the maximum value in the list, or -1 if the list is empty.
    """

    # If the list is empty, return -1 as there is no maximum value.
    if list == []:
        return -1

    # Initialize index and the variable to hold the maximum value.
    i = 0
    max: int = list[0]

    # First loop: Find the maximum value in the list.
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1

    # Second loop: Remove all occurrences of the maximum value from the list.
    i = 0
    while i < len(list):
        if list[i] == max:
            list.pop(i)
        else:
            i += 1

    # Return the maximum value found.
    return max
