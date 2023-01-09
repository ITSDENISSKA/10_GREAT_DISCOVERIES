import pygame

from buttons.question_button import QuestionButton
from functions.terminate import terminate
from levels import levels


def start_question(screen, lvl_number, CLICK_SOUND):
    while levels.question:
        print(1)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not levels.flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
            if event.type == pygame.QUIT:
                terminate()
        menu_background = pygame.image.load(f"backgrounds/question{lvl_number}.png")
        screen.blit(menu_background, (0, 0))

        true_btn = QuestionButton(382, 120, (255, 140, 0), (255, 215, 0), screen, True)
        false1_btn = QuestionButton(360, 120, (255, 140, 0), (255, 215, 0), screen, False)
        false2_btn = QuestionButton(350, 120, (255, 140, 0), (255, 215, 0), screen, False)
        true_btn.draw(455, 268, " Колесницы", 90)
        false1_btn.draw(95, 450, "   Бумагу", 90)
        false2_btn.draw(840, 450, "    Порох", 90)
        if true_btn.clicked:
            levels.question = False
            CLICK_SOUND.play()
            return True

        if false1_btn.clicked:
            levels.question = False
            return False

        if false2_btn.clicked:
            levels.question = False
            return False

        pygame.display.update()
