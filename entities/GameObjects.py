import pygame
from pygame import math as m
import math

import random
from config import CONFIG
from entities.GameEntity import GameEntity

BALL_RADIUS = 64
BONUS_SIZE = (64,64)


class Bouncer(GameEntity):
    def __init__(self, entity):
        super().__init__(self.x, self.y, self.image, self.name, self.collision_type)

        angle = random.uniform(0, 2 * math.pi)
        self.direction = pygame.math.Vector2(math.cos(angle), math.sin(angle))

        self.speed = random.randint(300, 900)

        self.offset = 1


    def update(self, dt):
        self.x += self.direction.x * self.speed * dt
        self.y += self.direction.y * self.speed * dt

        limit_edge_w = self.x < 0 or self.x + self.width >= CONFIG.WIDTH
        limit_edge_h = self.y < 0 or self.y + self.height >= CONFIG.HEIGHT

        if limit_edge_h:
            self.direction.y = - self.direction.y
            self.y = m.clamp(self.y, self.offset, CONFIG.HEIGHT - self.height - self.offset)

        if limit_edge_w:
            self.direction.x = - self.direction.x
            self.x = m.clamp(self.x, self.offset, CONFIG.WIDTH - self.width - self.offset)

        self.update_hitbox()



class Ball(Bouncer):
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (BALL_RADIUS, BALL_RADIUS))

        self.x = x
        self.y = y
        self.name = "ball"
        self.collision_type = "circle"

        super().__init__(self)


class Bonus(Bouncer):
    def __init__(self, x, y, image, bonus_type):
        self.image = pygame.transform.scale(image, (BONUS_SIZE[0], BONUS_SIZE[1]))

        self.x = x
        self.y = y
        self.name = "bonus"
        self.collision_type = "circle"

        super().__init__(self)

        self.bonus_type = bonus_type