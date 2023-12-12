# Code that is run

# Story Ideas
# Probably not gonna be serious
# Something gave artifacts to the monsters of genshin and now they too stronk
# BUT you grinded artifacts so you can beat them :}

# Battle Ideas
# I want it like Chrono Trigger where there is no scene change between the overworld and battle
# Character positioning matters so that you can hit more enemies with one attack
# Probably elemental reaction system on top of that
# Instantly won battles if you're high level enough
# Enemies will probably have artifact set bonuses for variety/so will characters

# Art Style
# Maybe the old-school pokemon, not sure if it will work though
# Maybe kinda like the Mother series, although it's harder to pull off

# Music
# Probably has similar tunes to genshin but digitised and with the same leight motifs

# Next Steps: Make a demo with the old-school pokemon idea
import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()  # initiates pygame
        pygame.display.set_caption("Chrono Clone")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creates a window
        self.clock = pygame.time.Clock()  # sets up a clock
        self.level = Level()

    def run(self):
        while True:
            # without this the window wouldn't close when we click the x
            for event in pygame.event.get():  # for every event that occurs
                if event.type == pygame.QUIT:  # if there is a quit event
                    pygame.quit()  # stop all pygame processes
                    sys.exit()  # exit the window

            self.screen.fill((0, 0, 0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
