import pygame

from database import DataBase
from functions.terminate import terminate
from helpers import settings
from helpers.settings import FONT, WHITE_BACKGROUND, FONT_COLOR, TABLE_COLOR


def start_statistic_window(screen):
    database = DataBase("database.sqlite")
    font_type = pygame.font.Font(FONT, 40)
    while settings.statistic_window:
        screen.fill(WHITE_BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    settings.music_playing = not settings.music_playing
                    if settings.music_playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == pygame.K_ESCAPE:
                    settings.statistic_window = False

        statistic = database.get_statistic()
        if type(statistic) is list:
            screen.blit(font_type.render("МЕСТО:", True, FONT_COLOR), (10, 0))
            screen.blit(font_type.render("НИКНЕЙМ:", True, FONT_COLOR), (130, 0))
            screen.blit(font_type.render("ВРЕМЯ ПРОХОЖДЕНИЯ:", True, FONT_COLOR), (480, 0))
            screen.blit(font_type.render("КОЛЛИЧЕСТВО ПОПЫТОК:", True, FONT_COLOR), (880, 0))
            for number, player in enumerate(statistic):
                screen.blit(font_type.render(str(number + 1), True, FONT_COLOR), (10, 40 * (number + 1)))
                screen.blit(font_type.render(str(player[0]), True, FONT_COLOR), (130, 40 * (number + 1)))
                if player[3]:
                    time = f"{int(player[1]) // 60:02}:{int(player[1]) % 60:02}"
                else:
                    time = "НЕ ПРОШЕЛ"
                screen.blit(font_type.render(time, True, FONT_COLOR), (480, 40 * (number + 1)))
                screen.blit(font_type.render(str(player[2]), True, FONT_COLOR), (880, 40 * (number + 1)))
                pygame.draw.line(screen, TABLE_COLOR, (0, 40 * (number + 1)), (1280, 40 * (number + 1)))
            pygame.draw.line(screen, TABLE_COLOR, (0, 40 * (len(statistic) + 1)),
                             (1280, 40 * (len(statistic) + 1)))
            pygame.draw.line(screen, TABLE_COLOR, (120, 0), (120, 40 * (len(statistic) + 1)))
            pygame.draw.line(screen, TABLE_COLOR, (470, 0), (470, 40 * (len(statistic) + 1)))
            pygame.draw.line(screen, TABLE_COLOR, (870, 0), (870, 40 * (len(statistic) + 1)))
        else:
            font_type = pygame.font.Font(FONT, 120)
            screen.blit(font_type.render("НЕ БЫЛО НИ ОДНОГО ИГРОКА", True, FONT_COLOR), (70, 325))
        pygame.display.update()
