import pygame
from pygame import font

from Colors import *

SQUARE_SIZE = 80
pygame.init()
title_format = pygame.font.Font('freesansbold.ttf', 36)
regular_text_format = pygame.font.SysFont("comicsansms", 32)
small_text_format = pygame.font.Font('freesansbold.ttf', 14)


def place_message(screen, message, position, color=BLACK,
                  font_selection=regular_text_format):
    text = font_selection.render(message, True, color)
    screen.blit(text, position)


def place_circle(screen, y_position, color):
    circle_radius = int(SQUARE_SIZE * .45)
    circle_position = (500, y_position + circle_radius + 5)
    pygame.draw.circle(screen, color,
                       circle_position, circle_radius, )
    if color == TEAL:
        pygame.draw.circle(screen, BLACK,
                           circle_position, circle_radius, 2)
