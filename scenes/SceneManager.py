from scenes.GameOverScene import GameOverScene
from scenes.GameScene import GameScene
from scenes.SceneMenu import MenuScene


class SceneManager:
    def __init__(self):
        self.scenes = {"menu_principal": MenuScene(), "gameplay": GameScene(), "gameover": GameOverScene()}
        self.current_scene = self.scenes["menu_principal"]

    def init(self):
        for scene in self.scenes.values():
            scene.init()

    def update(self, dt):
        self.current_scene.update(dt)

        if self.current_scene.next_scene:
            new_scene = self.scenes[self.current_scene.next_scene]
            self.current_scene.next_scene = None
            print("donnees", self.current_scene.get_data())
            new_scene.start(self.current_scene.get_data())
            self.current_scene = new_scene

    def draw(self, screen):
        self.current_scene.draw(screen)
