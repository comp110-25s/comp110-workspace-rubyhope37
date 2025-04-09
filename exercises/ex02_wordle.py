"""WORDLE"""

__author__: str = "730486387"


def contains_char(word: str, char: str) -> bool:
    """Checks if character is present in word"""
    assert len(char) == 1, f"len('{char}') is not 1"  # checks single character
    index: int = 0  # intialize index to start with first character
    while index < len(word):  # iterates through each character of the word
        if word[index] == char:  # check if character matches
            return True
        index = index + 1  # moves to next character in word
    return False


def emojified(guess: str, secret: str) -> str:
    """Converts guessed word into a box color"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"  # tells player letter is not present in word
    GREEN_BOX: str = (
        "\U0001F7E9"  # tells player letter is present and in correct order of word
    )
    YELLOW_BOX: str = (
        "\U0001F7E8"  # tells play letter is present but not in correct order of word
    )
    result: str = ""  # initializes an empty string
    index: int = 0  # initializes index to start at first character
    while index < len(guess):  # loops through each letter of the guessed word
        if (
            guess[index] == secret[index]
        ):  # means there was a correct letter in correct order
            result = result + GREEN_BOX
        elif contains_char(
            secret, guess[index]
        ):  # means there was a correct letter in wrong order
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX  # letter not present in secret word
        index = index + 1  # moves to the next character of guessed word
    return result  # returns the final emoji display


def input_guess(expected_length: int) -> str:
    """Prompts guesser for expected length of word"""
    guess: str = input(
        f"Enter a {expected_length} character word: "
    )  # tells player to guess a word
    while (
        len(guess) != expected_length
    ):  # continues to tell player to guess until their guessed word is x amount of characters
        guess = input(
            f"That wasn't {expected_length} chars! Try again: "
        )  # lets guesser know how many characters secret word is
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    max_turns: int = (
        6  # lets player know they have maximum of 6 attempts to guess secret word
    )
    turn_number: int = 1  # starts at turn 1
    while turn_number <= max_turns:  # game continues until maximum attempts are tried
        print(
            f"=== Turn {turn_number}/{max_turns} ==="
        )  # tells player what turn number they are on
        guess: str = input_guess(
            len(secret)
        )  # variable representing the word that the player guesses
        emoji_display: str = emojified(
            guess, secret
        )  # converts guessed word to emoji colored boxes
        print(emoji_display)  # dislays the emoji colored boxes
        if guess == secret:  # if players guessed word is same as secret word
            print(
                f"You won in {turn_number}/{max_turns} turns!"
            )  # tells player the won game
            return  # returns nothing and exits the game
        else:  # otherwise players guessed word was not same as secret word
            turn_number = (
                turn_number + 1
            )  # increases turn number 1 closer to maximum turn number
    print(
        f"X/{max_turns} - Sorry, try again tomorrow!"
    )  # secret word not guessed in maximum amount of turns and tells player they lost the game


if __name__ == "__main__":
    main(secret="codes")  # the secret word for the game is "codes"
