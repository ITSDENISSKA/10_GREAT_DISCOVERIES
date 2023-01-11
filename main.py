import pygame

from functions.start_question import start_question
from settings import *
from levels import levels
from functions.start_menu import start_menu
from functions.start_level import start_level
from functions.terminate import terminate
from database import DataBase

pygame.init()
database = DataBase("database.sqlite")
database.create_database()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('10 GREAT DISCOVERIES')
CLICK_SOUND = pygame.mixer.Sound("sounds/button.wav")

start_menu(screen)

while lvl_number <= 10:
    start_level(screen, lvl_number)
    answer = start_question(screen, lvl_number, CLICK_SOUND)
    if answer:
        lvl_number += 1
    levels.level = True

terminate()
