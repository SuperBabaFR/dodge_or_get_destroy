from random import randint, choice

import pygame

from config import CONFIG
from entities.GameObjects import Ball, BALL_RADIUS, BONUS_SIZE, Bonus


class EntityManager:
    def __init__(self):
        self.entities = []
        self.images = {}
        self.time = 0
        self.ball_spawn_cooldown = 2
        self.bonus_spawn_cooldown = 4

    def init(self):
        self.images["ball"] = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/ball.png").convert_alpha()
        self.images["life_bonus"] = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/bonus/life_bonus.png").convert_alpha()
        self.images["speed_boost"] = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/bonus/speed_boost.png").convert_alpha()
        self.spawn_ball()

    def spawn_ball(self):
        x = randint(0, CONFIG.WIDTH - BALL_RADIUS)
        y = randint(0, CONFIG.HEIGHT - BALL_RADIUS)
        self.entities.append(Ball(x, y, self.images["ball"]))

    def spawn_bonus(self):
        x = randint(0, CONFIG.WIDTH - BONUS_SIZE)
        y = randint(0, CONFIG.WIDTH - BONUS_SIZE)

        bonus_choice = choice(["life_bonus", "speed_boost"])

        self.entities.append(Bonus(x, y, self.images["life_bonus"], bonus_choice))

    def AutoSpawn(self, dt):
        self.time += dt

        if self.time % self.ball_spawn_cooldown:
            self.spawn_ball()
        elif self.time % self.bonus_spawn_cooldown:
            self.spawn_bonus()
