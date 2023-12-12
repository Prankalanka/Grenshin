import pygame
from settings import *


class Tile(pygame.sprite.Sprite):  # the class that the super func will use
    def __init__(self, pos, groups):
        super().__init__(
            groups
        )  # Makes it inherit the Sprite class with groups as a parameter (not sure why)
        # Notes: pygame.image.load() loads an image and makes it its own surface, convert alpha optimises the surface for blitting
        self.image = pygame.image.load(
            "/home/runner/Grenshin/graphics/grass_flowers.png"
        ).convert_alpha()  # convert alpha optimises the surface for blitting
        self.rect = self.image.get_rect(
            topleft=pos
        )  # makes a rectangle from the images size with the position at the topleft
        self.hitbox = self.rect.inflate(0, -10)
