import math
import sys
import pygame
from colors import Color
from drawing_tools import paint_block, place_message, place_circle
from game_logic import create_board, check_if_column_has_space, \
    get_next_open_row, drop_checker, check_for_win
from settings import ROW_COUNT, SQUARE_SIZE, COLUMN_COUNT
from sound_tools import play_checker_drop_sound
from students import bell


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        height = (ROW_COUNT + 1) * SQUARE_SIZE
        width = COLUMN_COUNT * SQUARE_SIZE
        self.screen = pygame.display.set_mode((width, height))
        self.board = create_board()
        self.game_in_progress = True
        self.current_player = 1

    def draw_board(self):
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.board[row][column] == 1:
                    paint_block(self.screen, ROW_COUNT, column, row,
                                self.player1.favorite_color)
                elif self.board[row][column] == 2:
                    paint_block(self.screen, ROW_COUNT, column, row,
                                self.player2.favorite_color)
                else:
                    paint_block(self.screen, ROW_COUNT, column, row,
                                Color.BLACK)

    def display_player_up(self):
        pygame.draw.rect(self.screen, Color.BLACK.value, (200, 0, 300, 75))
        if self.current_player == 1:
            pygame.draw.rect(self.screen, Color.BLACK.value,
                             (480, 0, SQUARE_SIZE,
                              SQUARE_SIZE))
            place_message(self.screen, self.player1.name + " is up", (200, 15),
                          Color.WHITE.value)
            self.screen.blit(self.player1.photo, (0, 0))
            place_circle(self.screen, (520, 0),
                         self.player1.favorite_color.value)
        else:
            place_message(self.screen, self.player2.name + " is up", (200, 15),
                          Color.WHITE.value)
            pygame.draw.rect(self.screen, Color.BLACK.value, (0, 0, SQUARE_SIZE,
                                                              SQUARE_SIZE))
            self.screen.blit(self.player2.photo, (480, 0))
            place_circle(self.screen, (int(SQUARE_SIZE / 2), 0),
                         self.player2.favorite_color.value)
        pygame.display.update()

    def declare_winner(self):
        bell.play()
        if self.current_player == 1:
            winner = self.player1
        else:
            winner = self.player2
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

    def switch_players(self):
        if self.current_player == 1:
            self.current_player = 2
        elif self.current_player == 2:
            self.current_player = 1
        else:
            print("Error: current_player must be 1 or 2.")

    def play(self):
        while self.game_in_progress:
            self.draw_board()
            self.display_player_up()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
                    if check_if_column_has_space(self.board, selected_column):
                        play_checker_drop_sound(self.player1, self.player2,
                                                self.current_player)
                        selected_row = get_next_open_row(self.board,
                                                         selected_column,
                                                         ROW_COUNT)
                        drop_checker(self.board, selected_row, selected_column,
                                     self.current_player)
                        self.draw_board()
                        pygame.display.update()
                        self.switch_players()
                        if check_for_win(self.board, self.current_player):
                            winner = self.declare_winner()
                            self.game_in_progress = False
                    else:
                        print("This column is full.")
        wait_for_any_key()
        return winner


def wait_for_any_key():
    awaiting_any_key = True
    while awaiting_any_key:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                awaiting_any_key = False
