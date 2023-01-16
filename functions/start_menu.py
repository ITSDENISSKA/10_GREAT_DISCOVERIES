import pygame

from database import DataBase
from functions.start_statistic_window import start_statistic_window
from helpers.settings import MENU_BUTTON_INACTIVE_COLOR, MENU_BUTTON_ACTIVE_COLOR, LINE_EDIT_INACTIVE_COLOR, \
    LINE_EDIT_ACTIVE_COLOR
from widgets.line_edit import LineEdit
from widgets.menu_button import MenuButton
from functions.terminate import terminate
from helpers import settings


def start_menu(screen, timer):
    database = DataBase("database.sqlite")

    start_btn = MenuButton(480, 145, MENU_BUTTON_INACTIVE_COLOR, MENU_BUTTON_ACTIVE_COLOR, screen)
    statistic_btn = MenuButton(200, 50, MENU_BUTTON_INACTIVE_COLOR, MENU_BUTTON_ACTIVE_COLOR, screen)
    line_edit = LineEdit(330, 40, LINE_EDIT_INACTIVE_COLOR, LINE_EDIT_ACTIVE_COLOR, screen)

    menu_background = pygame.image.load("backgrounds/background.png")
    while settings.menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                line_edit.update_text(event.key, event.unicode)
                if event.key == pygame.K_SPACE:
                    settings.music_playing = not settings.music_playing
                    if settings.music_playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == pygame.K_ESCAPE:
                    database.close()
                    terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                line_edit.update_state(event.pos)

        screen.blit(menu_background, (0, 0))

        start_btn.draw(410, 250, "Начать игру", 120)
        statistic_btn.draw(1070, 660, "Статистика", 50)

        line_edit.draw(475, 190, 50)

        if statistic_btn.clicked:
            settings.statistic_window = True
            start_statistic_window(screen)
            statistic_btn = MenuButton(200, 50, MENU_BUTTON_INACTIVE_COLOR, MENU_BUTTON_ACTIVE_COLOR, screen)

        pygame.display.update()

        if len(line_edit.get_text()) >= 3:
            settings.menu = not start_btn.clicked
            settings.players_name = line_edit.get_text()
            database.add_nickname(line_edit.get_text())
            timer.start()
            settings.count_of_incorrect_answers = database.get_count_of_incorrect_answers_by_nickname(settings.players_name)
            settings.level = True
