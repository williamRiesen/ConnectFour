import sys
import pygame
from colors import *
from drawing_tools import SQUARE_SIZE, draw_board, place_message, place_circle
from game_logic import check_if_column_has_space, get_next_open_row, \
    check_for_win, drop_checker, create_board
from official import Official
from settings import ROW_COUNT, COLUMN_COUNT
from students import Student
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
    game_in_progress = True
    current_player = 1
    board = create_board(ROW_COUNT, COLUMN_COUNT)
    pygame.init()
    height = (ROW_COUNT + 1) * SQUARE_SIZE
    width = COLUMN_COUNT * SQUARE_SIZE
    screen = pygame.display.set_mode((width, height))
    draw_board(screen, board, player1, player2)

    while game_in_progress:
        pygame.draw.rect(screen, Color.BLACK.value, (200, 0, 300, 75))
        if current_player == 1:
            pygame.draw.rect(screen, Color.BLACK.value, (480, 0, SQUARE_SIZE,
                                                         SQUARE_SIZE))
            place_message(screen, player1.name + " is up", (200, 15),
                          Color.WHITE.value)
            screen.blit(player1.photo, (0, 0))
            place_circle(screen, (520, 0), player1.favorite_color.value)
        else:
            place_message(screen, player2.name + " is up", (200, 15),
                          Color.WHITE.value)
            pygame.draw.rect(screen, Color.BLACK.value, (0, 0, SQUARE_SIZE,
                                                         SQUARE_SIZE))
            screen.blit(player2.photo, (480, 0))
            place_circle(screen, (int(SQUARE_SIZE / 2), 0),
                         player2.favorite_color.value)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
                if check_if_column_has_space(board, selected_column):
                    selected_row = get_next_open_row(board, selected_column,
                                                     ROW_COUNT)
                    drop_checker(board, selected_row, selected_column,
                                 current_player)

                    draw_board(screen, board, player1,
                               player2)
                    if check_for_win(board, COLUMN_COUNT, ROW_COUNT,
                                     current_player):
                        if current_player == 1:
                            winner = player1
                        else:
                            winner = player2
                        for i in range(10):
                            pygame.draw.rect(screen, Color.BLACK.value, (100, 0,
                                                                         350,
                                                                         75))
                            pygame.display.update()
                            pygame.time.wait(100)
                            place_message(screen, winner.name + " Wins!",
                                          (100, 15),
                                          Color.WHITE.value)
                            pygame.display.update()
                            pygame.time.wait(100)
                        pygame.time.wait(1000)
                        pygame.draw.rect(screen, Color.BLACK.value,
                                         (100, 0, 350,
                                          75))
                        place_message(screen, "For new match: any key", (100,
                                                                         15),
                                      Color.WHITE.value)
                        pygame.display.update()
                        game_in_progress = False
                else:
                    print("This column is full.")
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
    awaiting_any_key = True
    while awaiting_any_key:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                awaiting_any_key = False
    return winner
