import pygame
import random
from constants import CELL_SIZE


class Fruit:
    def __init__(self, color, grid_w, grid_h):
        self.color = color
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.x = random.randrange(1, self.grid_w)
        self.y = random.randrange(1, self.grid_h)

    def randomize(self, snake_body):
        while True:
            self.x = random.randrange(1, self.grid_w)
            self.y = random.randrange(1, self.grid_h)
            if (self.x, self.y) not in snake_body:
                break

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         rect=pygame.Rect((CELL_SIZE * self.x, CELL_SIZE * self.y, CELL_SIZE, CELL_SIZE)))
