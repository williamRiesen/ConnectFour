import math
import sys
import pygame
from drawing_tools import create_empty_grid, \
    PhotoPosition, create_banner, draw_checker
from game_logic import create_board, check_if_column_has_space, check_for_win, \
    get_next_open_row, record_move
from config import ROW_COUNT, SQUARE_SIZE, COLUMN_COUNT, BLACK
from sounds import bell, bubble_pop_high, bubble_pop_low

height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
pygame.init()
screen = pygame.display.set_mode((width, height))
player1, player2, current_player = None, None, None
player1_banner, player2_banner, current_player_banner = None, None, None
checker_array = create_board()


def play_match(entry1, entry2):
    global checker_array, player1_banner, player2_banner, \
        current_player_banner, current_player
    pygame.display.set_caption("Connect Four!")
    register_players(entry1, entry2)
    checker_array = create_board()
    construct_starting_layout()
    winner = None
    current_player = player1
    current_player_banner = player1_banner

    while winner is None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
                winner = play_move(selected_column)
            elif event.type == pygame.MOUSEMOTION:
                slide_checker_horizontally_to(event.pos[0])
            elif event.type == pygame.QUIT:
                sys.exit()
        pygame.time.wait(20)

    wait_for_any_key(winner)
    return winner


def register_players(entry1, entry2):
    global player1, player2
    player1 = entry1
    player2 = entry2


def construct_starting_layout():
    global player1_banner, player2_banner
    player1_banner = create_banner(player1, PhotoPosition.LEFT, player1.name
                                   + " is up.")
    player2_banner = create_banner(player2, PhotoPosition.RIGHT, player2.name
                                   + " is up.")
    screen.blit(player1_banner, (0, 0))
    empty_grid = create_empty_grid()
    screen.blit(empty_grid, (0, 0))
    pygame.display.update()


def slide_checker_horizontally_to(x_position):
    screen.blit(current_player_banner, (0, 0))
    checker_position = (x_position - int(SQUARE_SIZE / 2), 0)
    checker = draw_checker(current_player)
    screen.blit(checker, checker_position)
    pygame.display.update()


def play_move(selected_column):
    global current_player
    move_is_legal = check_if_column_has_space(checker_array, selected_column)
    if move_is_legal:
        drop_checker(selected_column)
        move_wins = check_for_win(checker_array, current_player)
        if move_wins:
            winner = current_player
            declare_winner(winner)
        else:
            switch_players()
            winner = None
    else:
        winner = None
    return winner


def drop_checker(selected_column):
    if current_player == player1:
        bubble_pop_high.play()
    else:
        bubble_pop_low.play()
    selected_row = get_next_open_row(checker_array, selected_column)
    record_move(checker_array, selected_row, selected_column, current_player)
    screen.blit(current_player_banner, (0, 0))
    background_column = pygame.Surface((SQUARE_SIZE,
                                        SQUARE_SIZE * (ROW_COUNT + 1)))
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
    screen.blit(current_player_banner, (0, 0))
    pygame.display.update()


def switch_players():
    global current_player_banner, current_player
    if current_player == player1:
        current_player = player2
        current_player_banner = player2_banner
    else:
        current_player = player1
        current_player_banner = player1_banner
    screen.blit(current_player_banner, (0, 0))
    pygame.display.update()
    return current_player


def declare_winner(winner):
    winner_banner = create_banner(winner, PhotoPosition.LEFT,
                                  winner.name + " Wins!")
    bell.play()
    winner.sound.play()
    flash_winner_message(winner_banner)
    pygame.time.wait(1000)


def flash_winner_message(winner_banner):
    for i in range(10):
        pygame.draw.rect(screen, BLACK, (100, 0, 350, 75))
        pygame.display.update()
        pygame.time.wait(100)
        screen.blit(winner_banner, (0, 0))
        pygame.display.update()
        pygame.time.wait(100)


def wait_for_any_key(winner):
    any_key_banner = create_banner(winner, PhotoPosition.LEFT,
                                   "For new match: any key")
    screen.blit(any_key_banner, (0, 0))
    pygame.display.update()
    awaiting_any_key = True
    while awaiting_any_key:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                awaiting_any_key = False
        pygame.time.wait(20)
