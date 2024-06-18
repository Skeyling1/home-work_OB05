# игра змейка

import pygame
pygame.init()

scee_size = (800, 600)
screen = pygame.display.set_mode(scee_size)
pygame.display.set_caption("Snake Game")

image = pygame.image.load("tail-1.png")
x = 50
y = 50
direction_x = 0
direction_y = 0
position = (x, y)


class Head:
    def __init__(self):
        self.position = position
    def moving(self):
        screen.blit(image, position)

class Tail:
    pass

class Eatables:
    pass

snail = Head()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    snail.moving()
    pygame.time.delay(10)


    keys = pygame.key.get_pressed()

    x += direction_x
    y += direction_y
    if keys[pygame.K_RIGHT]:
        direction_x = 1
    elif keys[pygame.K_LEFT]:
        direction_x = -1
    elif keys[pygame.K_UP]:
        direction_y = -1
    elif keys[pygame.K_DOWN]:
        direction_y = 1

    position = (x, y)





    pygame.display.flip()



pygame.quit()

