from game.console import Console
from game.player import Player
from game.roster import Roster
from game.guess import Guess
from game.board import Board


class Director:

    def __init__(self):
        self._board = Board()
        self.console = Console()
        self.roster = Roster()
        self._keep_playing = True
        self.current_player_guess = ""

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self.do_outputs()
            self._do_updates()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to
        the roster.

        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self.console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            guess = Guess("----", player.get_code())
            player.set_guess(guess)
            self.roster.add_player(player)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the move from the current player.

        Args:
            self (Director): An instance of Director.
        """
        # display the game board
        self._board.display_board(self.roster.players)
        # get next player's move
        player = self.roster.get_current()
        self.console.write(f"{player.get_name()}'s turn:")
        self.current_player_guess = input("What is your guess?: ")
        guess = Guess(self.current_player_guess, player.get_code())
        player.set_guess(guess)

    def _do_updates(self):
        """Updates the important game information for each round of play. In
        this case, that means updating the board with the current move.

        Args:
            self (Director): An instance of Director.
        """
        player = self.roster.get_current()
        guess = player.get_guess()
        if guess.has_won():
            self._keep_playing = False
        else:
            self.roster.next_player()

    def do_outputs(self):
        player = self.roster.get_current()
        if not self._keep_playing:
            self.console(f"Player{player.get_name()} has won!")
