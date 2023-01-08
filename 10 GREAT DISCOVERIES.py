import pygame
import sys

from moviepy.editor import VideoFileClip

from settings import *
from levels import levels
from functions.start_level import start_level
from functions.terminate import terminate
from buttons.menu_button import MenuButton
from database import DataBase

pygame.mixer.pre_init(*MUSIC_SETTINGS)

pygame.init()
database = DataBase("database.sqlite")
database.create_database()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('10 GREAT DISCOVERIES')
click = pygame.mixer.Sound("sounds/button.wav")
pygame.mixer.music.load("sounds/music.wav")
pygame.mixer.music.play(-1)
lvl_number = 1
run = True

clip = VideoFileClip('video/123.mp4')

while levels.menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not levels.flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    menu_background = pygame.image.load("backgrounds/background.png")
    screen.blit(menu_background, (0, 0))

    start_btn = MenuButton(480, 145, (13, 162, 58), (23, 204, 50), screen)

    start_btn.draw(410, 225, "Начать игру", 120)
    levels.menu = not start_btn.clicked
    pygame.display.update()


# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while lvl_number <= 10:
    level = start_level(screen, click, lvl_number)
    if level:
        lvl_number += 1
    levels.running = True


terminate()
