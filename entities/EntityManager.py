from random import randint, choice

import pygame

from config import CONFIG
from entities.GameObjects import Asteroid, BALL_RADIUS, BONUS_SIZE, Bonus, BONUS_TYPE
from util.TimeObjects import TimeCycleTrigger


class EntityManager:
    def __init__(self):
        self.entities = []
        self.images = {}
        self.ball_spawn_cycle = TimeCycleTrigger(2)
        self.bonus_spawn_cycle = TimeCycleTrigger(4)

    def init(self):
        for i in range(1,3):
            self.images["asteroid_"+str(i)] = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/asteroids/asteroid_" + str(i) + ".png").convert_alpha()
        self.images[BONUS_TYPE.life_bonus] = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/bonus/life_bonus.png").convert_alpha()
        self.images[BONUS_TYPE.speed_boost] = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/bonus/speed_boost.png").convert_alpha()

    def spawn_ball(self):
        x = randint(0, CONFIG.WIDTH - BALL_RADIUS)
        y = randint(0, CONFIG.HEIGHT - BALL_RADIUS)
        img_name = "asteroid_" + str(randint(1,2))
        self.entities.append(Asteroid(x, y, self.images[img_name]))


    def clear_entity(self):
        self.entities = []

    def spawn_bonus(self):
        x = randint(0, CONFIG.WIDTH - BONUS_SIZE[0])
        y = randint(0, CONFIG.WIDTH - BONUS_SIZE[1])

        bonus_choice = choice([BONUS_TYPE.life_bonus, BONUS_TYPE.speed_boost])

        self.entities.append(Bonus(x, y, self.images[bonus_choice], bonus_choice))

    def AutoSpawn(self, dt):

        if self.ball_spawn_cycle.trigger(dt):
            self.spawn_ball()

        if self.bonus_spawn_cycle.trigger(dt):
            self.spawn_bonus()
