import sys
import numpy
import pygame
import math

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 80
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
RED =(225,0,0)
game_in_progress = True
current_player = 1
selected_column = 0
height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE


def create_board():
    return numpy.zeros((ROW_COUNT, COLUMN_COUNT))


def check_if_column_has_space(column):
    return board[ROW_COUNT - 1][column] == 0


def get_next_open_row(column):
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row


def drop_checker(row, column, player):
    board[row][column] = player


def draw_board():
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            if board[row][column]==1:
                paint_block(column, row, YELLOW)
            elif board[row][column]==2:
                paint_block(column, row, RED)
            else:
                paint_block(column, row, BLACK)


def check_for_win():
    for column in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][column] == current_player and \
                    board[row][column + 1] == current_player and \
                    board[row][column + 2] == current_player and \
                    board[row][column + 3] == current_player:
                return True
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][column] == current_player and \
                    board[row + 1][column] == current_player and \
                    board[row + 2][column] == current_player and \
                    board[row + 3][column] == current_player:
                return True
    for column in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][column] == current_player and \
                    board[row + 1][column + 1] == current_player and \
                    board[row + 2][column + 2] == current_player and \
                    board[row + 3][column + 3] == current_player:
                return True
    for column in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][column] == current_player and \
                    board[row - 1][column + 1] == current_player and \
                    board[row - 2][column + 2] == current_player and \
                    board[row - 3][column + 3] == current_player:
                return True


def paint_block(column, row, color):
    screen_row = ROW_COUNT - row
    x_position = column * SQUARE_SIZE
    y_position = screen_row * SQUARE_SIZE
    rectangle = (x_position, y_position, SQUARE_SIZE, SQUARE_SIZE)
    circle_position = (x_position + int(SQUARE_SIZE / 2), y_position + int(
        SQUARE_SIZE / 2))
    circle_radius = int(SQUARE_SIZE * 0.45)
    pygame.draw.rect(screen, BLUE, rectangle)
    pygame.draw.circle(screen, color, circle_position, circle_radius)
    pygame.display.update()


board = create_board()
pygame.init()
screen = pygame.display.set_mode((width, height))
draw_board()
pygame.display.flip()
while game_in_progress:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
            if check_if_column_has_space(selected_column):
                selected_row = get_next_open_row(selected_column)
                drop_checker(selected_row, selected_column, current_player)
            else:
                print("This column is full.")
#     if check_for_win():
#         print("Player " + str(current_player) + " wins!")
#         game_in_progress = False
    draw_board()
    pygame.time.wait(50)
    if current_player == 1:
         current_player = 2
    elif current_player == 2:
       current_player = 1
