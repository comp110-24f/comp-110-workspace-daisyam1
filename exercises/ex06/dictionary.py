"""Dictionary Utility Functions Practice"""

__author__ = "730740592"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate key found!")
        # Store the key in a tempory variable before switching
        temp = key
        # Assign the value as the key and the temp as the value
        inverted_dict[value] = temp
    return inverted_dict


def favorite_color(fav_colors: dict[str, str]) -> str:
    color_count = {}
    for name, color in fav_colors.items():
        # Count occurences of each color
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    # Find the most frequent color, with a preference for the first if a tie
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
    result = {}
    for elem in input_list:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
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
    # Check if the day exists in the dictionary
    if day in attendance_log:
        # Add the student to the list if they are not already present
        attendance_log[day].append(student)
    else:
        # If the day is not in the dictionary, create a new entry with the student
        attendance_log[day] = [student]
