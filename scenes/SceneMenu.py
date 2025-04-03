import pygame

from config import CONFIG
from hud.UIElements import TextUI
from scenes.Scene import Scene


class MenuScene(Scene):

    def __init__(self):
        super().__init__()
        self.uiElements = []

    def init_images(self):
        pass

    def init_entities(self):
        self.init_ui()

    def init_ui(self):
        text = TextUI(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 5, "Menu principal", 60, True)
        self.uiElements.append(text)

        text = TextUI(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 3, "ESPACE pour jouer", 60, True)
        self.uiElements.append(text)

        text = TextUI(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 2, "ECHAP pour quitter", 60, True)
        self.uiElements.append(text)


    def update(self, dt):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.next_scene = "gameplay"


    def draw(self, screen):
        # BACKGROUND COLOR
        screen.fill((100, 100, 100))

        for uiElement in self.uiElements:
            uiElement.draw(screen)