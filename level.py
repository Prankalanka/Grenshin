# Tile Map is going to be a list of lists (2D Array) so that we can give an x and y value to each tile
import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):
        # get the display surface so we can draw onto it
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        """
        .We are working with a 2d array which is essentially a graph where each element can
        be accessed by their row and colum number (y and x value).
        .However, how it actually works is more like one graph for each nested list, the nested list being
        the row with a colum for each element
        .So this is basically how it works: we start off by enumerating the headlist giving a number
        starting from 0 to each nested lists. (y value)
        .Then we access the each tile (equivalent to a box in a graph) by enumerating each nested list
        giving a number for that too. (x value)
        .Now we have two numbers to access each tile with an x and y let's have an example with
        (0, 2) as our values this would be in the first nested list with the second element
        .We multiply this by the tilesize to get the actual position on the screen we want it to be
        .Then we make an instance of the Tile class using those values for its position on the screen
        .Its group(s) will depend on what letter it is represented with in the world map
        .AND THATS ALL TA-DA!!!

        """
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == "p":
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites
                    )

    def run(self):
        # Draws every sprite within the visible group onto the display surface (window)
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):  # the class super func uses
    def __init__(self):

        super().__init__()  # Makes it inherit the Group class
        self.display_surface = pygame.display.get_surface()
# finds the middle of the screen by getting half of the x and y size of the window
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(1, 1)

    def custom_draw(self, player):
# the sprite will be at an offset to the player creating a camera effect with the player at the center
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
