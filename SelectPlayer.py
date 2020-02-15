import numpy
import pygame

from Colors import *
from DrawingTools import place_message, place_circle, SQUARE_SIZE
from Students import *


def select_players():
    width = 560
    height = 560
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    screen.fill(TEAL)
    pygame.display.update()

    place_message(screen, "CONNECT", (15, 5), YELLOW)
    place_message(screen, "FOUR!", (15, 40), YELLOW)
    place_message(screen, "Who will be", (5, 150), WHITE)
    place_message(screen, "Player 1 ?", (20, 190), WHITE)
    name_y_position = 0
    for student in students:
        place_message(screen, student.name, (300, name_y_position + 20),
                      TAN)
        screen.blit(student.photo, (200, name_y_position))
        place_circle(screen, name_y_position, student.favorite_color)
        name_y_position += SQUARE_SIZE
    pygame.display.update()
    player1 = get_user_selection(screen)
    pygame.draw.rect(screen, TEAL, (5, 150, 180, 90))
    place_message(screen, "Player 1", (10, 100), WHITE)
    screen.blit(player1.photo, (25, 150))
    place_message(screen, player1.name, (10, 240), WHITE)
    pygame.display.update()
    pygame.time.wait(2000)
    place_message(screen, "Who will be", (5, 350), WHITE)
    place_message(screen, "Player 2 ?", (20, 390), WHITE)
    pygame.display.update()
    player2 = get_user_selection(screen)
    return player1, player2


def get_user_selection(screen):
    intro_is_running = True
    highlighted_student = harley
    while intro_is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_y_position = event.pos[1]
                mouse_over_row = numpy.math.floor(mouse_y_position / 80)
                if students[mouse_over_row] != highlighted_student:
                    previously_highlighted_student = highlighted_student
                    highlighted_student = students[mouse_over_row]
                    place_message(screen, highlighted_student.name,
                                  (300, mouse_over_row * SQUARE_SIZE + 20),
                                  WHITE)
                    place_message(screen, previously_highlighted_student.name,
                                  (300, students.index(
                                      previously_highlighted_student) *
                                   SQUARE_SIZE + 20),
                                  TAN)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player1 = highlighted_student

                intro_is_running = False
    return player1
