# игра змейка

import pygame
pygame.init()

scee_size = (800, 600)
screen = pygame.display.set_mode(scee_size)
pygame.display.set_caption("Snake Game")

image = pygame.image.load("tail-1.png")
x = 50
y = 50
position = (x, y)


class Head:
    pass

class Tail:
    pass

class Eatables:
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(image, position)
    x += 1
    y += 1
    position = (x, y)





    pygame.display.flip()



pygame.quit()

