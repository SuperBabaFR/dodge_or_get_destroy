import pygame

from config import CONFIG
from effects.StarryBackground import StarryBackground
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
        self.uiElements = []

        phrases = {
            0 : "Dodge or Get Destroy",
            160 : "ESPACE pour rejouer",
            240 : "ECHAP pour quitter"
        }

        start_y = CONFIG.HEIGHT / 3

        for line_spacing, phrase in phrases.items():
            x = CONFIG.WIDTH / 2
            y = start_y + line_spacing
            text = TextUI(x,y, phrase, 60, True)
            self.uiElements.append(text)


    def update(self, dt):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.next_scene = "gameplay"


    def draw(self, screen):


        for uiElement in self.uiElements:
            uiElement.draw(screen)