from os import X_OK
from game.actor import Actor
from game.constants import LIBRARY, MAX_Y
import random
from game.point import Point


class Word(Actor):
    """Word class is responsible for getting and generating random words to display them in random orders and random
    positions in the console

     Stereotype:
         Information Holder

     Attributes:
         _word (string): The words being generated.
     """

    def __init__(self):
        super().__init__()
        self._word = ""
        self.reset_word()

        """The class constructor.

                   Args:
                       self (Word): An instance of Actor.
                   """

    def _word_generator(self):
        """Generates random words from txt file

                Args:
                    self (Word): an instance of Actor.

                Returns:
                    Word: The actor's word position in 2d space.
                """
        return random.choice(LIBRARY)

    def get_word(self):
        """Get the random word.

               Args:
                   self (Word): An instance of Actor.
               """
        return self._word

    def reset_word(self):
        """Gives the randomly generated word a speed and a random position so they don't overlap. Once this is the
        done gets the word to be ready to be displayed in the console

               Args:
                   self (Word): An instance of Actor.
               """
        self._word = self._word_generator()
        self.set_velocity(Point(1, 0))
        self.set_position(Point(1, random.randint(1, MAX_Y - 2)))
        self.set_text(self._word)
