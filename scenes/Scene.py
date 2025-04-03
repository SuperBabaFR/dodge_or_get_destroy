class Scene:
    def __init__(self):
        self.next_scene = None

    def init(self):
        self.init_images()
        self.init_entities()

    def init_images(self):
        pass

    def init_entities(self):
        pass

    def start(self, data={}):
        pass

    def get_data(self):
        return {}

    def update(self, dt):
        pass

    def draw(self, screen):
        pass
