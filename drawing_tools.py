import pygame
from pygame import font, Surface
from colors import Color
from settings import ROW_COUNT, COLUMN_COUNT, SQUARE_SIZE

pygame.init()
text_format = pygame.font.SysFont("comicsansms", 32)


def draw_board(screen):
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            paint_block(screen, ROW_COUNT, column, row,
                        Color.BLACK)


def draw_checker(screen, row, column, player):
    place_circle(screen,
                 (column * SQUARE_SIZE, (ROW_COUNT - row) * SQUARE_SIZE),
                 player.favorite_color.value)


def place_message(screen, message, position, color=Color.BLACK,
                  font_selection=text_format):
    text = font_selection.render(message, True, color)
    screen.blit(text, position)


def place_circle(screen, position, color):
    circle_radius = int(SQUARE_SIZE * .45)
    circle_position = (position[0] + circle_radius + 5, position[1] + circle_radius + 5)
    pygame.draw.circle(screen, color,
                       circle_position, circle_radius)


def paint_block(screen, rows, column, row, color):
    """
    Places a board color rectangle and then a player color circle.
    :param screen: Destination to draw on
    :param rows: Number of ROW_COUNT in game
    :param column: Column number of block to be painted
    :param row: Row number of block to be painted
    :param color: Color of circle
    :return: None
    """
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


def create_empty_block():
    block = Surface((SQUARE_SIZE, SQUARE_SIZE))
    block.fill(Color.BLUE.value)
    radius = int(SQUARE_SIZE * 0.45)
    half_square = int(SQUARE_SIZE / 2)
    pygame.draw.circle(block, Color.BLACK.value, (half_square, half_square),
                       radius)
    return block
