import pygame

from config import CONFIG
from entities.EntityManager import EntityManager
from entities.Player import Player
from hud.UIElements import TextUI
from scenes.Scene import Scene
from util.SoundManager import SoundManager


class GameScene(Scene):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.player_img = None
        self.player = None
        self.entityManager = EntityManager()
        self.uiElements = []
        sfx = {"explosion": "explosion.mp3", "game_start": "game-start.mp3", "game_over": "game-over.mp3", "bonus": "bonus.mp3"}
        self.sound_manager = SoundManager(sfx, "")

    def init_images(self):
        self.entityManager.init()
        self.player_img = pygame.image.load(CONFIG.IMAGE_FOLDER + "/entity/personnage/alien.png").convert_alpha()

    def init_entities(self):
        self.init_ui()
        self.sound_manager.init()

    def init_ui(self):
        self.scoreUI = TextUI(0, 0, "Score : 0", 60)
        self.HPUI = TextUI(0, 40, "HP : 3", 60)
        self.uiElements.append(self.scoreUI)
        self.uiElements.append(self.HPUI)

    def start(self, data={}):
        self.player = Player(CONFIG.WIDTH / 2, CONFIG.HEIGHT / 2, self.player_img)
        self.score = 0
        self.entityManager.clear_entity()
        self.sound_manager.play_sfx("game_start")

    def update(self, dt):

        self.entityManager.AutoSpawn(dt)

        for entity in self.entityManager.entities:
            if self.player.collide(entity):
                if entity.name == "bonus":
                    self.sound_manager.play_sfx("bonus")
                elif entity.name == "ball":
                    self.sound_manager.play_sfx("explosion")

                self.entityManager.entities.remove(entity)
            else:
                entity.update(dt)

        self.player.update(dt)

        self.score += dt

        self.scoreUI.update_text("Score : " + str(int(self.score)))
        self.HPUI.update_text("HP : " + str(int(self.player.life)))

        if not self.player.is_alive():
            self.next_scene = "gameover"
            self.sound_manager.play_sfx("game_over")


    def get_data(self):
        return {"score": self.score}

    def draw(self, screen):
        # BACKGROUND COLOR
        # screen.fill((100, 100, 100))

        for entity in self.entityManager.entities:
            entity.draw(screen)

        self.player.draw(screen)

        for uiElement in self.uiElements:
            uiElement.draw(screen)
