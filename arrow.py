import pygame as pg
import math
from settings import *
from colors import *


class Arrow:
    def __init__(self, display, mouse_pos):
        self.x_m_p = mouse_pos[0]
        self.y_m_p = mouse_pos[1]
        self.display = display
        self.kx = self.x_m_p - x0
        self.ky = display_height - self.y_m_p - s - radius
        self.alf = math.atan(self.ky / self.kx)
        self.bet = 20 * math.pi / 180
        self.l0 = math.sqrt(self.kx ** 2 + self.ky ** 2)
        self.l = self.l0
        self.l_ar = l_min
        self.x1 = self.l_ar * math.cos(self.alf) + x0
        self.y1 = y0 - self.l_ar * math.sin(self.alf) - radius
        self.xs1 = self.x1 - ls * math.cos(self.bet - self.alf)
        self.ys1 = self.y1 - ls * math.sin(self.bet - self.alf)
        self.xs2 = self.x1 - ls * math.cos(self.bet + self.alf)
        self.ys2 = self.y1 + ls * math.sin(self.bet + self.alf)

    def draw_arrow(self):
        print((x0, y0),(self.x1, self.y1))
        pg.draw.aaline(self.display, BLACK, (x0, y0 - radius), (self.x1, self.y1))
        pg.draw.aaline(self.display, BLACK, (self.x1, self.y1),(self.xs1, self.ys1))
        pg.draw.aaline(self.display, BLACK, (self.x1, self.y1),(self.xs2, self.ys2))
        pg.display.update()