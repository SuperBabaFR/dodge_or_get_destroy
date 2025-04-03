import pygame

from config import CONFIG
from hud.UIElements import TextUI
from scenes.Scene import Scene

class GameOverScene(Scene):
    def __init__(self):
        super().__init__()
        self.uiElements = []
        self.score = 0

    def start(self, data={}):
        print("donnees", data)
        self.score = data.get("score")  # récupère le score
        self.init_ui()

    def init_ui(self):
        self.uiElements = []
        text = TextUI(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 5, "Game Over", 60, True)
        self.uiElements.append(text)
        text = TextUI(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 4, "Score : "+str(int(self.score)), 60, True)
        self.uiElements.append(text)

        text = TextUI(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 3, "ESPACE pour rejouer", 60, True)
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