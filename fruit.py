import pygame
import random


class Fruit:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        self.color = color
        self.fruit_list = []

    def draw(self, screen, screen_w, screen_h):
        if not self.fruit_list:
            x = 25 * random.randint(1, screen_h//25)
            y = 25 * random.randint(1, screen_w//25)
            self.fruit_list.append(x)
            self.fruit_list.append(y)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.fruit_list[0], self.fruit_list[1], self.w, self.h))

