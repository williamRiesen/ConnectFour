from enum import Enum
import pygame
from pygame import font, Surface
from colors import Color
from settings import ROW_COUNT, COLUMN_COUNT, SQUARE_SIZE

pygame.init()
text_format = pygame.font.SysFont("comicsansms", 32)


class PhotoPosition(Enum):
    RIGHT = (ROW_COUNT * SQUARE_SIZE, 0)
    LEFT = (0, 0)


def create_banner(player, photo_position, message):
    banner = Surface((COLUMN_COUNT * SQUARE_SIZE, SQUARE_SIZE))
    banner.blit(player.photo, photo_position.value)
    text = text_format.render(message, True, Color.WHITE.value)
    margin = int((banner.get_rect().width - text.get_rect().width) / 2)
    banner.blit(text, (margin, 15))
    return banner


def create_player_banner(player, photo_position):
    banner = Surface((COLUMN_COUNT * SQUARE_SIZE, SQUARE_SIZE))
    banner.blit(player.photo, photo_position.value)
    message = player.name + " is up."
    text = text_format.render(message, True, Color.WHITE.value)
    margin = int((banner.get_rect().width - text.get_rect().width) / 2)
    banner.blit(text, (margin, 15))
    return banner


def create_winner_banner(player, photo_position):
    banner = Surface((COLUMN_COUNT * SQUARE_SIZE, SQUARE_SIZE))
    banner.blit(player.photo, photo_position.value)
    message = player.name + " Wins!"
    text = text_format.render(message, True, Color.WHITE.value)
    banner.blit(text, (150, 15))
    return banner


def create_any_key_banner(player, photo_position):
    banner = Surface((COLUMN_COUNT * SQUARE_SIZE, SQUARE_SIZE))
    banner.blit(player.photo, photo_position.value)
    message = "For new match: any key"
    text = text_format.render(message, True, Color.WHITE.value)
    banner.blit(text, (100, 15))
    return banner


def create_empty_grid(screen):
    empty_grid = Surface(
        (COLUMN_COUNT * SQUARE_SIZE, (ROW_COUNT + 1) * SQUARE_SIZE))
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            paint_block(empty_grid, ROW_COUNT, column, row,
                        Color.BLACK)
    return empty_grid


def create_banner_message(screen, message, position, color=Color.BLACK,
                          font_selection=text_format):
    banner_message = Surface((COLUMN_COUNT * SQUARE_SIZE, SQUARE_SIZE))
    banner_message.set_colorkey(Color.BLACK.value)
    text = font_selection.render(message, True, color)
    banner_message.blit(text, position)
    return banner_message


def place_circle(screen, position, color):
    circle_radius = int(SQUARE_SIZE * .45)
    circle_position = (
        position[0] + circle_radius + 5, position[1] + circle_radius + 5)
    pygame.draw.circle(screen, color,
                       circle_position, circle_radius)


def paint_block(screen, rows, column, row, color):
    screen_row = rows - row
    x_position = column * SQUARE_SIZE
    y_position = screen_row * SQUARE_SIZE
    rectangle = (x_position, y_position, SQUARE_SIZE, SQUARE_SIZE)
    circle_position = (x_position + int(SQUARE_SIZE / 2), y_position + int(
        SQUARE_SIZE / 2))
    circle_radius = int(SQUARE_SIZE * 0.45)
    pygame.draw.rect(screen, Color.BLUE.value, rectangle)
    pygame.draw.circle(screen, color.value, circle_position, circle_radius)
    pygame.display.update()
