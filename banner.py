import pygame

from colors import Color
from drawing_tools import place_message
from settings import SQUARE_SIZE, COLUMN_COUNT

height = SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
black_banner_background = pygame.Surface((width, height))
print(width, height)
banner_with_photo_only = pygame.Surface((width, height))
photo = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))


def update_banner_with_photo(player, photo_on_left):
    banner_with_photo_only.blit(black_banner_background, (0, 0))
    photo.blit(player.photo, (0, 0))
    if photo_on_left:
        photo_position = (0, 0)
    else:
        photo_position = ((COLUMN_COUNT - 1) * SQUARE_SIZE, 0)
    banner_with_photo_only.blit(photo, photo_position)

    return banner_with_photo_only
