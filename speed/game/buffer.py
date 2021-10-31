import random
from game.constants import MAX_Y
from asciimatics.event import KeyboardEvent
from game.actor import Actor
from game.point import Point


class Buffer(Actor):

    def __init__(self):
        self._buffer = ""
        self.set_position(Point(1, MAX_Y))
        self.set_text(f"Buffer: {self._buffer}")

    def add_letter(self, character):
        self._buffer += character
        self.set_text(f"Buffer: {self._buffer}")

    def clear_buffer(self):
        self._buffer = ""

    def get_buffer(self):
        return self._buffer
