import pygame

from database import DataBase
from functions.terminate import terminate
from helpers import settings
from helpers.settings import FONT, WHITE, BLACK


def start_statistic_window(screen):
    database = DataBase("database.sqlite")
    font_type = pygame.font.Font(FONT, 40)
    while settings.statistic_window:
        screen.fill(WHITE)
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
            screen.blit(font_type.render("МЕСТО:", True, BLACK), (10, 0))
            screen.blit(font_type.render("НИКНЕЙМ:", True, BLACK), (130, 0))
            screen.blit(font_type.render("ВРЕМЯ ПРОХОЖДЕНИЯ:", True, BLACK), (480, 0))
            screen.blit(font_type.render("КОЛЛИЧЕСТВО ПОПЫТОК:", True, BLACK), (880, 0))
            for number, player in enumerate(statistic):
                screen.blit(font_type.render(str(number + 1), True, BLACK), (10, 40 * (number + 1)))
                screen.blit(font_type.render(str(player[0]), True, BLACK), (130, 40 * (number + 1)))
                if player[3]:
                    time = f"{int(player[1]) // 60:02}:{int(player[1]) % 60:02}"
                else:
                    time = "НЕ ПРОШЕЛ"
                screen.blit(font_type.render(time, True, BLACK), (480, 40 * (number + 1)))
                screen.blit(font_type.render(str(player[2]), True, BLACK), (880, 40 * (number + 1)))
                pygame.draw.line(screen, BLACK, (0, 40 * (number + 1)), (1280, 40 * (number + 1)))
            pygame.draw.line(screen, BLACK, (0, 40 * (len(statistic) + 1)),
                             (1280, 40 * (len(statistic) + 1)))
            pygame.draw.line(screen, BLACK, (120, 0), (120, 40 * (len(statistic) + 1)))
            pygame.draw.line(screen, BLACK, (470, 0), (470, 40 * (len(statistic) + 1)))
            pygame.draw.line(screen, BLACK, (870, 0), (870, 40 * (len(statistic) + 1)))
        else:
            font_type = pygame.font.Font(FONT, 120)
            screen.blit(font_type.render("НЕ БЫЛО НИ ОДНОГО ИГРОКА", True, BLACK), (70, 325))
        pygame.display.update()
