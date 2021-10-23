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
        selects a word from the list self.words by using the random module.

        """
        self.word =  random.choice(self.words)


    def draw_word(self):
        """
        Will draw a word by using a for loop to print out each of the characters of the chosen word.
        """
        for letter in self.word_guess:
             self.console.write_single_line(letter)        
        self.console.write("")

    def process_guess(self, guess_letter):
        """
        Will determine if the players letter guess is in the word by iterating through the list of characters and seeing if the letter mathes any of the characters in the list.

        Parameter: 'guess_letter'(string):  the letter the user passes into the function
        """
        correct_guess = False
        
        for index, char in enumerate(self.word):
            if char == guess_letter:
                self.word_guess[index] = guess_letter
                correct_guess = True

        return correct_guess

    def keep_playing(self):
        """
        determine whether the game should continue or not

        return: word guessed
        """
        return ("_" in self.word_guess)
