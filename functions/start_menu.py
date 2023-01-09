import pygame

from buttons.menu_button import MenuButton
from functions.terminate import terminate
from levels import levels


def start_menu(screen):
    while levels.menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not levels.flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        menu_background = pygame.image.load("backgrounds/background.png")
        screen.blit(menu_background, (0, 0))

        start_btn = MenuButton(480, 145, (13, 162, 58), (23, 204, 50), screen)
        start_btn.draw(410, 225, "Начать игру", 120)

        levels.menu = not start_btn.clicked
        pygame.display.update()
