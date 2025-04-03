import pygame
from pygame import math as m
import math

import random
from config import CONFIG
from entities.GameEntity import GameEntity

BALL_RADIUS = 64
PLAYER_SIZE = (64,64)


class Ball(GameEntity):
    def __init__(self, x, y, image):

        self.image = pygame.transform.scale(image, (BALL_RADIUS, BALL_RADIUS))

        super().__init__(x, y, self.image)

        angle = random.uniform(0, 2 * math.pi)
        self.direction = pygame.math.Vector2(math.cos(angle), math.sin(angle))

        self.speed = random.randint(300, 900)

        self.offset = 1

    def update(self, dt):
        self.x += self.direction.x * self.speed * dt
        self.y += self.direction.y * self.speed * dt

        limit_edge_w = self.x < 0 or self.x + BALL_RADIUS >= CONFIG.WIDTH
        limit_edge_h = self.y < 0 or self.y + BALL_RADIUS >= CONFIG.HEIGHT

        if limit_edge_h:
            self.direction.y = - self.direction.y
            self.y = m.clamp(self.y, self.offset, CONFIG.HEIGHT - BALL_RADIUS - self.offset)

        if limit_edge_w:
            self.direction.x = - self.direction.x
            self.x = m.clamp(self.x, self.offset, CONFIG.WIDTH - BALL_RADIUS - self.offset)


class Player(GameEntity):
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, PLAYER_SIZE)

        super().__init__(x - PLAYER_SIZE[0], y - PLAYER_SIZE[1], self.image)

        self.speed = 500
        self.direction = pygame.math.Vector2(0,0)

    def update(self, dt):
        self.inputs()

        self.x += self.direction.x * self.speed * dt
        self.y += self.direction.y * self.speed * dt

        limit_edge_w = self.x < 0 or self.x + PLAYER_SIZE[0] >= CONFIG.WIDTH
        limit_edge_h = self.y < 0 or self.y + PLAYER_SIZE[1] >= CONFIG.HEIGHT

        if limit_edge_h:
            self.y = m.clamp(self.y, 0, CONFIG.HEIGHT - PLAYER_SIZE[0])

        if limit_edge_w:
            self.x = m.clamp(self.x, 0, CONFIG.WIDTH - PLAYER_SIZE[1])

    def inputs(self):
        self.direction.x = 0
        self.direction.y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()