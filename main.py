import pygame as pg
from colors import *
from settings import *
from ball import Ball
from trajectory import Trajectory

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

        rele = True
        rele_start = False
        while rele:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    rele = False
                elif event.type == pg.MOUSEBUTTONUP and not rele_start:
                    map = ball.fly_map()
                    rele_start = True

            pg.time.delay(1000 // self.FPS)
            self.display.fill(WHITE)
            pg.draw.rect(self.display,
                         GRAY,
                         (0, y0, display_width, display_height))

            if not rele_start:
                pressed = pg.mouse.get_pressed()
                pos = pg.mouse.get_pos()
                ball.draw_start_pos_ball()

                if pressed[0]:
                    pass # события, связанные со стрелкой

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
