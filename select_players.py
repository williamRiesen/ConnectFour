from drawing_tools import place_message, place_circle, SQUARE_SIZE
from students import *
import math
from colors import Color


def select_players() -> object:
    """
    Presents a screen for the user to select two players from a list of all
    the students, shown by name, photo, and piece color.
    :return: two Student objects, player1 and player2
    """
    width = 560
    height = 560
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    screen.fill(Color.BLUE.value)
    pygame.display.update()

    place_message(screen, "CONNECT", (15, 5), Color.YELLOW.value)
    place_message(screen, "FOUR!", (15, 40), Color.YELLOW.value)
    place_message(screen, "Who will be", (5, 150), Color.WHITE.value)
    place_message(screen, "Player 1 ?", (20, 190), Color.WHITE.value)

    for student in students:
        y_position = students.index(student) * SQUARE_SIZE
        place_message(screen, student.name, (300, y_position + 20), Color.TAN.value)
        screen.blit(student.photo, (200, y_position))
        place_circle(screen, (500, y_position), student.favorite_color.value)
    pygame.display.update()

    player1 = get_user_selection(screen)
    pygame.draw.rect(screen, Color.BLUE.value, (5, 150, 180, 90))
    place_message(screen, "Player 1", (10, 100), Color.WHITE.value)
    screen.blit(player1.photo, (25, 150))
    place_message(screen, player1.name, (10, 230), Color.WHITE.value)
    pygame.display.update()
    pygame.time.wait(500)
    place_message(screen, "Who will be", (5, 350), Color.WHITE.value)
    place_message(screen, "Player 2 ?", (20, 390), Color.WHITE.value)
    pygame.display.update()

    player2 = get_user_selection(screen, player1)
    pygame.draw.rect(screen, Color.BLUE.value, (5, 350, 180, 90))
    place_message(screen, "Player 2", (10, 320), Color.WHITE.value)
    screen.blit(player2.photo, (25, 370))
    place_message(screen, player2.name, (10, 450), Color.WHITE.value)
    pygame.display.update()
    pygame.time.wait(500)

    for i in range(7):
        pygame.draw.rect(screen, Color.RED.value, (5, 280, 180, 40))
        place_message(screen, "GAME ON!", (10, 275), Color.WHITE.value)
        pygame.display.update()
        pygame.time.wait(100)
        pygame.draw.rect(screen, Color.BLUE.value, (5, 280, 180, 40))
        pygame.display.update()
        pygame.time.wait(100)
    return player1, player2


def get_user_selection(screen, already_selected=None):
    waiting_for_user = True
    highlighted_student = harley
    while waiting_for_user:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_y_position = event.pos[1]
                row = math.floor(mouse_y_position / 80)
                if students[row] != highlighted_student and students[
                    row] != already_selected:
                    previously_highlighted_student = highlighted_student
                    highlighted_student = students[row]
                    place_message(screen, highlighted_student.name,
                                  (300, row * SQUARE_SIZE + 20), Color.WHITE.value)
                    place_message(screen, previously_highlighted_student.name,
                                  (300, students.index(
                                      previously_highlighted_student) *
                                   SQUARE_SIZE + 20), Color.TAN.value)
                    pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player = highlighted_student
                waiting_for_user = False
    return player
