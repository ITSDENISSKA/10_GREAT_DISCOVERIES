import pygame

from functions.start_question import start_question
from helpers.settings import *
from functions.start_menu import start_menu
from functions.start_level import start_maze_level, start_platformer_level
from functions.terminate import terminate
from helpers.timer import Timer
from database import DataBase
from helpers import settings

pygame.init()
database = DataBase("database.sqlite")
timer = Timer()

database.create_database()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('10 GREAT DISCOVERIES')
CLICK_SOUND = pygame.mixer.Sound("sounds/button.wav")

pygame.mixer.music.load("sounds/music.wav")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

start_menu(screen, timer)
while lvl_number <= 10:
    if lvl_number % 2 != 0:
        start_maze_level(screen, lvl_number, timer)
    else:
        start_platformer_level(screen, lvl_number, timer)
    answer = start_question(screen, lvl_number, CLICK_SOUND, timer)
    if answer:
        lvl_number += 1
    settings.level = True
    clock.tick(FPS)
database.set_passed_game_by_nickname(settings.players_name)

database.close()
terminate()
