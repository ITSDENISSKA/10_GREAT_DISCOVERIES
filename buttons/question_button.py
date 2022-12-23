import pygame

from buttons.button import Button


class QuestionButton(Button):
    def __init__(self, width, height, inactive_color, active_color, screen, answer):
        super().__init__(width, height, inactive_color, active_color, screen)
        self.answer = answer