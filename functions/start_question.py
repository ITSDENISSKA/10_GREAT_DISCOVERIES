import pygame

from database import DataBase
from functions.draw_attempts_count import draw_attempts_count
from widgets.buttons import QuestionButton
from functions.terminate import terminate
from helpers.settings import QUESSTION_BUTTONS_TEXT, FONT, QUESTION_BUTTON_INACTIVE_COLOR, QUESTION_BUTTON_ACTIVE_COLOR
from helpers import settings


def start_question(screen, lvl_number, click_sound, timer):
    database = DataBase("database.sqlite")
    database.update_time_by_nickname(settings.players_name, timer.get_time())

    while settings.question:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    settings.music_playing = not settings.music_playing
                    if settings.music_playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
            if event.type == pygame.QUIT:
                terminate()
        menu_background = pygame.image.load(f"backgrounds/question{lvl_number}.png")
        screen.blit(menu_background, (0, 0))

        true_btn = QuestionButton(400, 120, QUESTION_BUTTON_INACTIVE_COLOR, QUESTION_BUTTON_ACTIVE_COLOR, screen, True)
        false1_btn = QuestionButton(400, 120, QUESTION_BUTTON_INACTIVE_COLOR, QUESTION_BUTTON_ACTIVE_COLOR, screen, False)
        false2_btn = QuestionButton(400, 120, QUESTION_BUTTON_INACTIVE_COLOR, QUESTION_BUTTON_ACTIVE_COLOR, screen, False)
        true_btn.draw(440, 280, QUESSTION_BUTTONS_TEXT[f"level{lvl_number}"][0], 90)
        false1_btn.draw(100, 450, QUESSTION_BUTTONS_TEXT[f"level{lvl_number}"][1], 90)
        false2_btn.draw(780, 450, QUESSTION_BUTTONS_TEXT[f"level{lvl_number}"][2], 90)
        if true_btn.clicked:
            settings.question = False
            click_sound.play()
            return True
        elif false2_btn.clicked or false1_btn.clicked:
            settings.question = False
            settings.count_of_incorrect_answers += 1
            database.increment_count_of_incorrect_answers_by_nickname(settings.players_name)
            return False

        draw_attempts_count(screen, 0, 40)
        timer.draw(screen, 640, 0, 40)

        pygame.display.update()
