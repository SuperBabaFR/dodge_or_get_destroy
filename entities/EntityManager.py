from random import randint

import pygame

from config import CONFIG
from entities.GameObjects import Ball, BALL_RADIUS


class EntityManager:
    def __init__(self):
        self.entities = []
        self.images = {}
        self.time = 0
        self.ball_spawn_cooldown = 2

    def init(self):
        self.images["ball"] = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/ball.png").convert_alpha()
        self.SpawnBall()

    def SpawnBall(self):
        x = randint(0, CONFIG.WIDTH - BALL_RADIUS)
        y = randint(0, CONFIG.HEIGHT - BALL_RADIUS)
        self.entities.append(Ball(x, y, self.images["ball"]))

    def AutoSpawn(self, dt):
        self.time += dt

        if self.time > self.ball_spawn_cooldown:
            self.SpawnBall()
            self.time -= self.ball_spawn_cooldown