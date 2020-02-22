import math
import pygame
from colors import Color
from drawing_tools import text_format
from settings import COLUMN_COUNT, SQUARE_SIZE, ROW_COUNT
from students import bell

height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
screen = pygame.display.set_mode((width, height))


def choose_players(students):
    post_players_roster(students)
    ask_who_is_player1()
    player1 = get_user_selection(students)
    ask_who_is_player2(player1)
    player2 = get_user_selection(students, player1)
    display_player2(player2)
    declare_game_on()
    return player1, player2


def place_message(message, position=(0, 0), color=Color.BLACK,
                  font_selection=text_format):
    text = font_selection.render(message, True, color.value)

    screen.blit(text, position)


def fill(color):
    screen.fill(color.value)


def place_circle(position=(100, 100), color=Color.WHITE):
    circle_radius = int(SQUARE_SIZE * .45)
    circle_position = (position[0], position[1] + circle_radius + 5)
    pygame.draw.circle(screen, color, circle_position, circle_radius)

    if color == Color.TEAL:
        pygame.draw.circle(screen, Color.BLACK,
                           circle_position, circle_radius, 2)


def post_players_roster(students):
    fill(Color.BLUE)
    for student in students:
        y_position = students.index(student) * SQUARE_SIZE
        place_message(student.name, (300, y_position + 20), Color.TAN)

        screen.blit(student.photo, (200, y_position))
        place_circle((500, y_position),
                     student.favorite_color.value)
    pygame.display.update()


def ask_who_is_player1():
    pygame.display.set_caption("Select Players")
    place_message("CONNECT", (15, 5), Color.YELLOW)
    place_message("FOUR!", (15, 40), Color.YELLOW)
    place_message("Who will be", (5, 150), Color.WHITE)
    place_message("Player 1 ?", (20, 190), Color.WHITE)
    pygame.display.update()


def get_user_selection(students, already_selected=None):
    waiting_for_user = True
    highlighted_student = students[0]
    while waiting_for_user:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_y_position = event.pos[1]
                row = math.floor(mouse_y_position / 80)
                if students[row] != highlighted_student and students[row] != already_selected:
                    previously_highlighted_student = highlighted_student
                    highlighted_student = students[row]
                    place_message(highlighted_student.name,
                                  (300, row * SQUARE_SIZE + 20),
                                  Color.WHITE)
                    place_message(previously_highlighted_student.name,
                                  (300, students.index(
                                      previously_highlighted_student) *
                                   SQUARE_SIZE + 20), Color.TAN)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player = highlighted_student
                highlighted_student.sound.play()
                waiting_for_user = False
    return player


def ask_who_is_player2(player1):
    pygame.draw.rect(screen, Color.BLUE.value, (5, 150, 180, 90))
    place_message("Player 1", (10, 100), Color.WHITE)
    screen.blit(player1.photo, (25, 150))
    place_message(player1.name, (10, 230), Color.WHITE)
    pygame.display.update()
    pygame.time.wait(500)
    place_message("Who will be", (5, 350), Color.WHITE)
    place_message("Player 2 ?", (20, 390), Color.WHITE)
    pygame.display.update()


def display_player2(player2):
    pygame.draw.rect(screen, Color.BLUE.value, (5, 350, 180, 90))
    place_message("Player 2", (10, 320), Color.WHITE)
    screen.blit(player2.photo, (25, 370))
    place_message(player2.name, (10, 450), Color.WHITE)
    pygame.display.update()
    pygame.time.wait(500)


def declare_game_on():
    bell.play()
    for i in range(14):
        pygame.draw.rect(screen, Color.RED.value, (5, 280, 180, 40))
        place_message("GAME ON!", (10, 275), Color.WHITE)
        pygame.display.update()
        pygame.time.wait(100)
        pygame.draw.rect(screen, Color.BLUE.value, (5, 280, 180, 40))
        pygame.display.update()
        pygame.time.wait(100)
