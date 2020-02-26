import math
import sys
import pygame
from checker import draw_checker
from colors import Color
from drawing_tools import create_empty_grid, \
    PhotoPosition, create_banner
from game_logic import create_board, check_if_column_has_space, check_for_win, \
    get_next_open_row, record_move
from settings import ROW_COUNT, SQUARE_SIZE, COLUMN_COUNT
from sounds import bell, bubble_pop_high, bubble_pop_low

pygame.init()
height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
screen = pygame.display.set_mode((width, height))
checker_array = None
player1 = None
player2 = None
current_player = None
player_banner = None
player1_banner = None
player2_banner = None
photo_goes_on_left = True
game_in_progress = True
banner_with_photo = None


def play(new_player1, new_player2):
    global player1, player2, current_player, checker_array, game_in_progress, \
        banner_with_photo, player1_banner, \
        player2_banner, player_banner

    player1 = new_player1
    player2 = new_player2
    checker_array = create_board()
    display_starting_layout()

    winner = None

    while winner is None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                winner = play_move(event)
            elif event.type == pygame.MOUSEMOTION:
                slide_checker_horizontally(event)
            elif event.type == pygame.QUIT:
                sys.exit()
        pygame.time.wait(20)

    wait_for_any_key()
    return winner


def display_starting_layout():
    global player1_banner, player2_banner, current_player, player_banner
    current_player = player1
    empty_grid = create_empty_grid()
    screen.blit(empty_grid, (0, 0))
    player1_banner = create_banner(player1, PhotoPosition.LEFT, player1.name
                                   + " is up.")
    player2_banner = create_banner(player2, PhotoPosition.RIGHT, player2.name
                                   + " is up.")
    player_banner = player1_banner
    screen.blit(player1_banner, (0, 0))
    pygame.display.update()


def slide_checker_horizontally(event):
    screen.blit(player_banner, (0, 0))
    checker_position = (event.pos[0] - int(SQUARE_SIZE / 2), 0)
    checker = draw_checker(current_player)
    screen.blit(checker, checker_position)
    pygame.display.update()


def play_move(event):
    global current_player
    selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
    if check_if_column_has_space(checker_array, selected_column):
        drop_checker(selected_column)
        if check_for_win(checker_array, current_player):
            winner = current_player
            declare_winner(winner)
        else:
            switch_players()
            winner = None
    else:
        winner = None
    return winner


def switch_players():
    global player1, player2, current_player, player_banner
    if current_player == player1:
        current_player = player2
        player_banner = player2_banner
    else:
        current_player = player1
        player_banner = player1_banner
    screen.blit(player_banner, (0, 0))
    pygame.display.update()


def declare_winner(winner):
    winner_banner = create_banner(winner, PhotoPosition.LEFT, winner.name + " "
                                                                            "Wins!")
    bell.play()
    winner.sound.play()
    flash_winner_message(winner_banner)

    pygame.time.wait(1000)
    any_key_banner = create_banner(winner, PhotoPosition.LEFT, "For new match: "
                                                               "any key")
    screen.blit(any_key_banner, (0, 0))
    pygame.display.update()
    return winner


def flash_winner_message(winner_banner):
    for i in range(10):
        pygame.draw.rect(screen, Color.BLACK.value, (100, 0, 350, 75))
        pygame.display.update()
        pygame.time.wait(100)
        screen.blit(winner_banner, (0, 0))
        pygame.display.update()
        pygame.time.wait(100)


def wait_for_any_key():
    awaiting_any_key = True
    while awaiting_any_key:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                awaiting_any_key = False


def drop_checker(selected_column):
    if current_player == player1:
        bubble_pop_high.play()
    else:
        bubble_pop_low.play()
    selected_row = get_next_open_row(checker_array, selected_column,
                                     ROW_COUNT)
    record_move(checker_array, selected_row, selected_column, current_player)
    screen.blit(player_banner, (0, 0))
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
    screen.blit(player_banner, (0, 0))
    pygame.display.update()
