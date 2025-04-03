from pygame import Surface, Rect


class GameEntity:
    def __init__(self, x, y, image:Surface, name='entity', collision_type='rect'):
        self.x = x
        self.y = y
        self.image = image
        self.name = name
        self.width = image.get_width()
        self.height = image.get_height()

        self.collision_type = collision_type
        self.hitbox = self.init_hitbox()

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def init_hitbox(self):
        if self.collision_type == 'rect':
            return Rect(self.x, self.y, self.width, self.height)
        elif self.collision_type == 'circle':
            radius = self.width / 2
            return {
                "center": (self.x + radius, self.y + radius),
                "radius": radius,
            }
        return None

    def update_hitbox(self):
        if self.collision_type == 'rect':
            self.hitbox.topleft = (self.x, self.y)
        elif self.collision_type == 'circle':
            radius = self.hitbox["radius"]
            self.hitbox["center"] = (self.x + radius, self.y + radius)

# class StaticEntity(GameEntity):
#     pass
