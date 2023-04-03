import pygame

CELL_SIZE = 25


def cords_in_rect(x, y, rect_x, rect_y, rect_w, rect_h):
    return rect_x <= x < rect_x + rect_w and rect_y <= y < rect_y + rect_h


class Game:
    def __init__(self, snake, fruit):
        self.snake = snake
        self.fruit = fruit
        self.state = "ongoing"

    def update(self, events):
        self.snake.update(events)
        if cords_in_rect(*self.snake.rect_list[0], self.fruit.x, self.fruit.y, 1, 1):
            self.fruit.randomize(self.snake.rect_list)
            self.snake.just_ate = True

    def draw(self, screen):
        screen.fill((0, 0, 0))

        if self.state == "ongoing":
            self.snake.draw(screen)
            self.fruit.draw(screen)

        pygame.display.flip()
