import pygame as pg
from colors import *
from settings import *

class Game:
    def __init__(self):
        self.FPS = 60
        pg.init()
        self.display = pg.display.set_mode((display_width, display_height))

        self.display.fill(WHITE)

    def run(self):
        rele = True
        while rele:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    rele = False
            pg.time.delay(1000 // self.FPS)
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
