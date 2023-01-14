import pygame

from functions.start_question import start_question
from helpers.settings import *
from levels import levels
from functions.start_menu import start_menu
from functions.start_level import start_level
from functions.terminate import terminate
from helpers.timer import Timer
from database import DataBase

pygame.init()
database = DataBase("database.sqlite")
timer = Timer()

database.create_database()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('10 GREAT DISCOVERIES')
CLICK_SOUND = pygame.mixer.Sound("sounds/button.wav")

clock = pygame.time.Clock()


start_menu(screen)
timer.start()
while lvl_number <= 10:
    start_level(screen, lvl_number, timer)
    answer = start_question(screen, lvl_number, CLICK_SOUND, timer)
    if answer:
        lvl_number += 1
    levels.level = True
    clock.tick(FPS)

terminate()
