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
        self.player_img = pygame.image.load(CONFIG.IMAGE_FOLDER+"/entity/personnage/player.png").convert_alpha()

    def init_entities(self):
        self.player = Player(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 2, self.player_img)

    def is_key_down(self, event, key):
        return event.key == key

    def update(self, dt):

        self.entityManager.AutoSpawn(dt)

        for entity in self.entityManager.entities:
            entity.update(dt)

        self.player.update(dt)

    def draw(self, screen):
        # BACKGROUND COLOR
        screen.fill((100, 100, 100))

        for entity in self.entityManager.entities:
            entity.draw(screen)

        self.player.draw(screen)
