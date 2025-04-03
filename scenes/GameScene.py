import pygame
from pygame import Color
from pygame.color import THECOLORS

from config import CONFIG
from entities.EntityManager import EntityManager
from entities.Player import Player
from hud.UIElements import TextUI
from scenes.Scene import Scene


class GameScene(Scene):

    def __init__(self):
        self.score = 0
        self.player_img = None
        self.player = None
        self.entityManager = EntityManager()
        self.uiElements = []

    def init_images(self):
        self.entityManager.init()
        self.player_img = pygame.image.load(CONFIG.IMAGE_FOLDER + "/entity/personnage/player.png").convert_alpha()

    def init_entities(self):
        self.start()
        self.init_ui()

    def init_ui(self):
        self.scoreUI = TextUI(0, 0, "Score : 0", 60)
        self.uiElements.append(self.scoreUI)

    def start(self):
        self.player = Player(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 2, self.player_img)
        self.score = 0

    def update(self, dt):

        self.entityManager.AutoSpawn(dt)

        for entity in self.entityManager.entities:
            if self.player.collide(entity):
                self.entityManager.entities.remove(entity)
            else:
                entity.update(dt)

        self.player.update(dt)

        self.score += dt

        self.scoreUI.update_text("Score : " + str(int(self.score)))

    def draw(self, screen):
        # BACKGROUND COLOR
        screen.fill((100, 100, 100))

        for entity in self.entityManager.entities:
            entity.draw(screen)

        self.player.draw(screen)

        for uiElement in self.uiElements:
            uiElement.draw(screen)
