import random

import pygame

from config import CONFIG


class Star:
    def __init__(self, x, y, rayon, anim_time_sec):
        self.x = x
        self.y = y
        self.start_rayon = rayon
        self.rayon = rayon
        self.anim_time_sec = anim_time_sec
        self.center = (self.x - self.rayon, self.y - self.rayon)
        self.direction = -1

    def respawn(self):
        self.direction = 1
        self.x = random.randint(0, CONFIG.WIDTH)
        self.y = random.randint(0, CONFIG.HEIGHT)
        self.start_rayon = random.random() * 5
        self.anim_time_sec = random.randint(1, 3)

    def update(self, dt):
        self.rayon += (self.start_rayon * dt / self.anim_time_sec) * self.direction

        if self.rayon <= 0:
            self.respawn()

        if self.rayon >= self.start_rayon:
            self.rayon = self.start_rayon
            self.direction = -self.direction

    def draw(self, screen):
        self.center = (self.x, self.y)
        pygame.draw.circle(screen, (255, 255, 255), self.center, self.rayon, 0)


class StarryBackground:

    def __init__(self, star_count):
        self.star_count = star_count
        self.stars = []

    def init_stars(self):
        for i in range(self.star_count):
            x = random.randint(0, CONFIG.WIDTH)
            y = random.randint(0, CONFIG.HEIGHT)
            rayon = random.random() * 5
            anim_time_sec = random.randint(1,3)
            self.stars.append(Star(x, y, rayon, anim_time_sec))

    def update(self, dt):
        for star in self.stars:
            star.update(dt)

    def draw(self, screen):
        screen.fill((0, 0, 0))

        for star in self.stars:
            star.draw(screen)