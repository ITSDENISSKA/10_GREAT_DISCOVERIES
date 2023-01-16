import pygame

from helpers.settings import FONT, FONT_COLOR


class LineEdit:
    def __init__(self, width, height, inactive_color, active_color, screen):
        self.text_surface = None
        self.y = None
        self.x = None
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.screen = screen
        self.color = self.inactive_color
        self.active = False
        self.text = ""

    def draw(self, x, y, font_size):
        self.x = x
        self.y = y

        font_type = pygame.font.Font(FONT, font_size)
        text = font_type.render(self.text, True, FONT_COLOR)
        font = pygame.font.Font(None, 50)

        if self.active:
            pygame.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height), 2)
            self.text_surface = font.render(self.text, True, self.active_color)

        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height), 2)
            self.text_surface = font.render(self.text, True, self.inactive_color)

        self.screen.blit(text, (x, y))

    def update_state(self, *args):
        pos_x, pos_y = args[0]
        if args:
            if self.x <= pos_x <= self.x + self.width and self.y <= pos_y <= self.y + self.height:
                self.active = not self.active

    def update_text(self, *args):
        key, unicode = args
        if self.active:
            pass
            if key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if self.text_surface.get_width() < 300:
                    self.text += unicode

    def get_text(self):
        return self.text
