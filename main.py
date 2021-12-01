import sys
import pygame
import random
from pygame.math import Vector2

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),
                                 int(self.pos.y * cell_size), cell_size, cell_size)

        pygame.draw.rect(screen, pygame.color.Color("red"), fruit_rect)


fruit = FRUIT()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pygame.Color('green'))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
