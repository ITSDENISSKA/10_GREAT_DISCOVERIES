import time

import pygame
from helpers.settings import FONT, FONT_COLOR


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def get_time(self):
        return time.perf_counter() - self.start_time

    def stop(self):
        end_time = time.perf_counter() - self.start_time
        self.start_time = None
        return end_time

    def draw(self, screen, x, y, font_size):
        font_type = pygame.font.Font(FONT, font_size)
        text = font_type.render(f"Текущее время прохождения: {int(self.get_time()) // 60:02}:"
                                f"{int(self.get_time()) % 60:02}", True, FONT_COLOR)
        screen.blit(text, (x, y))
