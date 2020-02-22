import pygame

from colors import Color
from drawing_tools import place_message
from settings import SQUARE_SIZE, COLUMN_COUNT

height = SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
background = pygame.Surface((width, height))
print(width, height)
banner = pygame.Surface((width, height))
photo = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))


def erase_banner():
    banner.blit(background, (0, 0))


def draw_photo(player):
    photo.blit(player.photo, (0, 0))


def draw_banner(player, photo_on_left):
    erase_banner()
    draw_photo(player)
    if photo_on_left:
        photo_position = (0, 0)
    else:
        photo_position = ((COLUMN_COUNT - 1) * SQUARE_SIZE, 0)
    banner.blit(photo, photo_position)
    place_message(banner, player.name + " is up", (200, 15),
                  Color.WHITE.value)
    return banner
