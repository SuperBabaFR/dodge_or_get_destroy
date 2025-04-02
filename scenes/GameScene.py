import pygame

from config import CONFIG
from entities.EntityManager import EntityManager
from entities.GameObjects import Player
from scenes.Scene import Scene

class GameScene(Scene):

    def __init__(self):
        self.entityManager = EntityManager()


    def init_images(self):
        self.entityManager.init()
        self.entityManager.images

    def init_entities(self):
        self.player = Player(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 2, )

    def update(self, dt):

        self.entityManager.AutoSpawn(dt)

        for entity in self.entityManager.entities:
            entity.update(dt)

    def draw(self, screen):
        for entity in self.entityManager.entities:
            entity.draw(screen)


