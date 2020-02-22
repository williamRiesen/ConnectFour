import math
import sys

import pygame

from banner import draw_banner
from checker import draw_checker
from colors import Color
from drawing_tools import place_message, place_circle, draw_board, \
    create_empty_block
from game_logic import create_board, check_if_column_has_space, \
    get_next_open_row, drop_checker, check_for_win
from settings import ROW_COUNT, SQUARE_SIZE, COLUMN_COUNT
from students import bell, bubble_pop_high, bubble_pop_low

height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
screen = pygame.display.set_mode((width, height))
board = create_board()
player1 = None
player2 = None
current_player = None
photo_on_left = True


def display_player_up():
    global player1, player2
    global photo_on_left
    right_upper_corner = ((COLUMN_COUNT - 1) * SQUARE_SIZE, 0)
    left_upper_corner = (0, 0)
    right_upper_with_offset = (int((COLUMN_COUNT - 0.5) * SQUARE_SIZE),
                               int(SQUARE_SIZE * 0.5))
    left_upper_with_offset = (int(SQUARE_SIZE * 0.5), int(SQUARE_SIZE * 0.5))
    if current_player == player1:
        photo_on_left = True
        checker_position = right_upper_corner
        pygame.mouse.set_pos(right_upper_with_offset)
    else:
        photo_on_left = False
        checker_position = left_upper_corner
        pygame.mouse.set_pos(left_upper_with_offset)

    banner = draw_banner(current_player, photo_on_left)
    screen.blit(banner, (0, 0,))

    pygame.display.update()
    return banner


def declare_winner():
    global player1, player2
    bell.play()
    if current_player == player1:
        winner = player1
    else:
        winner = player2
    winner.sound.play()
    flash_winner_message(winner)

    pygame.time.wait(1000)
    pygame.draw.rect(screen, Color.BLACK.value,
                     (100, 0, 350,
                      75))
    place_message(screen, "For new match: any key", (100, 15),
                  Color.WHITE.value)
    pygame.display.update()
    return winner


def flash_winner_message(winner):
    for i in range(10):
        pygame.draw.rect(screen, Color.BLACK.value, (100, 0, 350, 75))
        pygame.display.update()
        pygame.time.wait(100)
        place_message(screen, winner.name + " Wins!", (100, 15),
                      Color.WHITE.value)
        pygame.display.update()
        pygame.time.wait(100)


def switch_players():
    global current_player
    global player1
    global player2
    if current_player == player1:
        current_player = player2
    elif current_player == player2:
        current_player = player1
    else:
        print("Error ID-ten-T: current_player must be 1 or 2.")


def set_players(new_player1, new_player2):
    global player1
    global player2
    player1 = new_player1
    player2 = new_player2


def play():
    global player1
    global player2
    global current_player
    global board
    board = create_board()
    current_player = player1
    game_in_progress = True
    draw_board(screen)
    banner = display_player_up()
    corner_to_center_offset = (int(SQUARE_SIZE / 2), int(SQUARE_SIZE / 2))
    while game_in_progress:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
                if check_if_column_has_space(board, selected_column):

                    make_move(selected_column)
                    if check_for_win(board, current_player):
                        winner = declare_winner()
                        game_in_progress = False
                    else:
                        switch_players()
                        banner = display_player_up()
                else:
                    print("This column is full.")
            elif event.type == pygame.MOUSEMOTION:
                screen.blit(banner, (0, 0))
                checker_position = (event.pos[0] - int(SQUARE_SIZE / 2),
                                    0)
                checker = draw_checker(current_player)
                screen.blit(checker, checker_position)
                pygame.display.update()
    wait_for_any_key()
    return winner


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
    empty = create_empty_block()
    prior_checker_position = (2 * SQUARE_SIZE, 2 * SQUARE_SIZE)

    for checker_height in range(0, (ROW_COUNT - selected_row + 1) * SQUARE_SIZE,
                                80):
        checker = draw_checker(current_player)
        checker_position = (selected_column * SQUARE_SIZE, checker_height)
        screen.blit(empty, prior_checker_position)
        screen.blit(checker, checker_position)
        pygame.display.update()
        prior_checker_position = checker_position
        pygame.time.wait(50)
        print(checker_height)
