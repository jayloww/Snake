import pygame
from enum import Enum


class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3


class Snake:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.rect_list = [(self.x, self.y), (self.x - self.w, self.y), (self.x - 2 * self.w, self.y),
                          (self.x - 3 * self.w, self.y)]
        self.just_ate = False
        self.direction = Direction.East

    def move(self):
        if self.direction == Direction.West:
            self.x -= 25
            self.rect_list.insert(0, (self.x, self.y))
        elif self.direction == Direction.East:
            self.x += 25
            self.rect_list.insert(0, (self.x, self.y))
        elif self.direction == Direction.North:
            self.y -= 25
            self.rect_list.insert(0, (self.x, self.y))
        elif self.direction == Direction.South:
            self.y += 25
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
        for rectangle in self.rect_list:
            pygame.draw.rect(screen, self.color, pygame.Rect(*rectangle, self.w, self.h))

    def __repr__(self):
        return f"Snake = (x={self.x}, y={self.y}, w ={self.w}, h={self.h}, color={self.color})"
