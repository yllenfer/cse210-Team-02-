from os import X_OK
from game.actor import Actor
from game.constants import LIBRARY, MAX_Y
import random
from game.point import Point


class Word(Actor):

    def __init__(self):
        super().__init__()
        self._word = ""
        self.reset_word()

    def _word_generator(self):
        return random.choice(LIBRARY)

    def get_word(self):
        return self._word

    def reset_word(self):
        self._word = self._word_generator()
        self.set_velocity(Point(1, 0))
        self.set_position(Point(1, random.randint(1, MAX_Y - 2)))
        self.set_text(self._word)
