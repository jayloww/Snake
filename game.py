import pygame


def cords_in_rect(x, y, rect_x, rect_y, rect_w, rect_h):
    return rect_x <= x <= rect_x + rect_w and rect_y <= y <= rect_y + rect_h

class Game:
    def __init__(self, w, h, snake, fruit):
        self.w = h
        self.h = h
        self.snake = snake
        self.fruit = fruit
        self.state = "ongoing"


    def update(self, events):
        self.snake.update(events)
        if self.fruit.fruit_list:
            if cords_in_rect(*self.snake.rect_list[0], self.fruit.fruit_list[0], self.fruit.fruit_list[1], self.fruit.w, self.fruit.h):
                self.fruit.fruit_list = []
                self.snake.just_ate = True


    def draw(self, screen):
        screen.fill((0, 0, 0))

        if self.state == "ongoing":
            self.snake.draw(screen)
            self.fruit.draw(screen, self.w, self.h)

        pygame.display.flip()

