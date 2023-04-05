import pygame
from enum import Enum

CELL_SIZE = 25


class GameState(Enum):
    Running = 0
    Lost = 1
    Won = 2

    def message(self) -> str:
        if self == self.Running:
            raise ValueError("No message for running state")
        elif self == self.Lost:
            return "You lost"
        elif self == self.Won:
            return "You won"
        raise ValueError(f"Exhaustive handling of GameState: {self.value}")


def cords_in_rect(x, y, rect_x, rect_y, rect_w, rect_h):
    return rect_x <= x < rect_x + rect_w and rect_y <= y < rect_y + rect_h


class Game:
    def __init__(self, screen_w, screen_h, snake, fruit):
        self.snake = snake
        self.fruit = fruit
        self.font = pygame.font.SysFont("Arial", 45)
        self.state = GameState.Running
        self.screen_w = screen_w
        self.screen_h = screen_h

    def update(self, events):
        self.snake.update(events)
        if cords_in_rect(*self.snake.rect_list[0], self.fruit.x, self.fruit.y, 1, 1):
            self.fruit.randomize(self.snake.rect_list)
            self.snake.just_ate = True

        if self.snake.check_collide():
            self.state = GameState.Lost

    def draw(self, screen):
        screen.fill((0, 0, 0))

        if self.state == GameState.Running:
            self.snake.draw(screen)
            self.fruit.draw(screen)
        else:
            surface_state = self.font.render(self.state.message(), False, (149, 42, 163))
            text_rect_state = surface_state.get_rect(center=(self.screen_w / 2, self.screen_h / 2))

            screen.blit(surface_state, text_rect_state)
        pygame.display.flip()
