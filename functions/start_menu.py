import pygame

from buttons.menu_button import MenuButton
from functions.terminate import terminate
from levels import levels


def start_menu(screen):
    font = pygame.font.Font(None, 50)
    input_box = pygame.Rect(475, 190, 330, 40)
    color_inactive = pygame.Color('#A719A3')
    color_active = pygame.Color('#FF0000')
    color = color_inactive
    active = False
    text = ""
    txt_surface = font.render(text, True, color)
    while levels.menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if txt_surface.get_width() < 300:
                            text += event.unicode
                if event.key == pygame.K_SPACE:
                    flPause = not levels.flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
        menu_background = pygame.image.load("backgrounds/background.png")
        screen.blit(menu_background, (0, 0))

        start_btn = MenuButton(480, 145, (13, 162, 58), (23, 204, 50), screen)
        start_btn.draw(410, 250, "Начать игру", 120)

        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        levels.menu = not start_btn.clicked
        pygame.display.update()
