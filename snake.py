import pygame
from game import Game, CELL_SIZE
from snake_character import Snake
from fruit import Fruit

grid_w, grid_h = 25, 16
w, h = grid_w * CELL_SIZE, grid_h * CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
fps = 10
snake = Snake(x=1, y=1, color=(255, 255, 255))
fruit = Fruit(color=(149, 42, 163), grid_h=grid_h, grid_w=grid_w)
game = Game(snake=snake, fruit=fruit)

active = True
while active:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            active = False

    clock.tick(fps)
    game.update(events)
    game.draw(screen)
