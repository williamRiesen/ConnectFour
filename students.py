import pygame
from colors import *


class Student:
    def __init__(self, name, photo_file, favorite_color, score):
        self.name = name
        self.photo = photo_file
        self.favorite_color = favorite_color
        self.score = score


test_image = pygame.image.load("Photos/TestImage.bmp")
harley_photo = pygame.image.load("Photos/HarleyPhoto.bmp")
josh_photo = pygame.image.load("Photos/JoshPhoto.bmp")
tim_photo = pygame.image.load("Photos/TimPhoto.bmp")
kaydence_photo = pygame.image.load("Photos/kaydencePhoto.bmp")
ana_photo = pygame.image.load("Photos/AnaPhoto.bmp")
gabe_photo = pygame.image.load("Photos/GabePhoto.bmp")
wjr_photo = pygame.image.load("Photos/WJRPhoto.bmp")

harley = Student("Harley", harley_photo, Color.HARLEYS_COLOR, 0)
josh = Student("Josh", josh_photo, Color.YELLOW, 0)
tim = Student("Tim", tim_photo, Color.TIMS_COLOR, 0)
WJR = Student("WJR", wjr_photo, Color.TAN, 0)
kaydence = Student("Kaydence", kaydence_photo, Color.KAYDENCES_COLOR, 0)
gabe = Student("Gabe", gabe_photo, Color.GABES_COLOR, 0)
ana = Student("Ana", ana_photo, Color.TEAL, 0)

