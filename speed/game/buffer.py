import random
from game.constants import MAX_Y
from asciimatics.event import KeyboardEvent
from game.actor import Actor
from game.point import Point


class Buffer(Actor):
    """Process and displays words as they typed in the keyboard and displays them.

     Stereotype:
         Information Displayed

     Attributes:
         _buffer (string): The characters typed in
     """

    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes string to empty and updates dashes
        with typed in character.

                Args:
                    self (Buffer): an instance of Buffer.
                """
        self._buffer = ""
        self.set_position(Point(1, MAX_Y))
        self.set_text(f"Buffer: {self._buffer}")

    def add_letter(self, character):
        """Adds character typed to make it a sentence and displays it the buffer keyboard event.

                Args:
                    self (Buffer): An instance of Buffer.
                    character (string): The letter to add.
                """
        self._buffer += character
        self.set_text(f"Buffer: {self._buffer}")

    def clear_buffer(self):
        """Clears character from buffer keyboard event.

                        Args:
                            self (Buffer): An instance of Buffer.

                        """

        self._buffer = ""

    def get_buffer(self):
        """Gets the buffer and displays it

                               Args:
                                   self (Buffer): An instance of Buffer.

                               """
        return self._buffer
