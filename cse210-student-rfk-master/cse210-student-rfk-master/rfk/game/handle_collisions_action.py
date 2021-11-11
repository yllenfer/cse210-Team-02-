from os import X_OK
from game import constants
import random
from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point
import sys


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._cast = cast
        self.ball_brick_collision(cast)
        self.ball_paddle_collision(cast)
        self.ball_wall_collision(cast)
        self.ball_ceiling_collision(cast)
        self.ball_floor_collision(cast)

    def ball_brick_collision(self, cast):
        """Defines what happens when the ball touches the bricks

        Args:
            cast (dict): The game actors {key: tag, value: list}.

        """
        ball = cast["ball"][0]  # there's only one
        bricks = cast["brick"]
        velocity = ball.get_velocity()
        ball_x_velocity = velocity.get_x()
        ball_y_velocity = velocity.get_y()
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                cast["brick"].remove(brick)  # delete current brick
                ball.set_velocity(Point(ball_x_velocity, (ball_y_velocity * -1)))

    def ball_paddle_collision(self, cast):
        """Defines what happens when the ball touches the paddle.

        Args:
            cast (dict): The game actors {key: tag, value: list}.

        """
        ball = cast["ball"][0]
        paddle = cast["paddle"][0]
        velocity = ball.get_velocity()

        paddle_x_position = paddle.get_position().get_x()
        paddle_y_position = paddle.get_position().get_y()
        ball_x_position = ball.get_position().get_x()
        ball_y_position = ball.get_position().get_y()

        if (ball_y_position == paddle_y_position and
                paddle_x_position <= ball_x_position <= paddle_x_position + len(paddle.get_text())):
            ball_x_velocity = velocity.get_x()
            ball_y_velocity = velocity.get_y()
            ball.set_velocity(Point(ball_x_velocity, (ball_y_velocity * -1)))

    def ball_wall_collision(self, cast):
        """Defines what happens when the ball touches the bricks
​
        Args:
            cast (dict): The game actors {key: tag, value: list}.

        """
        ball = cast["ball"][0]
        velocity = ball.get_velocity()
        position = ball.get_position()
        ball_x_velocity = velocity.get_x()
        ball_y_velocity = velocity.get_y()
        x2 = position.get_x()
        if x2 == 79 or x2 == 1:
            ball.set_velocity(Point((ball_x_velocity * -1), ball_y_velocity))

    def ball_ceiling_collision(self, cast):
        """Defines what happens when the ball touches the ceiling.
​
        Args:
            cast (dict): The game actors {key: tag, value: list}.

        """

        ball = cast["ball"][0]
        velocity = ball.get_velocity()
        position = ball.get_position()
        ball_x_velocity = velocity.get_x()
        ball_y_velocity = velocity.get_y()
        y2 = position.get_y()
        if y2 == 1:
            ball.set_velocity(Point(ball_x_velocity, (ball_y_velocity * -1)))

    def ball_floor_collision(self, cast):
        """Ends the game when the ball touches the floor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.

        """
        ball = cast["ball"][0]
        position = ball.get_position()
        y2 = position.get_y()
        if y2 == 19:
            sys.exit()