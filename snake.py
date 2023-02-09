import pygame
from game import Game
from snake_character import Snake
from fruit import Fruit

w, h = 640, 400

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
fps = 10

snake = Snake(x=25, y=25, w=25, h=25, color=(255, 255, 255))
fruit = Fruit(w=25, h=25, color=(149, 42, 163), screen_h=h, screen_w=w)
game = Game(w=w, h=h, snake=snake, fruit=fruit)

active = True
while active:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            active = False

    clock.tick(fps)

    game.update(events)
    game.draw(screen)
