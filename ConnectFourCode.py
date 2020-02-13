import sys
import numpy
import pygame
from pygame import font

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 80
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
WHITE = (255,255,255)
ANAS_COLOR = (0, 62, 100)
TIMS_COLOR = (10, 10, 10)
JOSHS_COLOR = YELLOW
HARLEYS_COLOR = (16, 6, 66)
KAYDENCES_COLOR = (7, 23, 27)
GABES_COLOR = (255, 255, 255)
WJRS_COLOR = (225, 225, 225)
RED = (225, 0, 0)
current_player = 1
height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
test_image = pygame.image.load("TestImage.bmp")
harley_photo = pygame.image.load("HarleyPhoto.bmp")
josh_photo = pygame.image.load("JoshPhoto.bmp")

pygame.init()
game_screen = pygame.display.set_mode((width, height))
intro_screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Student:
    def __init__(self, name, photo_file, favorite_color, score):
        self.name = name
        self.photo = photo_file
        self.favorite_color = favorite_color
        self.score = score


harley = Student("Harley", harley_photo, HARLEYS_COLOR, 0)
josh = Student("Josh", josh_photo, JOSHS_COLOR, 0)
tim = Student("Tim", test_image, TIMS_COLOR, 0)
WJR = Student("WJR", test_image, WJRS_COLOR, 0)
kaydence = Student("Kaydence", test_image, KAYDENCES_COLOR, 0)
gabe = Student("Gabe", test_image, GABES_COLOR, 0)
ana = Student("Ana", test_image, ANAS_COLOR, 0)

player1 = harley
player2 = josh


def create_board():
    return numpy.zeros((ROW_COUNT, COLUMN_COUNT))


board = create_board()


def check_if_column_has_space(column):
    return board[ROW_COUNT - 1][column] == 0


def get_next_open_row(column):
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row


def drop_checker(row, column, player):
    board[row][column] = player


def switch_players():
    if current_player == 1:
        return 2
    else:
        return 1


def draw_board():
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            if board[row][column] == 1:
                paint_block(column, row, player1.favorite_color)
            elif board[row][column] == 2:
                paint_block(column, row, player2.favorite_color)
            else:
                paint_block(column, row, BLACK)
    if current_player == 1:
        game_screen.blit(player1.photo, (0, 0))
        rectangle = (width - SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(game_screen, BLACK, rectangle)
    else:
        game_screen.blit(player2.photo, (width - SQUARE_SIZE, 0))
        rectangle = (0, 0, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(game_screen, BLACK, rectangle)


def check_for_win():
    for column in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][column] == current_player and \
                    board[row][column + 1] == current_player and \
                    board[row][column + 2] == current_player and \
                    board[row][column + 3] == current_player:
                return True
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 3):
            if board[row][column] == current_player and \
                    board[row + 1][column] == current_player and \
                    board[row + 2][column] == current_player and \
                    board[row + 3][column] == current_player:
                return True
    for column in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 3):
            if board[row][column] == current_player and \
                    board[row + 1][column + 1] == current_player and \
                    board[row + 2][column + 2] == current_player and \
                    board[row + 3][column + 3] == current_player:
                return True
    for column in range(COLUMN_COUNT - 3):
        for row in range(3, ROW_COUNT):
            if board[row][column] == current_player and \
                    board[row - 1][column + 1] == current_player and \
                    board[row - 2][column + 2] == current_player and \
                    board[row - 3][column + 3] == current_player:
                return True


def paint_block(column, row, color):
    screen_row = ROW_COUNT - row
    x_position = column * SQUARE_SIZE
    y_position = screen_row * SQUARE_SIZE
    rectangle = (x_position, y_position, SQUARE_SIZE, SQUARE_SIZE)
    circle_position = (x_position + int(SQUARE_SIZE / 2), y_position + int(
        SQUARE_SIZE / 2))
    circle_radius = int(SQUARE_SIZE * 0.45)
    pygame.draw.rect(game_screen, BLUE, rectangle)
    pygame.draw.circle(game_screen, color, circle_position, circle_radius)
    pygame.display.update()


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



def game_intro():
    intro_is_running = True
    game_screen.fill(ANAS_COLOR)
    free_sans_bold = pygame.font.Font('freesansbold.ttf', 32)
    comic_sans = pygame.font.SysFont("comicsansms", 36)
    small_text = pygame.font.Font('freesansbold.ttf', 32)
    text_surf, text_rect = text_objects("Please select Player 1:", comic_sans)
    text_rect.center = ((width / 2), (height / 6))
    game_screen.blit(text_surf, text_rect)


    text = free_sans_bold.render("Connect Four by FTC 6025", True, YELLOW)
    game_screen.blit(text,(0,0))


    pygame.display.update()

    while intro_is_running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        clock.tick(15)


def game_loop():
    game_in_progress = True
    selected_column = 0
    while game_in_progress:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected_column = numpy.math.floor(event.pos[0] / SQUARE_SIZE)
            if check_if_column_has_space(selected_column):
                selected_row = get_next_open_row(selected_column)
                current_player = drop_checker(selected_row,
                                              selected_column, current_player)
            if check_for_win():
                print("Player " + str(current_player) + " wins!")
                pygame.time.wait(3000)
                game_in_progress = False

            else:
                print("This column is full.")
        if current_player == 1:
            current_player = 2
        elif current_player == 2:
            current_player = 1
    pygame.display.update()
    clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
