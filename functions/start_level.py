import sys

import pygame

from buttons.question_button import QuestionButton
from functions.generate_levels import generate_level
from functions.load_level import load_level
from functions.terminate import terminate
from levels import levels
from sprites.all_sprites_groups import spritres_groups


def start_level(screen, click):
    player, px, py = generate_level(load_level(f"data/lvl{levels.lvl_number}/level{levels.lvl_number}.txt"), 1)

    while levels.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    levels.flPause = not levels.flPause
                    if levels.flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
        if pygame.sprite.spritecollideany(player, spritres_groups.doors):
            spritres_groups.all_sprites.remove(spritres_groups.all_sprites)
            spritres_groups.doors.remove(spritres_groups.doors)
            spritres_groups.blocks.remove(spritres_groups.blocks)
            spritres_groups.roads.remove(spritres_groups.roads)
            levels.level1 = False
            levels.question = True
        spritres_groups.all_sprites.draw(screen)
        pygame.display.update()

        # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
        while levels.question:
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
            menu_background = pygame.image.load(f"backgrounds/question{levels.lvl_number}.png")
            screen.blit(menu_background, (0, 0))

            true_btn = QuestionButton(382, 120, (255, 140, 0), (255, 215, 0), screen, True)
            false1_btn = QuestionButton(360, 120, (255, 140, 0), (255, 215, 0), screen, False)
            false2_btn = QuestionButton(350, 120, (255, 140, 0), (255, 215, 0), screen, False)
            true_btn.draw(455, 268, " Колесницы", 90)
            false1_btn.draw(95, 450, "   Бумагу", 90)
            false2_btn.draw(840, 450, "    Порох", 90)
            question = true_btn.answer
            if true_btn.clicked:
                levels.question = False
                levels.lvl_number += 1
                click.play()
                levels.running = False
            if false1_btn.clicked:
                levels.question = False
                levels.level1 = True
                break
            if false2_btn.clicked:
                levels.question = False
                levels.level1 = True
                break

            pygame.display.update()
