import sys

import pygame

from buttons.question_button import QuestionButton
from functions.generate_levels import generate_level
from functions.load_level import load_level
from functions.terminate import terminate
from levels import levels
from sprites.all_sprites_groups import spritres_groups


def start_level(screen, lvl_number):
    player, px, py = generate_level(load_level(f"data/lvl{lvl_number}/level{lvl_number}.txt"), lvl_number)

    while levels.level:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
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
            levels.level = False
            levels.question = True
        spritres_groups.all_sprites.draw(screen)
        pygame.display.update()
