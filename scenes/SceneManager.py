
from scenes.GameScene import GameScene


class SceneManager:
    def __init__(self):
        self.scenes = { "gameplay" : GameScene() }
        self.current_scene = self.scenes["gameplay"]
        pass

    def init(self):
        for scene in self.scenes.values():
            scene.init()

    def update(self, dt):
        self.current_scene.update(dt)

    def draw(self, screen):
        self.current_scene.draw(screen)