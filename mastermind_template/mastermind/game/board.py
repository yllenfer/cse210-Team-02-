import random
from game.player import Player
from game.console import Console


# changing branch

class Board:

    def __init__(self):
        # self._item = []
        # self.name = ""
        # self.player = Player(self.name)
        self.console = Console()

    def display_board(self, players):
        """Sets up the board with an entry for each player.

    Args:
        self (Board): an instance of Board.
        :param players:
    """
        self.console.write("--------------------")
        for player in players:
            guess = player.get_guess()
            self.console.write(f"Player {player.get_name()}: {guess.get_guess()}, {guess.get_hint()}")
        self.console.write("--------------------")

    def player_guess_hint(self, player, guess, hint):
        self._item.append([player, guess, hint])
