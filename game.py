import math
import os
import sys

import pygame

from banner import update_banner_with_photo
from checker import draw_checker
from colors import Color
from drawing_tools import place_message, draw_board
from game_logic import create_board, check_if_column_has_space, check_for_win, \
    get_next_open_row, drop_checker
from settings import ROW_COUNT, SQUARE_SIZE, COLUMN_COUNT
from sounds import bell, bubble_pop_high, bubble_pop_low

window_x_position = 100
window_y_position = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
    window_x_position, window_y_position)
pygame.init()
height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
screen = pygame.display.set_mode((width, height))
board = None
player1 = None
player2 = None
current_player = None
photo_goes_on_left = True
winner = None
game_in_progress = True
banner_with_photo_and_text = None


def play(new_player1, new_player2):
    global player1, player2, current_player, board, game_in_progress, banner_with_photo_and_text
    game_in_progress = True
    set_players(new_player1, new_player2)
    board = create_board()
    current_player = player1
    draw_board(screen)
    display_player_up()
    place_message(banner_with_photo_and_text, current_player.name + " is up", (200, 15),
                  Color.WHITE.value)
    screen.blit(banner_with_photo_and_text, (0, 0))
    pygame.display.update()

    while game_in_progress:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(event)
            elif event.type == pygame.MOUSEMOTION:
                handle_mouse_motion(event)
    wait_for_any_key()
    return winner


def display_player_up():
    global player1, player2, photo_goes_on_left, banner_with_photo_and_text
    if current_player == player1:
        photo_goes_on_left = True
    else:
        photo_goes_on_left = False
    banner_with_photo_and_text = update_banner_with_photo(current_player, photo_goes_on_left)
    screen.blit(banner_with_photo_and_text, (0, 0,))
    pygame.display.update()


def declare_winner():
    global player1, player2, winner
    if current_player == player1:
        winner = player1
    else:
        winner = player2
    bell.play()
    winner.sound.play()
    flash_winner_message()

    pygame.time.wait(1000)
    display_player_up()
    screen.blit(banner_with_photo_and_text, (0, 0))
    place_message(screen, "For new match: any key", (100, 15),
                  Color.WHITE.value)
    pygame.display.update()
    return winner


def flash_winner_message():
    global winner
    for i in range(10):
        pygame.draw.rect(screen, Color.BLACK.value, (100, 0, 350, 75))
        pygame.display.update()
        pygame.time.wait(100)
        place_message(screen, winner.name + " Wins!", (100, 15),
                      Color.WHITE.value)
        pygame.display.update()
        pygame.time.wait(100)


def switch_players():
    global player1, player2, current_player, banner_with_photo_and_text
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
    display_player_up()
    place_message(banner_with_photo_and_text, current_player.name + " is up", (200, 15),
                  Color.WHITE.value)
    screen.blit(banner_with_photo_and_text, (0, 0))
    pygame.display.update()


def set_players(new_player1, new_player2):
    global player1, player2
    player1 = new_player1
    player2 = new_player2


def handle_mouse_motion(event):
    screen.blit(banner_with_photo_and_text, (0, 0))
    checker_position = (event.pos[0] - int(SQUARE_SIZE / 2), 0)
    checker = draw_checker(current_player)
    screen.blit(checker, checker_position)
    pygame.display.update()


def handle_click(event):
    global winner, game_in_progress
    selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
    if check_if_column_has_space(board, selected_column):
        make_move(selected_column)
        if check_for_win(board, current_player):
            winner = declare_winner()
            game_in_progress = False
        else:
            switch_players()


def wait_for_any_key():
    awaiting_any_key = True
    while awaiting_any_key:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                awaiting_any_key = False


def make_move(selected_column):
    if current_player == player1:
        bubble_pop_high.play()
    else:
        bubble_pop_low.play()
    selected_row = get_next_open_row(board, selected_column,
                                     ROW_COUNT)
    drop_checker(board, selected_row, selected_column, current_player)
    screen.blit(banner_with_photo_and_text, (0, 0))
    background_column = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE * (ROW_COUNT
                                                                    + 1)))
    drop_column = pygame.Rect(SQUARE_SIZE * selected_column, 0, SQUARE_SIZE,
                              (SQUARE_SIZE * (ROW_COUNT + 1)))
    background_column.blit(screen, (0, 0), drop_column)
    checker = draw_checker(current_player)
    for checker_height in range(0, (ROW_COUNT - selected_row + 1) * SQUARE_SIZE,
                                80):
        checker_position = (selected_column * SQUARE_SIZE, checker_height)
        screen.blit(background_column, (selected_column * SQUARE_SIZE, 0))
        screen.blit(checker, checker_position)
        pygame.display.update()
        pygame.time.wait(50)
    place_message(banner_with_photo_and_text, current_player.name + " is up", (200, 15),
                  Color.WHITE.value)
    screen.blit(banner_with_photo_and_text, (0, 0))
    pygame.display.update()
    print("Screen updated.")
