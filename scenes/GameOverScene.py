import json

import pygame

from config import CONFIG
from effects.StarryBackground import StarryBackground
from hud.UIElements import TextUI
from scenes.Scene import Scene

class GameOverScene(Scene):
    def __init__(self):
        super().__init__()
        self.uiElements = []
        self.score = 0
        self.best_score = 0

    def start(self, data={}):
        print("donnees", data)
        self.score = data.get("score", 0)  # récupère le score

        with open('data/data.json', 'r') as f:
            data = json.load(f)
            self.best_score = data["best_score"]
            f.close()

        if self.score > self.best_score:
            self.best_score = self.score
            with open('data/data.json', 'w') as f:
                f.write(json.dumps({'best_score':int(self.best_score)}))
                f.close()

        self.init_ui()

    def init_ui(self):
        self.uiElements = []


        phrases = {
            0 : "Game Over",
            100 : f"Score: {int(self.score)}",
            180 : f"Best score: {int(self.best_score)}",
            160+80*2 : "ESPACE pour rejouer",
            160+80*3 : "ECHAP pour quitter"
        }

        start_y = CONFIG.HEIGHT / 4

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