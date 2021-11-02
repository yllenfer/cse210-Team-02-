from time import sleep
from game import constants
from game.score import Score
from game.word import Word
from game.buffer import Buffer
from game.constants import ASTERISK


class Director:
    """A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score..
    """

    def __init__(self, input_service, output_service):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._words = []
        for i in range(5):
            self._words.append(Word())
        self._buffer = Buffer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play.

        Args:
            self (Director): An instance of Director.
        """
        character = self._input_service.get_letter()
        if character == ASTERISK:
            self._buffer.clear_buffer()
        else:
            self._buffer.add_letter(character)

    def _do_updates(self):
        """Updates the important game information for each round of play.

        Args:
            self (Director): An instance of Director.
        """
        self.check_buffer()
        for word in self._words:
            word.move_next()

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means checking if there are stones left and declaring
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self._words)
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()

    def check_buffer(self):
        """Checks if there word in the buffer is the same that's being displayed in order to add points according to
        the length of the word and takes away the word that's been typed in correctly

              Args:
                  self (Director): An instance of Director.
              """
        buffer = self._buffer.get_buffer()
        for word in self._words:
            if word.get_word() in buffer:
                self._score.add_points(len(word.get_word()))
                word.reset_word()
