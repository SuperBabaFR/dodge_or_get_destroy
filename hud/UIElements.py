import pygame


class StaticUIElement:
    def __init__(self, x, y, element):
        self.x = x
        self.y = y
        self.element = element

    def draw(self, screen):
        screen.blit(self.element, (self.x, self.y))


class TextUI(StaticUIElement):
    def __init__(self, x, y, text, size, font=None, color=(255,255,255)):

        self.color = color
        self.font = pygame.font.Font(font, size)
        self.element = self.font.render(text, True, color)

        super().__init__(x, y, self.element)

    def update_text(self, text, color=None):
        self.element = self.font.render(text, True, color if color is not None else self.color)