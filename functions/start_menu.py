import pygame

from database import DataBase
from widgets.line_edit import LineEdit
from widgets.menu_button import MenuButton
from functions.terminate import terminate
from levels import levels


def start_menu(screen):
    database = DataBase("database.sqlite")

    color_inactive = pygame.Color('#A719A3')
    color_active = pygame.Color('#FF0000')

    start_btn = MenuButton(480, 145, (13, 162, 58), (23, 204, 50), screen)
    line_edit = LineEdit(330, 40, color_inactive, color_active, screen)

    menu_background = pygame.image.load("backgrounds/background.png")
    while levels.menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                line_edit.update_text(event.key, event.unicode)
                if event.key == pygame.K_SPACE:
                    flPause = not levels.flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
            if event.type == pygame.MOUSEBUTTONDOWN:
                line_edit.update_state(event.pos)

        screen.blit(menu_background, (0, 0))

        start_btn.draw(410, 250, "Начать игру", 120)

        line_edit.draw(475, 190, 50)

        levels.menu = not start_btn.clicked
        pygame.display.update()
    database.add_nickname(line_edit.get_text())
