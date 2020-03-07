import math

import pygame

from config import ROW_COUNT, COLUMN_COUNT, SQUARE_SIZE
from drawing_tools import draw_checker
from sounds import checker_drop_1
from students import gabe


def animate_checker_fall(column, row, color):
    screen_height = (ROW_COUNT + 1) * SQUARE_SIZE
    width = COLUMN_COUNT * SQUARE_SIZE
    starting_height = screen_height
    final_height = (ROW_COUNT - row) * SQUARE_SIZE


    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, screen_height))
    background = screen.copy()
    checker = draw_checker(gabe)
    checker_height = starting_height
    checker_speed = 0
    gravity = - 4
    still_falling = True
    checker_drop_1.play()
    while still_falling:
        checker_speed += gravity
        checker_height += checker_speed
        screen.blit(background, (0, 0))
        if checker_height < final_height:
            checker_height = final_height
            still_falling = False
        checker_position = column * SQUARE_SIZE, screen_height - checker_height
        clock.tick(40)
        screen.blit(checker, checker_position)
        pygame.display.update()


    pygame.time.wait(1000)
