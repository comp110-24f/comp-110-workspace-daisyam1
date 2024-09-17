"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730740592"


# takes a word as user input to use in the other functions
# quits the program and displays an error message if input format is incorrect
def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


# takes a character as user input to use in the other functions
# quits the program and displays an error message if input format is incorrect
def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


# counts instances that a character is present in a word and where
# prints the total number of instances at the end for the user
def contains_char(word: str, letter: str) -> None:
    instances: int = 0
    print("Searching for " + str(letter) + " in " + str(word))
    if word[0] == letter:
        print(letter + " found at index 0")
        instances = instances + 1

    if word[1] == letter:
        print(letter + " found at index 1")
        instances = instances + 1

    if word[2] == letter:
        print(letter + " found at index 2")
        instances = instances + 1

    if word[3] == letter:
        print(letter + " found at index 3")
        instances = instances + 1

    if word[4] == letter:
        print(letter + " found at index 4")
        instances = instances + 1

    if instances > 1:
        print(str(instances) + " instances of " + letter + " found in " + word)
    elif instances == 1:
        print(str(instances) + " instance of " + letter + " found in " + word)
    elif instances == 0:
        print("No instances of " + letter + " found in " + word)


# main function that calls all the functions
# ties the whole program and the function definitions together
def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
