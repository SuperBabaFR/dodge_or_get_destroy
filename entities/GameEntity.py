class GameEntity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# class StaticEntity(GameEntity):
#     pass
