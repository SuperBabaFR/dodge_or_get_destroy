import pygame

from config import CONFIG
from scenes.SceneManager import SceneManager

pygame.init()

screen = pygame.display.set_mode((CONFIG.WIDTH, CONFIG.HEIGHT))
pygame.display.set_caption(CONFIG.TITLE)

running = True
clock = pygame.time.Clock()

scene_manager = SceneManager()

scene_manager.init()


while running:
    # Limite à X fps
    dt = clock.tick(CONFIG.FPS) / 1000.0

    # events pour fermer le jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # UPDATES
    scene_manager.update(dt)

    # CLEAN SCREEN
    screen.fill(CONFIG.CLEAN_COLOR)

    # DRAW
    scene_manager.draw(screen)

    # Actualise l'écran
    pygame.display.flip()


pygame.quit()