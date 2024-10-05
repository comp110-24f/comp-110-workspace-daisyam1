"""EX04: List Utility Functions"""

__author__ = "730740592"


def all(input: list[int], num: int) -> bool:
    """
    Checks if all elements in the input list are equal to a given number.

    Args:
        input (list[int]): the list of integers to check.
        num(int): the number to compare each element to.

    Returns:
        bool: True if all elements in the list are equal to the given number, False otherwise.
    """
    # Initialize the index for iteration
    i: int = 0
    # Counter to track how many elements match the number
    counter: int = 0
    # Iterate through the list to check each element
    while i < len(input):
        if input[i] == num:
            # Increment counter if the element matches the number
            counter += 1
        i += 1
    # Return True if all elements matched the number, otherwise return False.
    if counter == len(input):
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """
    Finds the maximum value in a list of integers.

    Args:
        input (list[int]): the list of integers to find the maximum value from.

    Returns:
        int: the maximum integer in the list

    Raises:
        ValueError: If the input list is empty.
    """
    # Raise an error for an empty list
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # Initialize the index for iteration
    i: int = 0
    # Assume the first element is the maximum
    max_value: int = input[0]
    # Iterate through the list to find the maximum value
    while i < len(input):
        if input[i] > max_value:
            # Update the maximum if a greater element is found
            max_value = input[i]
        i += 1
    # Return the maximum value found
    return max_value


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """
    Checks whether two lists of integers are equal.

    Args:
        input1 (list[int]): the first list to compare.
        input2 (list[int]): the second list to compare.

    Returns:
        bool: True if the two lists are identical, False otherwise.
    """
    # Directly compares the two lists
    if input1 == input2:
        return True
    else:
        return False


def extend(a: list[int], b: list[int]) -> None:
    """
    Extends the first list by appending all elements from the second list.

    Args:
        a (list[int]): the list to be extended.
        b (list[int]): the list whose elements will be added to the first list.

    Returns:
        None: This function modifies the first list in place.
    """
    # Initialize the index for iteration
    i = 0
    # Iterate through the second list and append each element to the first list
    while i < len(b):
        a.append(b[i])
        i += 1
