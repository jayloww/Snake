import pygame
import random
class Fruit:
    def __init__(self, w, h, color, screen_w, screen_h):
        self.w = w
        self.h = h
        self.color = color
        self.just_ate = False
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.x = 25 * random.randint(1, self.screen_h // 25)
        self.y = 25 * random.randint(1, self.screen_w // 25)

    def draw(self, screen):
        if self.just_ate:
            self.x = 25 * random.randint(1, self.screen_h // 25+1)
            self.y = 25 * random.randint(1, self.screen_w // 25+1)
            self.just_ate = False
            print(self.x, self.y)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

