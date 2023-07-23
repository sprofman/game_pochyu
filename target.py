import pygame as pg
from random import randint
from colors import *
from settings import *


class Target:
    def __init__(self, display):
        self.width = 50
        self.height = 50
        self.x1 = randint(display_width / 2, display_width - self.width)
        self.y1 = display_height - self.height - s
        self.x2 = self.x1 + display_width
        self.y2 = self.y1 + display_height
        self.color = LIGHT_BLUE
        self.display = display


    def draw(self):
        n = randint(1, 100)
        if n == 1:
            self.x1 = randint(display_width / 2, display_width - self.width)
            self.y1 = display_height - self.height - s
            self.x2 = self.x1 + display_width
            self.y2 = self.y1 + display_height
        pg.draw.rect(self.display, self.color, (self.x1, self.y1, self.width, self.height))
        pg.display.update()