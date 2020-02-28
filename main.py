import os
import sys

from game import play_match
from students import ana, gabe, harley, kaydence, josh, tim, WJR
from tournament import choose_players_from


def set_up_window():
    window_x_position = 100
    window_y_position = 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (
        window_x_position, window_y_position)


set_up_window()
students = [ana, gabe, harley, kaydence, josh, tim, WJR]
students_are_playing = True
while students_are_playing:
    player1, player2 = choose_players_from(students)
    play_match(player1, player2)

