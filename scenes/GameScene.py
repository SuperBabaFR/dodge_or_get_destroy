import pygame

from config import CONFIG
from scenes.Scene import Scene
from entities.GameObjects import Ball

class GameScene(Scene):

    def __init__(self):
        self.images = {}
        self.entities = []

    def init_images(self):
        self.images["ball"] = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/ball.png").convert_alpha()

    def init_entities(self):
        self.entities.append(Ball(500, 500, self.images["ball"]))
        pass

    def update(self, dt):
        for entity in self.entities:
            entity.update(dt)

    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen)


