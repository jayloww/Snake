from typing import Tuple
import pygame
from enum import Enum
from snake import Snake
from fruit import Fruit
from constants import CELL_SIZE, SCREEN_SIZE


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
    def __init__(self, grid_w=25, grid_h=16):
        self.snake = None
        self.fruit = None
        self.font = pygame.font.SysFont("Arial", 45)
        self.state = GameState.Running
        self.grid_w, self.grid_h = grid_w, grid_h
        self.screen_w, self.screen_h = (grid_w * (CELL_SIZE), grid_h * (CELL_SIZE))
        self.reset()

    def reset(self):
        self.snake = Snake(grid_w=self.grid_w, grid_h=self.grid_h, x=1, y=1, color=(255, 255, 255))
        self.fruit = Fruit(color=(149, 42, 163), grid_h=self.grid_h, grid_w=self.grid_w, )
        self.state = GameState.Running

    def update(self, events):
        if self.state == GameState.Running:
            self.snake.update(events)
            if cords_in_rect(*self.snake.rect_list[0], self.fruit.x, self.fruit.y, 1, 1):
                self.fruit.randomize(self.snake.rect_list)
                self.snake.just_ate = True

            if self.snake.check_collide():
                self.state = GameState.Lost
        else:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.reset()

    def draw(self, screen):
        screen.fill((0, 0, 0))

        if self.state == GameState.Running:
            self.snake.draw(screen)
            self.fruit.draw(screen)
        else:
            surface_state = self.font.render(self.state.message(), False, (149, 42, 163))
            text_rect_state = surface_state.get_rect(center=(self.screen_w / 2, self.screen_h / 2 - 40))
            surface_message = self.font.render("Press <Enter> to play again", False, (149, 42, 163))
            text_rect_message = surface_state.get_rect(center=(self.screen_w / 4, self.screen_h / 2 + 20))
            screen.blit(surface_state, text_rect_state)
            screen.blit(surface_message, text_rect_message)

        pygame.display.flip()

    def get_screen_size(self) -> Tuple[int, int]:
        return self.screen_w, self.screen_h
