import pygame

from config import CONFIG
from entities.EntityManager import EntityManager
from entities.Player import Player
from scenes.Scene import Scene


class GameScene(Scene):

    def __init__(self):
        self.player_img = None
        self.player = None
        self.entityManager = EntityManager()

    def init_images(self):
        self.entityManager.init()
        self.player_img = pygame.image.load(CONFIG.IMAGE_FOLDER + "/entity/personnage/player.png").convert_alpha()

    def init_entities(self):
        self.player = Player(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 2, self.player_img)

    def update(self, dt):

        self.entityManager.AutoSpawn(dt)

        for entity in self.entityManager.entities:
            if self.player.collide(entity):
                self.entityManager.entities.remove(entity)
            else:
                entity.update(dt)

        self.player.update(dt)

    def draw(self, screen):
        # BACKGROUND COLOR
        screen.fill((100, 100, 100))

        for entity in self.entityManager.entities:
            entity.draw(screen)

        self.player.draw(screen)
