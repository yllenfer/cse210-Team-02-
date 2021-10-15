import random
from game.console import Console

class Puzzle:
    
    def __init__(self):
        self.word = ""
        self.words = ["green", "ghost", "words", "about", "party"]
        self.console = Console()
        self.select_word()
        self.word_guess = [" _ "] * len(self.word)
        

    def select_word(self):
        """
        Gets a word from the list self.words

        args = self 
        """
        self.word =  random.choice(self.words)


    def draw_word(self):
        for letter in self.word_guess:
             self.console.write_single_line(letter)        
        self.console.write("")

    def process_guess(self, guess_letter):
        correct_guess = False
        
        for index, char in enumerate(self.word):
            if char == guess_letter:
                self.word_guess[index] = guess_letter
                correct_guess = True

        return correct_guess

    def keep_playing(self):
        return ("_" in self.word_guess)
