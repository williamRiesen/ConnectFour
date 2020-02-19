import sys
import pygame
from colors import *
from drawing_tools import SQUARE_SIZE, draw_board, place_message, place_circle
from game_logic import check_if_column_has_space, get_next_open_row, \
    check_for_win, drop_checker, create_board
from official import Official, switch_players
from settings import ROW_COUNT, COLUMN_COUNT
from sound_tools import play_checker_drop_sound
from students import Student, rubber_chicken
import math


def choose_players(students):
    scorekeeper = Official()
    scorekeeper.post_players_roster(students)
    scorekeeper.ask_who_is_player1()
    player1 = scorekeeper.get_user_selection(students)
    scorekeeper.ask_who_is_player2(player1)
    player2 = scorekeeper.get_user_selection(students, player1)
    scorekeeper.display_player2(player2)
    scorekeeper.declare_game_on()
    return player1, player2


def play_game(player1: Student, player2: Student):
    referee = Official()
    game_in_progress = True
    current_player = 1
    board = create_board(ROW_COUNT, COLUMN_COUNT)
    draw_board(referee.screen, board, player1, player2)

    while game_in_progress:
        referee.display_player_up(player1, player2, current_player)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
                if check_if_column_has_space(board, selected_column):
                    play_checker_drop_sound(player1, player2, current_player)
                    selected_row = get_next_open_row(board, selected_column,
                                                     ROW_COUNT)
                    drop_checker(board, selected_row, selected_column,
                                 current_player)

                    draw_board(referee.screen, board, player1,
                               player2)
                    if check_for_win(board, COLUMN_COUNT, ROW_COUNT,
                                     current_player):
                        winner = referee.declare_winner(player1, player2,
                                                        current_player)
                        game_in_progress = False
                else:
                    print("This column is full.")
                current_player = switch_players(current_player)

    awaiting_any_key = True
    while awaiting_any_key:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                awaiting_any_key = False
    return winner


