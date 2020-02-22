import pygame

from colors import Color
from settings import SQUARE_SIZE


def draw_checker(player):
    checker = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
    checker.set_colorkey(Color.BLACK.value)
    radius = int(SQUARE_SIZE * 0.45)
    center = (int(SQUARE_SIZE * 0.5), int(SQUARE_SIZE * 0.5))
    pygame.draw.circle(checker, player.favorite_color.value, center, radius)
    return checker
