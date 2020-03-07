import pygame

from config import DARK_BLUE, YELLOW, BROWN, TAN, AQUA, WHITE, GOLD
from sounds import viola, rubber_chicken, mud_splat, cow


class Student:
    def __init__(self, name, photo_file, favorite_color, sound=viola, score=0):
        self.name = name
        self.photo = photo_file
        self.favorite_color = favorite_color
        self.sound = sound
        self.score = score


test_image = pygame.image.load("Photos/TestImage.bmp")
harley_photo = pygame.image.load("Photos/HarleyPhoto.bmp")
josh_photo = pygame.image.load("Photos/JoshPhoto.bmp")
tim_photo = pygame.image.load("Photos/TimPhoto.bmp")
kaydence_photo = pygame.image.load("Photos/kaydencePhoto.bmp")
ana_photo = pygame.image.load("Photos/AnaPhoto.bmp")
gabe_photo = pygame.image.load("Photos/GabePhoto.bmp")
wjr_photo = pygame.image.load("Photos/WJRPhoto.bmp")

harley = Student("Harley", harley_photo, DARK_BLUE, viola)
josh = Student("Josh", josh_photo, YELLOW, rubber_chicken)
tim = Student("Tim", tim_photo, BROWN, mud_splat)
WJR = Student("WJR", wjr_photo, TAN, viola)
kaydence = Student("Kaydence", kaydence_photo, AQUA, cow)
gabe = Student("Gabe", gabe_photo, WHITE, mud_splat)
ana = Student("Ana", ana_photo, GOLD, viola)
