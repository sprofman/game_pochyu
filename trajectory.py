from pygame import draw
from settings import *
from colors import *


class Trajectory:
    def __init__(self, display):
        self.radius = 1
        self.traject_list = []
        self.display = display

    def draw_traject(self):
        for coord in self.traject_list:
            x = coord[0]
            y = coord[1]
            draw.circle(surface=self.display,
                        color=BLACK,
                        center=(x, y),
                        radius=self.radius)
