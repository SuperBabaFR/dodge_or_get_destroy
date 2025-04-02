import pygame
from pygame import math as m
import math

import random
from config import CONFIG
from entities.GameEntity import GameEntity

BALL_RADIUS = 64


class Ball(GameEntity):
    def __init__(self, x, y, image):

        self.image = pygame.transform.scale(image, (BALL_RADIUS, BALL_RADIUS))

        super().__init__(x, y, self.image)

        angle = random.uniform(0, 2 * math.pi)
        self.direction = {
            "x": math.cos(angle),
            "y": math.sin(angle)
        }

        self.speed = random.randint(300, 900)

        self.offset = 1

        print("my speed is", self.speed)
        print("my direction is", self.direction)

    def update(self, dt):
        self.x += self.direction["x"] * self.speed * dt
        self.y += self.direction["y"] * self.speed * dt

        limit_edge_w = self.x < 0 or self.x + BALL_RADIUS >= CONFIG.WIDTH
        limit_edge_h = self.y < 0 or self.y + BALL_RADIUS >= CONFIG.HEIGHT

        if limit_edge_h:
            self.direction["y"] = - self.direction["y"]
            self.y = m.clamp(self.y, self.offset, CONFIG.HEIGHT - BALL_RADIUS - self.offset)

        if limit_edge_w:
            self.direction["x"] = - self.direction["x"]
            self.x = m.clamp(self.x, self.offset, CONFIG.WIDTH - BALL_RADIUS - self.offset)


class Player(GameEntity):
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (BALL_RADIUS, BALL_RADIUS))
        super().__init__(x, y, self.image)

        self.speed = 500
        self.direction = {"x": 0, "y": 0}

    def set_direction(self, x, y):
        self.direction["x"] = x
        self.direction["y"] = y

    def update(self, dt):
        self.x += self.direction["x"] * self.speed * dt
        self.y += self.direction["y"] * self.speed * dt
