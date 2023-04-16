import pygame
from game import Game

pygame.init()
game = Game()
screen = pygame.display.set_mode(game.get_screen_size())
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
fps = 10

active = True
while active:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            active = False

    clock.tick(fps)
    game.update(events)
    game.draw(screen)
