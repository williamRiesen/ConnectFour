import sys
import numpy
from pygame import font
from DrawingTools import SQUARE_SIZE
from Game import game_loop
from GameLogic import check_for_win, check_if_column_has_space, \
    get_next_open_row
from SelectPlayers import select_players
from Students import *

ROW_COUNT = 6
COLUMN_COUNT = 7

player1 = harley
player2 = josh


# def switch_players():
#     if current_player == 1:
#         return 2
#     else:
#         return 1


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


while True:
    player1, player2 = select_players()
    game_loop(ROW_COUNT, COLUMN_COUNT, player1, player2)

