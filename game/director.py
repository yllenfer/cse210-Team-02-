from game.puzzle import Puzzle
from game.parachute import Parachute

class Director:
    """
    Directs the game and initializes all classes in the game

    """
    def __init__(self):
        self.puzzle = Puzzle()
        self.keep_playing = True
        self.parachute = Parachute()

    def start_game(self):
        """
        Starts the game and grabs inputs and displays outputs and updates the game each turn.
        """
        while self.keep_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def do_outputs(self):
        """
        Draws the parachute man and displays the word on the screen

        """
        self.puzzle.draw_word()
        self.parachute.draw_parachute()
        
    def get_inputs(self):
        """
        Gets the input from the user in the form of a letter
        """
        self.player_guess = input("Guess a letter from (A-Z): ")

    def do_updates(self):
        """
        Updates the game for each turn, updating the parachute and the word.
        """
        correct_guess = self.puzzle.process_guess(self.player_guess)
        if correct_guess == False:
            self.parachute.cut_parachute_piece()

        if self.puzzle.keep_playing():
            if self.parachute.has_parachute() == False:
                self.keep_playing == False
                self.parachute.parachute_gone()
                self.parachute.draw_parachute()
        else:
            self.keep_playing == False
            


        


        
        