import sys
import numpy
import pygame
from Colors import *
from pygame import font

from DrawingTools import SQUARE_SIZE
from Students import *

from GameLogic import check_for_win, check_if_column_has_space, \
    get_next_open_row
from SelectPlayer import select_players

ROW_COUNT = 6
COLUMN_COUNT = 7

current_player = 1
height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE

pygame.init()
game_screen = pygame.display.set_mode((width, height))
intro_screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

player1 = harley
player2 = josh


def create_board():
    return numpy.zeros((ROW_COUNT, COLUMN_COUNT))


board = create_board()


def drop_checker(row, column, player):
    board[row][column] = player


def switch_players():
    if current_player == 1:
        return 2
    else:
        return 1


def draw_board():
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            if board[row][column] == 1:
                paint_block(column, row, player1.favorite_color)
            elif board[row][column] == 2:
                paint_block(column, row, player2.favorite_color)
            else:
                paint_block(column, row, BLACK)
    if current_player == 1:
        game_screen.blit(player1.photo, (0, 0))
        rectangle = (width - SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(game_screen, BLACK, rectangle)
    else:
        game_screen.blit(player2.photo, (width - SQUARE_SIZE, 0))
        rectangle = (0, 0, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(game_screen, BLACK, rectangle)


def paint_block(column, row, color):
    screen_row = ROW_COUNT - row
    x_position = column * SQUARE_SIZE
    y_position = screen_row * SQUARE_SIZE
    rectangle = (x_position, y_position, SQUARE_SIZE, SQUARE_SIZE)
    circle_position = (x_position + int(SQUARE_SIZE / 2), y_position + int(
        SQUARE_SIZE / 2))
    circle_radius = int(SQUARE_SIZE * 0.45)
    pygame.draw.rect(game_screen, BLUE, rectangle)
    pygame.draw.circle(game_screen, color, circle_position, circle_radius)
    pygame.display.update()


def text_objects(text, font):
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()


def message_display(screen, text):
    large_text = pygame.font.Font('freesansbold.ttf')
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((width / 2), (height / 2))
    screen.blit(text_surf, text_rect)
    pygame.display.update()
    pygame.time.sleep(2)
    game_loop()


def game_loop():
    game_in_progress = True
    selected_column = 0
    while game_in_progress:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_column = numpy.math.floor(event.pos[0] / SQUARE_SIZE)
            if check_if_column_has_space(board, selected_column, ROW_COUNT):
                selected_row = get_next_open_row(board, selected_column,
                                                 ROW_COUNT)
                drop_checker(selected_row, selected_column, current_player)
            if check_for_win(board, COLUMN_COUNT, ROW_COUNT, current_player):
                print("Player " + str(current_player) + " wins!")
                pygame.time.wait(3000)
                game_in_progress = False

            else:
                print("This column is full.")
    #        if current_player == 1:
    #          current_player = 2
    #      elif current_player == 2:
    #           current_player = 1
    pygame.display.update()
    clock.tick(60)


player1, player2 = select_players()
print("Player 1 is " + player1.name)
print("Player 2 is " + player2.name)
pygame.time.wait(3000)
# game_intro()
# game_loop()
pygame.quit()
quit()
