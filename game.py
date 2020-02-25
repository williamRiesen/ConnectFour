import math
import os
import sys
import pygame
from banner import update_banner_with_photo
from checker import draw_checker
from colors import Color
from drawing_tools import create_banner_message, create_empty_grid, \
    create_player_banner, PhotoPosition, create_winner_banner, \
    create_any_key_banner, create_banner
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
player_banner = None
player1_banner = None
player2_banner = None
photo_goes_on_left = True
winner = None
game_in_progress = True
banner_with_photo = None
banner_with_photo_and_message = None


def play(new_player1, new_player2):
    global player1, player2, current_player, board, game_in_progress, \
        banner_with_photo, banner_with_photo_and_message, player1_banner, \
        player2_banner, player_banner
    game_in_progress = True
    set_players(new_player1, new_player2)
    board = create_board()
    current_player = player1
    empty_grid = create_empty_grid(screen)
    screen.blit(empty_grid, (0, 0))
    player1_banner = create_banner(player1, PhotoPosition.LEFT, player1.name
                                   + " is up.")
    player2_banner = create_banner(player2, PhotoPosition.RIGHT, player2.name
                                   + " is up.")
    player_banner = player1_banner
    screen.blit(player1_banner, (0, 0))
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


def create_banner_with_photo():
    global player1, player2, photo_goes_on_left, banner_with_photo
    if current_player == player1:
        photo_goes_on_left = True
    else:
        photo_goes_on_left = False
    banner_with_photo = update_banner_with_photo(current_player,
                                                 photo_goes_on_left)
    return banner_with_photo


def declare_winner():
    global player1, player2, winner
    if current_player == player1:
        winner = player1
        photo_position = PhotoPosition.LEFT
    else:
        winner = player2
        photo_position = PhotoPosition.RIGHT
    winner_banner = create_banner(winner, photo_position, winner.name + " "
                                                                        "Wins!")
    bell.play()
    winner.sound.play()
    flash_winner_message(winner_banner)

    pygame.time.wait(1000)
    any_key_banner = create_banner(winner, photo_position, "For new match: "
                                                           "any key")
    screen.blit(any_key_banner, (0, 0))
    pygame.display.update()
    return winner


def flash_winner_message(winner_banner):
    global winner
    for i in range(10):
        pygame.draw.rect(screen, Color.BLACK.value, (100, 0, 350, 75))
        pygame.display.update()
        pygame.time.wait(100)
        screen.blit(winner_banner, (0, 0))
        pygame.display.update()
        pygame.time.wait(100)


def switch_players():
    global player1, player2, current_player, banner_with_photo, \
        player_banner
    if current_player == player1:
        current_player = player2
        player_banner = player2_banner
    else:
        current_player = player1
        player_banner = player1_banner
    create_banner_with_photo()
    create_banner_message(banner_with_photo, current_player.name + " is up",
                          (200, 15),
                          Color.WHITE.value)
    screen.blit(player_banner, (0, 0))
    pygame.display.update()


def set_players(new_player1, new_player2):
    global player1, player2
    player1 = new_player1
    player2 = new_player2


def handle_mouse_motion(event):
    screen.blit(player_banner, (0, 0))
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
    create_banner_message(banner_with_photo, current_player.name + " is up",
                          (200, 15),
                          Color.WHITE.value)
    screen.blit(player_banner, (0, 0))
    pygame.display.update()
