from dataclasses import dataclass

import pygame

from config import CONFIG
from entities.GameEntity import GameEntity
from entities.GameObjects import Bonus, BONUS_TYPE
from util.TimeObjects import CountdownTimer
from util.collisions import collide_circle_rect
from pygame import math as m

PLAYER_SIZE = (64, 64)



class Effect:
    def __init__(self, name, duration):
        self.name = name
        self.countdown = CountdownTimer(duration)
        self.countdown.start()


class Player(GameEntity):
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, PLAYER_SIZE)

        super().__init__(x - PLAYER_SIZE[0], y - PLAYER_SIZE[1], self.image, "player")

        self.default_speed = 500
        self.speed = self.default_speed
        self.direction = pygame.math.Vector2(0, 0)

        self.life_max = 3
        self.life = self.life_max

        self.invulnerability = CountdownTimer(1)
        self.invulnerable = False

        self.effects_list = []

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.update_hitbox()

        self.speed = self.default_speed

        self.life = self.life_max

        self.effects_list = []
        self.invulnerability = CountdownTimer(1)
        self.invulnerable = False

    def collide(self, other: GameEntity):
        if self.invulnerable and other.name == "ball":
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
            elif other.name == "bonus":
                bonus: Bonus = other

                if bonus.bonus_type == BONUS_TYPE.life_bonus:
                    print("Get life_bonus")
                    self.life_manager(1)
                elif bonus.bonus_type == BONUS_TYPE.speed_boost:
                    self.effects_list.append(Effect(bonus.bonus_type, bonus.duration))
                    print("Add Effect", bonus.bonus_type,)

        return collided

    def life_manager(self, value):
        print("life_manager | vie : ", self.life + value)

        if value < 0:
            self.invulnerable = True
            self.invulnerability.start()

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

        # Gestion des effets
        self.effects_update(dt)

        # Gestion de l'invincibilité
        if self.invulnerable:
            print("invulnerable timeleft : ", self.invulnerability.is_alive(dt))
            if self.invulnerability.is_alive(dt):
                self.invulnerable = False

    def effects_update(self, dt):
        for effect in self.effects_list:
            is_alive = effect.countdown.is_alive(dt)

            match effect.name:
                case BONUS_TYPE.speed_boost:
                    self.speed = self.default_speed * 2 if is_alive else self.default_speed
                case _:
                    pass

            if not is_alive:
                print(effect.name, "is dead")
                self.effects_list.remove(effect)

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
