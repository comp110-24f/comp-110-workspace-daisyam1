"""EX03: Wordle"""

__author__ = "730740592"


def input_guess(chars: int) -> str:
    """
    Prompts the user to input a word
    Ensures the input meets the required # of chars

    Arguments: chars (int): required # of chars
    Returns: str: a word with the right # of chars
    """
    # Prompt the user to input a word of the required length
    word: str = input(f"Enter a {chars} character word: ")

    # Loop to check if the input length matches the required number of characters
    while len(word) != chars:
        # If the word length is incorrect, ask user to try again
        word = input(f"That wasn't {chars} chars! Try again: ")

    # Return the valid word with the correct number of characters
    return word


def contains_char(word: str, char: str) -> bool:
    """
    Checks whether a given character is present in a word.

    Arguments:
        word (str): the word to search through.
        char (str): the character to search for.
    Returns:
        bool: True if character is found in word, False otherwise
    Raises:
        AssertionError: If the 'char' argument is not a single character.
    """
    # Ensure that the 'char' argument is exactly one character long
    assert len(char) == 1

    # Initialize index to start searching the word from the beginning
    index = 0

    # Loop through each character in the word
    while index < len(word):
        # If the character matches the target character, return True
        if word[index] == char:
            return True
        # Move to the next character
        index += 1
    # Return False if the character is not found after check word
    return False


# emoji globals
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(user_guess: str, secret_word: str) -> str:
    """
    Converts a user's guess into a string of emojis based on how it matches

    Green box: correct letter in correct position.
    Yellow box: correct letter in wrong position.
    White box: incorrect letter.

    Arguments:
        user_guess (str): word guessed by the user.
        secret_word (str): secret word to match against.

    Returns:
        str: a string of emojis indicating the accuracy
        of each letter in the user's guess.
    """
    # Ensure that both the user guess and the secret word have the same length
    assert len(user_guess) == len(secret_word)

    # Initialize index to start checking each character in the words
    index = 0
    # String to accumulate the emojis representing the guess accuracy
    concat_emojis: str = ""

    # Loop through each character of the user's guess
    while index < (len(secret_word)):
        if user_guess[index] == secret_word[index]:
            # Correct letter and position -> add green box emoji
            concat_emojis += GREEN_BOX
        elif contains_char(secret_word, user_guess[index]):
            # Correct letter but wrong position -> add yellow box emoji
            concat_emojis += YELLOW_BOX
        else:
            # Incorrect letter -> add white box emoji
            concat_emojis += WHITE_BOX

        # Move to the next character
        index += 1

    # Return the final string of emojis
    return concat_emojis


def main(secret: str) -> None:
    """
    The entrypoint of the program and main game loop.

    The user has 6 turns to guess the secret word. After each guess,
    the function outputs a string of emojis indicating how well the
    guess matches the secret word.

    Arguments:
        secret (str): The secret word to be guessed by the user.

    Returns:
        None
    """
    # Initialize turn counter and empty guess
    turns: int = 1
    guess: str = ""

    # Allow the user up to 6 turns to guess the word
    while turns <= 6:
        # Display the current turn number
        print(f"=== Turn {turns}/6 ===")

        # Prompt the user to input a guess of the same length
        # as the secret word
        guess = input_guess(len(secret))

        # Display the emojis representing the accuracy of the guess
        print(emojified(guess, secret))

        # If the guess is correct, announce the win and end the game
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            return
        else:
            # Increment turn counter for the next attempt
            turns += 1

    # If the user uses all turns without guessing correctly,
    # show a failure message.
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
