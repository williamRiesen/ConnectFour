import pygame
from pygame import Surface
from enum import Enum
from config import ROW_COUNT, COLUMN_COUNT, SQUARE_SIZE, WHITE, BLACK, BLUE
from tournament import text_format


class PhotoPosition(Enum):
    RIGHT = (ROW_COUNT * SQUARE_SIZE, 0)
    LEFT = (0, 0)


def create_banner(player, photo_position, message):
    banner = Surface((COLUMN_COUNT * SQUARE_SIZE, SQUARE_SIZE))
    banner.blit(player.photo, photo_position.value)
    text = text_format.render(message, True, WHITE)
    margin = int((banner.get_rect().width - text.get_rect().width) / 2)
    banner.blit(text, (margin, 15))
    return banner


def create_empty_grid():
    empty_grid = Surface(
        (COLUMN_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE))
    empty_grid.set_colorkey((0, 0, 0))
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            draw_block(empty_grid, column, row)
    return empty_grid


def draw_block(screen, column, row):
    screen_row = ROW_COUNT - row
    x_position = column * SQUARE_SIZE
    y_position = screen_row * SQUARE_SIZE
    rectangle = (x_position, y_position, SQUARE_SIZE, SQUARE_SIZE)
    circle_position = (x_position + int(SQUARE_SIZE / 2), y_position + int(
        SQUARE_SIZE / 2))
    circle_radius = int(SQUARE_SIZE * 0.45)
    pygame.draw.rect(screen, BLUE, rectangle)
    pygame.draw.circle(screen, BLACK, circle_position, circle_radius)
    pygame.display.update()


def draw_checker(player):
    checker = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
    checker.set_colorkey(BLACK)
    radius = int(SQUARE_SIZE * 0.5)
    center = (int(SQUARE_SIZE * 0.5), int(SQUARE_SIZE * 0.5))
    pygame.draw.circle(checker, player.favorite_color, center, radius)
    return checker


def create_checker_layer(checker_array, player1, player2):
    checker_layer = Surface(
        (COLUMN_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE))
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            whose_checker = checker_array[row][column]
            if whose_checker != 0:
                destination = (column * SQUARE_SIZE, (ROW_COUNT - row) *
                               SQUARE_SIZE)
                checker = draw_checker(whose_checker)
                checker_layer.blit(checker, destination)
    return checker_layer
