








































































































































































































































































































































































import pygame
from settings import *


class Player(pygame.sprite.Sprite):  # the class that the super func will use
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(
            groups
        )  # makes it inherit the Sprite class with groups as a parameter (not sure why)
        self.image = pygame.image.load(
            "/home/runner/Grenshin/graphics/player.png"
        ).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = (
            pygame.math.Vector2()
        )  # something that holds the x and/or y position by a parameter
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
        # the func inflate takes x and y as a parameter and takes away half of each parameter from the left right and top bottom of each rect
        self.hitbox = self.rect.inflate(0, -26)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        # to ensure we are travelling at the same speed
        if self.direction.magnitude() != 0:  # a magnitude of 0 can't be normalised
            self.direction = (
                self.direction.normalize()
            )  # returns the same vector but with a magnitude of 1

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == "horizontal":  # horizontal collisions
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        # moves the right side of the player to the left side of the obstacle
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":  # vertical collisions
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down (cause 0,0 stars top left)
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)
