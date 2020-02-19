import pygame
from colors import *

rubber_chicken = pygame.mixer.Sound('Sounds/rubber-chicken.wav')
cow = pygame.mixer.Sound("Sounds/cow.wav")
mud_splat = pygame.mixer.Sound("Sounds/mud-splat.wav")
viola = pygame.mixer.Sound('Sounds/viola.wav')
bell = pygame.mixer.Sound("Sounds/hand-bell.wav")


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

harley = Student("Harley", harley_photo, Color.HARLEYS_COLOR, viola)
josh = Student("Josh", josh_photo, Color.YELLOW, mud_splat)
tim = Student("Tim", tim_photo, Color.TIMS_COLOR)
WJR = Student("WJR", wjr_photo, Color.TAN, cow)
kaydence = Student("Kaydence", kaydence_photo, Color.KAYDENCES_COLOR)
gabe = Student("Gabe", gabe_photo, Color.GABES_COLOR)
ana = Student("Ana", ana_photo, Color.TEAL)
