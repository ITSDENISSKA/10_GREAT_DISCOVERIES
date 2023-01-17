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

infoObject = pygame.display.Info()
pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

database.create_database()

pygame.display.set_caption('10 GREAT DISCOVERIES')

clock = pygame.time.Clock()

while settings.game:
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED + pygame.NOFRAME + pygame.FULLSCREEN)
    click_sound = pygame.mixer.Sound("sounds/button.wav")
    pygame.mixer.music.load("sounds/music.wav")
    pygame.mixer.music.play(-1)
    start_menu(screen, timer)
    while settings.lvl_number <= 10:
        if settings.lvl_number % 2 != 0:
            start_maze_level(screen, settings.lvl_number, timer)
        else:
            start_platformer_level(screen, settings.lvl_number, timer)
        answer = start_question(screen, settings.lvl_number, click_sound, timer)
        if answer:
            settings.lvl_number += 1
        settings.level = True
        clock.tick(FPS)

    database.set_passed_game_by_nickname(settings.players_name)
    RESIZED_FINAL_VIDEO.preview()

    settings.lvl_number = 1
    settings.menu = True
    settings.level = False
    settings.question = False

database.close()
terminate()
