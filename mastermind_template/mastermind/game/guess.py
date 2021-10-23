import random


class Guess:

    def __init__(self, player_guess, player_code):
        self._player_guess = player_guess
        self._hint = ""
        self._player_code = player_code
        self._create_hint()

    def _create_hint(self):
        """Generates a hint based on the given code and guess.

    Args:
        self (Board): An instance of Board.

    Returns:
        string: A hint in the form [xxxx]
    """
        for index, letter in enumerate(self._player_guess):
            if self._player_code[index] == letter:
                self._hint += "x"
            elif letter in self._player_code:
                self._hint += "o"
            else:
                self._hint += "*"

    def get_hint(self):
        return self._hint

    def get_guess(self):
        return self._player_guess

    def has_won(self):
        return self._player_guess == self._player_code
