# змейка

import pygame
pygame.init()

scee_size = (800, 600)
screen = pygame.display.set_mode(scee_size)
pygame.display.set_caption("Snake Game")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # событие
    screen.fill((0, 0, 0))
    pygame.display.flip()



pygame.quit()

