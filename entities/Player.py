import pygame

from config import CONFIG
from entities.GameEntity import GameEntity
from util.collisions import collide_circle_rect
from pygame import math as m

PLAYER_SIZE = (64,64)

class Player(GameEntity):
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, PLAYER_SIZE)

        super().__init__(x - PLAYER_SIZE[0], y - PLAYER_SIZE[1], self.image, "player")

        self.default_speed = 500
        self.speed = self.default_speed
        self.direction = pygame.math.Vector2(0,0)

        self.life_max = 3
        self.life = self.life_max

        self.invulnerability_time = 0
        self.invulnerable = False

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.update_hitbox()

        self.speed = self.default_speed

        self.life = self.life_max
        self.invulnerability_time = 0
        self.invulnerable = False

    def collide(self, other: GameEntity):
        if self.invulnerable:
            return False

        collided = False

        if other.collision_type == "rect":
            if self.hitbox.colliderect(other.hitbox):
                collided = True
        elif other.collision_type == "circle":
            if collide_circle_rect(other.hitbox, self.hitbox):
                collided = True

        if collided:
            if other.name == "ball":
                self.life_manager(-1)
            elif other.name == "life_bonus":
                self.life_manager(1)

        return collided


    def life_manager(self, value):
        print("life_manager | vie : ", self.life + value)

        if value < 0:
            self.invulnerable = True
            self.invulnerability_time = 1

        self.life += value

    def is_alive(self):
        return self.life > 0

    def update(self, dt):
        # Mouvements au clavier
        self.inputs()
        # Application du mouvement
        self.x += self.direction.x * self.speed * dt
        self.y += self.direction.y * self.speed * dt

        # Limitations à la fenetre
        limit_edge_w = self.x < 0 or self.x + self.width >= CONFIG.WIDTH
        limit_edge_h = self.y < 0 or self.y + self.height >= CONFIG.HEIGHT

        if limit_edge_h:
            self.y = m.clamp(self.y, 0, CONFIG.HEIGHT - self.height)

        if limit_edge_w:
            self.x = m.clamp(self.x, 0, CONFIG.WIDTH - self.width)

        self.update_hitbox()

        # Gestion de l'invincibilité
        if self.invulnerable:
            self.invulnerability_time -= dt

            if self.invulnerability_time <= 0:
                self.invulnerable = False


    def inputs(self):
        self.direction.x = 0
        self.direction.y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()