import pygame as pg
from colors import *
from settings import *
from ball import Ball
from trajectory import Trajectory
from arrow import Arrow
from target import Target
from random import randint

class Game:
    def __init__(self):
        pg.init()
        self.FPS = 60
        self.display = pg.display.set_mode((display_width, display_height))
        self.display.fill(WHITE)

    def run(self):
        ball = Ball(self.display)
        ind = 0

        trajectory = Trajectory(self.display)

        targ = Target(self.display)

        rele = True
        rele_start = False
        while rele:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    rele = False
                elif event.type == pg.MOUSEBUTTONUP and not rele_start:
                    v0, alf = arr.return_params()
                    ball.v0 = v0
                    ball.alf = alf
                    map = ball.fly_map()
                    rele_start = True
                elif event.type == pg.MOUSEBUTTONDOWN and not rele_start:
                    pos = pg.mouse.get_pos()
                    arr = Arrow(self.display, pos)

            pg.time.delay(1000 // self.FPS)
            self.display.fill(WHITE)
            pg.draw.rect(self.display,
                         GRAY,
                         (0, y0, display_width, display_height))
            targ.draw()

            if not rele_start:
                pressed = pg.mouse.get_pressed()
                pos = pg.mouse.get_pos()
                ball.draw_start_pos_ball()

                n = randint(1, 100)
                if n == 1:
                    targ.recalculation()

                if pressed[0]:
                    if pos[0] > x0 and pos[1] < y0 - radius:
                        arr.change_params(pos)
                    arr.draw_arrow()

            if rele_start:
                if ind != len(map) - 1:
                    coord = map[ind]
                    trajectory.draw_traject()
                    ball.draw_ball(coord)
                    trajectory.traject_list.append(coord)
                    ind += 1
                else:
                    ind = 0
                    ball.y = ball.y0
                    ball.x = ball.x0
                    trajectory.traject_list.clear()
                    rele_start = False
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
