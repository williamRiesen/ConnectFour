import sys
import numpy
import pygame
import math

from pygame.rect import Rect

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 80
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
ANAS_COLOR = (0, 62, 100)
TIMS_COLOR = (10, 10, 10)
JOSHS_COLOR = YELLOW
HARLEYS_COLOR = (16, 6, 66)
KAYDENCES_COLOR = (7, 23, 27)
GABES_COLOR = (255, 255, 255)
WJRS_COLOR = (225, 225, 225)
RED = (225, 0, 0)
game_in_progress = True
current_player = 1
selected_column = 0
height = (ROW_COUNT + 1) * SQUARE_SIZE
width = COLUMN_COUNT * SQUARE_SIZE
test_image = pygame.image.load("TestImage.bmp")
harley_photo = pygame.image.load("HarleyPhoto.bmp")
josh_photo = pygame.image.load("JoshPhoto.bmp")

pygame.init()
screen = pygame.display.set_mode((width, height))


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
# player2 = harley

# player1 = josh
player2 = josh

# player1 = tim
# player2 = tim

# player1 = WJR
# player2 = WJR

# player1 = kaydence
# player2 = kaydence

# player1 = gabe
# player2 = gabe

# player1 = ana
# player2 = ana

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
    print(str(player))

    board[row][column] = player
    switch_players()
    draw_board()
    pygame.display.flip()

    return player


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
        screen.blit(player1.photo, (0, 0))
        rectangle = (width - SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, BLACK, rectangle)
    else:
        screen.blit(player2.photo, (width - SQUARE_SIZE, 0))
        rectangle = (0, 0, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, BLACK, rectangle)


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
    pygame.draw.rect(screen, BLUE, rectangle)
    pygame.draw.circle(screen, color, circle_position, circle_radius)
    pygame.display.update()



#start_screen = pygame.display.set_mode((width, height))

waiting_for_user_imput = False
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

    import pygame
    import time
    import random

    pygame.init()

    display_width = 800
    display_height = 600

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    block_color = (53, 115, 255)

    car_width = 73

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Connect Four Game')
    clock = pygame.time.Clock()

   # josh_photo = pygame.image.load(josh_photo)


    def things_dodged(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: " + str(count), True, black)
        gameDisplay.blit(text, (0, 0))


    def things(thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


    def car(x, y):
        gameDisplay.blit(josh_photo, (x, y))


    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()


    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

        time.sleep(2)

        game_loop()


    def crash():
        message_display('You Crashed')


    def game_intro():

        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("Connect Four Game", largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(15)


    def game_intro():

        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


    def game_loop():
        x = (display_width * 0.45)
        y = (display_height * 0.8)

        x_change = 0

        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        thing_speed = 4
        thing_width = 100
        thing_height = 100

        thingCount = 1

        dodged = 0

        gameExit = False

        while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            x += x_change
            gameDisplay.fill(white)

            things(thing_startx, thing_starty, thing_width, thing_height,
                   block_color)

            thing_starty += thing_speed
            car(x, y)
            things_dodged(dodged)

            if x > display_width - car_width or x < 0:
                crash()

            if thing_starty > display_height:
                thing_starty = 0 - thing_height
                thing_startx = random.randrange(0, display_width)
                dodged += 1
                thing_speed += 1
                thing_width += (dodged * 1.2)

            if y < thing_starty + thing_height:
                print('y crossover')

                if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                    print('x crossover')
                    crash()

            pygame.display.update()
            clock.tick(60)


    game_intro()
    game_loop()
    pygame.quit()
    quit()


draw_board()
pygame.display.flip()

while game_in_progress:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_column = math.floor(event.pos[0] / SQUARE_SIZE)
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
    pygame.time.wait(50)
