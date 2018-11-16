import pyglet
from lib.component import Component
import config


class Ball(Component):

    def __init__(self, *args, **kwargs):
        """
        Creates a sprite using a ball image.
        """
        super(Ball, self).__init__(*args, **kwargs)
        self.speed = kwargs.get('speed', 5)
        self.ball_image = pyglet.image.load('assets/kitten.png')
        self.width = self.ball_image.width
        self.height = self.ball_image.height
        self.ball_sprite = pyglet.sprite.Sprite(self.ball_image, self.x, self.y)
        self.x_direction = 1
        self.y_direction = 1

        print('Ball Created')

    def update_self(self):
        """
        Increments x and y value and updates position.
        Also ensures that the ball does not leave the screen area by changing its axis direction
        :return:
        """
        self.x += (self.speed * self.x_direction)
        self.y += (self.speed * self.y_direction)
        self.ball_sprite.set_position(self.x, self.y)

        if self.x < 0 or (self.x + self.width) > config.window_width:
            self.x_direction *= -1

        if self.y < 0 or (self.y + self.height) > config.window_height:
            self.y_direction *= -1

    def draw_self(self):
        """
        Draws our ball sprite to screen
        :return:
        """
        self.ball_sprite.draw()
