import pygame
from enum import Enum
from game import CELL_SIZE


class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3


class Snake:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect_list = [(self.x, self.y), (self.x - CELL_SIZE, self.y), (self.x - 2 * CELL_SIZE, self.y),
                          (self.x - 3 * CELL_SIZE, self.y)]
        self.just_ate = False
        self.direction = Direction.East

    def move(self):
        if self.direction == Direction.West:
            self.x -= 1
            self.rect_list.insert(0, (self.x, self.y))
        elif self.direction == Direction.East:
            self.x += 1
            self.rect_list.insert(0, (self.x, self.y))
        elif self.direction == Direction.North:
            self.y -= 1
            self.rect_list.insert(0, (self.x, self.y))
        elif self.direction == Direction.South:
            self.y += 1
            self.rect_list.insert(0, (self.x, self.y))
        if self.just_ate:
            self.just_ate = False
        else:
            self.rect_list = self.rect_list[:-1]

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.direction != Direction.East:
                        self.direction = Direction.West
                if event.key == pygame.K_RIGHT:
                    if self.direction != Direction.West:
                        self.direction = Direction.East
                if event.key == pygame.K_UP:
                    if self.direction != Direction.South:
                        self.direction = Direction.North
                if event.key == pygame.K_DOWN:
                    if self.direction != Direction.North:
                        self.direction = Direction.South
        self.move()

    def draw(self, screen):
        for x, y in self.rect_list:
            pygame.draw.rect(screen, self.color, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def __repr__(self):
        return f"Snake = (x={self.x}, y={self.y}, color={self.color})"
