import pygame

from helpers.settings import FONT
from helpers import settings


def draw_attempts_count(screen, y, font_size):
    screen_x, screen_y, screen_width, screen_height = screen.get_rect()
    background_surface = pygame.Surface((screen_width, font_size))
    background_surface.fill((187, 187, 187))
    background_surface.set_alpha(200)
    screen.blit(background_surface, (screen_x, y))
    font_type = pygame.font.Font(FONT, font_size)
    text = font_type.render(f"Количество неправильных ответов: {settings.count_of_incorrect_answers}", True, (0, 0, 0))
    screen.blit(text, (0, y))
