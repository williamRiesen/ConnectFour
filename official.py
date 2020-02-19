import math
import pygame
from colors import Color
from drawing_tools import regular_text_format, place_circle, place_message
from settings import COLUMN_COUNT, SQUARE_SIZE, ROW_COUNT
from students import bell, cow


def switch_players(current_player):
    if current_player == 1:
        return 2
    elif current_player == 2:
        return 1
    else:
        print("Error: current_player must be 1 or 2.")


class Official:
    def __init__(self):
        height = (ROW_COUNT + 1) * SQUARE_SIZE
        width = COLUMN_COUNT * SQUARE_SIZE
        self.screen = pygame.display.set_mode((width, height))

    def place_message(self, message, position=(0, 0), color=Color.BLACK,
                      font_selection=regular_text_format):
        text = font_selection.render(message, True, color.value)
        self.screen.blit(text, position)

    def fill(self, color):
        self.screen.fill(color.value)

    def place_circle(self, position=(100, 100), color=Color.WHITE):
        circle_radius = int(SQUARE_SIZE * .45)
        circle_position = (position[0], position[1] + circle_radius + 5)
        pygame.draw.circle(self.screen, color.value,
                           circle_position, circle_radius, )
        if color == Color.TEAL:
            pygame.draw.circle(self.screen, Color.BLACK,
                               circle_position, circle_radius, 2)

    def post_players_roster(self, students):
        self.fill(Color.BLUE)
        for student in students:
            y_position = students.index(student) * SQUARE_SIZE
            self.place_message(student.name,
                               (300, y_position + 20),
                               Color.TAN)
            self.screen.blit(student.photo, (200, y_position))
            place_circle(self.screen, (500, y_position),
                         student.favorite_color.value)
        pygame.display.update()

    def ask_who_is_player1(self):
        pygame.display.set_caption("Select Players")
        self.place_message("CONNECT", (15, 5), Color.YELLOW)
        self.place_message("FOUR!", (15, 40), Color.YELLOW)
        self.place_message("Who will be", (5, 150), Color.WHITE)
        self.place_message("Player 1 ?", (20, 190), Color.WHITE)
        pygame.display.update()

    def get_user_selection(self, students, already_selected=None):
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
                    if students[row] != highlighted_student and students[
                        row] != already_selected:
                        previously_highlighted_student = highlighted_student
                        highlighted_student = students[row]
                        place_message(self.screen,
                                      highlighted_student.name,
                                      (300, row * SQUARE_SIZE + 20),
                                      Color.WHITE.value)
                        place_message(self.screen,
                                      previously_highlighted_student.name,
                                      (300, students.index(
                                          previously_highlighted_student) *
                                       SQUARE_SIZE + 20), Color.TAN.value)
                        pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    player = highlighted_student
                    waiting_for_user = False
        return player

    def ask_who_is_player2(self, player1):
        pygame.draw.rect(self.screen, Color.BLUE.value, (5, 150, 180, 90))
        place_message(self.screen, "Player 1", (10, 100), Color.WHITE.value)
        self.screen.blit(player1.photo, (25, 150))
        place_message(self.screen, player1.name, (10, 230), Color.WHITE.value)
        pygame.display.update()
        pygame.time.wait(500)
        place_message(self.screen, "Who will be", (5, 350), Color.WHITE.value)
        place_message(self.screen, "Player 2 ?", (20, 390), Color.WHITE.value)
        pygame.display.update()

    def display_player2(self, player2):
        pygame.draw.rect(self.screen, Color.BLUE.value, (5, 350, 180, 90))
        place_message(self.screen, "Player 2", (10, 320), Color.WHITE.value)
        self.screen.blit(player2.photo, (25, 370))
        place_message(self.screen, player2.name, (10, 450), Color.WHITE.value)
        pygame.display.update()
        pygame.time.wait(500)

    def declare_game_on(self):
        cow.play()
        for i in range(14):
            pygame.draw.rect(self.screen, Color.RED.value, (5, 280, 180, 40))
            place_message(self.screen, "GAME ON!", (10, 275), Color.WHITE.value)
            pygame.display.update()
            pygame.time.wait(100)
            pygame.draw.rect(self.screen, Color.BLUE.value, (5, 280, 180, 40))
            pygame.display.update()
            pygame.time.wait(100)

    def display_player_up(self, player1, player2, current_player):
        pygame.draw.rect(self.screen, Color.BLACK.value, (200, 0, 300, 75))
        if current_player == 1:
            pygame.draw.rect(self.screen, Color.BLACK.value,
                             (480, 0, SQUARE_SIZE,
                              SQUARE_SIZE))
            place_message(self.screen, player1.name + " is up", (200, 15),
                          Color.WHITE.value)
            self.screen.blit(player1.photo, (0, 0))
            place_circle(self.screen, (520, 0), player1.favorite_color.value)
        else:
            place_message(self.screen, player2.name + " is up", (200, 15),
                          Color.WHITE.value)
            pygame.draw.rect(self.screen, Color.BLACK.value, (0, 0, SQUARE_SIZE,
                                                              SQUARE_SIZE))
            self.screen.blit(player2.photo, (480, 0))
            place_circle(self.screen, (int(SQUARE_SIZE / 2), 0),
                         player2.favorite_color.value)
        pygame.display.update()

    def declare_winner(self, player1, player2, current_player):
        bell.play()
        if current_player == 1:
            winner = player1
        else:
            winner = player2
        self.flash_winner_message(winner)

        pygame.time.wait(1000)
        pygame.draw.rect(self.screen, Color.BLACK.value,
                         (100, 0, 350,
                          75))
        place_message(self.screen, "For new match: any key", (100, 15),
                      Color.WHITE.value)
        pygame.display.update()
        return winner

    def flash_winner_message(self, winner):
        for i in range(10):
            pygame.draw.rect(self.screen, Color.BLACK.value, (100, 0, 350, 75))
            pygame.display.update()
            pygame.time.wait(100)
            place_message(self.screen, winner.name + " Wins!", (100, 15),
                          Color.WHITE.value)
            pygame.display.update()
            pygame.time.wait(100)
