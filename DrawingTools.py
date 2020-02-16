import pygame
from pygame import font

from Colors import *

SQUARE_SIZE = 80
pygame.init()
title_format = pygame.font.Font('freesansbold.ttf', 36)
regular_text_format = pygame.font.SysFont("comicsansms", 32)
small_text_format = pygame.font.Font('freesansbold.ttf', 14)


def draw_board(screen, board, rows, columns, player1, player2):
    for row in range(rows):
        for column in range(columns):
            if board[row][column] == 1:
                paint_block(screen, rows, column, row, player1.favorite_color)
            elif board[row][column] == 2:
                paint_block(screen, rows, column, row, player2.favorite_color)
            else:
                paint_block(screen, rows, column, row, BLACK)
    # if current_player == 1:
    #     game_screen.blit(player1.photo, (0, 0))
    #     rectangle = (width - SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE)
    #     pygame.draw.rect(game_screen, BLACK, rectangle)
    # else:
    #     game_screen.blit(player2.photo, (width - SQUARE_SIZE, 0))
    #     rectangle = (0, 0, SQUARE_SIZE, SQUARE_SIZE)
    #     pygame.draw.rect(game_screen, BLACK, rectangle)


def place_message(screen, message, position, color=BLACK,
                  font_selection=regular_text_format):
    text = font_selection.render(message, True, color)
    screen.blit(text, position)


def place_circle(screen, position, color):
    circle_radius = int(SQUARE_SIZE * .45)
    circle_position = (position[0], position[1] + circle_radius + 5)
    pygame.draw.circle(screen, color,
                       circle_position, circle_radius, )
    if color == TEAL:
        pygame.draw.circle(screen, BLACK,
                           circle_position, circle_radius, 2)


def paint_block(screen, rows, column, row, color):
    screen_row = rows - row
    x_position = column * SQUARE_SIZE
    y_position = screen_row * SQUARE_SIZE
    rectangle = (x_position, y_position, SQUARE_SIZE, SQUARE_SIZE)
    circle_position = (x_position + int(SQUARE_SIZE / 2), y_position + int(
        SQUARE_SIZE / 2))
    circle_radius = int(SQUARE_SIZE * 0.45)
    pygame.draw.rect(screen, BLUE, rectangle)
    pygame.draw.circle(screen, color, circle_position, circle_radius)
    pygame.display.update()