from pygame import Surface


class GameEntity:
    def __init__(self, x, y, image:Surface, name='entity'):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


# class StaticEntity(GameEntity):
#     pass
