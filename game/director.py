from game.puzzle import Puzzle
from game.parachute import Parachute

class Director:
    def __init__(self):
        self.puzzle = Puzzle()
        self.keep_playing = True
        self.parachute = Parachute()

    def start_game(self):
        while self.keep_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def do_outputs(self):
        self.puzzle.draw_word()
        self.parachute.draw_parachute()
        
    def get_inputs(self):
        self.player_guess = input("Guess a letter from (A-Z): ")

    def do_updates(self):
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
            


        


        
        