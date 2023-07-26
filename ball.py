from pygame import draw
from settings import *
import math
from colors import *


class Ball:
    def __init__(self, display):
        self.radius = radius
        self.max_v0 = 100
        self.v0 = 112
        self.alf = 45
        self.x0 = x0
        self.y0 = y0 - self.radius
        self.x = x0
        self.y = self.y0
        self.display = display

    def fly_map(self, x1, x2, y1, y2):
        map_list = [(self.x, self.y)]
        d = 0
        while self.y <= self.y0:
            self.x += step_x
            self.y = -(self.x - x0) * math.tan(self.alf) + g / (2 * self.v0 ** 2 * (math.cos(self.alf) ** 2)) * (
                        self.x - x0) ** 2 + self.y0
            if x1 <= self.x <= x2 and y1 <= self.y <= y2:
                d = 1
                break
            map_list.append((self.x, self.y))
        return map_list, d

    def draw_ball(self, coord):
        x = coord[0]
        y = coord[1]
        draw.circle(surface=self.display,
                    color=BLACK,
                    center=(x, y),
                    radius=self.radius)

    def draw_start_pos_ball(self):
        draw.circle(surface=self.display,
                    color=BLACK,
                    center=(self.x0, self.y0),
                    radius=self.radius)
