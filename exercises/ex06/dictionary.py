"""Dictionary Utility Functions Practice"""

__author__ = "730740592"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverted the keys and values of a given dictionary."""
    inverted_dict = {}
    for key, value in input_dict.items():
        # Raise error if the value is already used as a key in inverted_dict
        if value in inverted_dict:
            raise KeyError("Duplicate key found!")
        # Store the key in a tempory variable before switching
        temp = key
        # Assign the value as the key and the temp as the value
        inverted_dict[value] = temp
    return inverted_dict


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Determines the most frequently occuring color
    in a dictionary of favorite colors."""
    color_count = {}
    for name, color in fav_colors.items():
        # Count occurences of each color
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    # Initialize variables to track the most frequent color and its count
    most_frequent: str = ""
    max_count = 0
    for name, color in fav_colors.items():
        if color_count[color] > max_count:
            most_frequent = color
            max_count = color_count[color]
        elif color_count[color] == max_count and most_frequent is None:
            most_frequent = color  # Keeps the first occuring color in case of a tie
    return most_frequent


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the occurrences of each unique element in a list."""
    result = {}
    for elem in input_list:
        # If the element is already in the dictionary, increment its count
        if elem in result:
            result[elem] += 1
        else:
            # Initialize the count to 1 for the new element
            result[elem] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Groups words by their starting letter."""
    result = {}
    for word in words:
        first_letter = word[0].lower()  # Get the first letter in lowercase
        if first_letter not in result:
            result[first_letter] = (
                []
            )  # Initialize an empty list for the letter if not present
        result[first_letter].append(word)  # Add the word to the list for that letter
    return result


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates the attendance log with a student's presence on a specific day."""
    # Check if the day exists in the dictionary
    if day in attendance_log:
        # Add the student to the list if they are not already present
        attendance_log[day].append(student)
    else:
        # If the day is not in the dictionary, create a new entry with the student
        attendance_log[day] = [student]
