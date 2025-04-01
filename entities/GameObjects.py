import pygame
from pygame import math

import random
from config import CONFIG
from entities.GameEntity import GameEntity

BALL_RADIUS = 64

class Ball(GameEntity):
    def __init__(self, x, y, image):

        self.image = pygame.transform.scale(image, (BALL_RADIUS, BALL_RADIUS))

        super().__init__(x, y, self.image)

        random_direction = random.random()

        self.direction = {"x": random.choice([-random_direction, random_direction]), "y": random.choice([-random_direction, random_direction])}
        self.speed = random.randint(300,900)

    def update(self, dt):
        self.x += self.direction["x"] * self.speed * dt
        self.y += self.direction["y"] * self.speed * dt

        limit_edge_w = self.x < 0 or self.x + BALL_RADIUS > CONFIG.WIDTH
        limit_edge_h = self.y < 0 or self.y + BALL_RADIUS > CONFIG.HEIGHT

        self.direction["x"] = (- self.direction["x"]) if limit_edge_w else self.direction["x"]
        self.direction["y"] = (- self.direction["y"]) if limit_edge_h else self.direction["y"]

        math.clamp(self.x, 0, CONFIG.WIDTH - BALL_RADIUS)
        math.clamp(self.y, 0, CONFIG.HEIGHT - BALL_RADIUS)
