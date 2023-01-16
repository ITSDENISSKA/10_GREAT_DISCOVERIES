import sys

import pygame

from database import DataBase
from widgets.question_button import QuestionButton
from functions.generate_levels import generate_maze_level, generate_platformer_level
from functions.load_level import load_level
from functions.terminate import terminate
from functions.draw_attempts_count import draw_attempts_count
from helpers import settings
from sprites.all_sprites_groups import spritres_groups


def remove_all_sprites_groups():
    spritres_groups.all_sprites.remove(spritres_groups.all_sprites)
    spritres_groups.doors.remove(spritres_groups.doors)
    spritres_groups.blocks.remove(spritres_groups.blocks)
    spritres_groups.roads.remove(spritres_groups.roads)
    settings.level = False
    settings.question = True


def start_maze_level(screen, lvl_number, timer):
    database = DataBase("database.sqlite")
    database.update_time_by_nickname(settings.players_name, timer.get_time())
    player, px, py = generate_maze_level(load_level(f"data/lvl{lvl_number}/level{lvl_number}.txt"), lvl_number)

    while settings.level:
        if pygame.key.get_pressed()[pygame.K_a]:
            player.update(pygame.K_a, (0, 0, 1, 0))
        if pygame.key.get_pressed()[pygame.K_d]:
            player.update(pygame.K_d, (0, 0, 0, 1))
        if pygame.key.get_pressed()[pygame.K_w]:
            player.update(pygame.K_w, (1, 0, 0, 0))
        if pygame.key.get_pressed()[pygame.K_s]:
            player.update(pygame.K_s, (0, 1, 0, 0))
        player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.close()
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    settings.music_playing = not settings.music_playing
                    if settings.music_playing:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == pygame.K_ESCAPE:
                    database.close()
                    terminate()
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
        if pygame.sprite.spritecollideany(player, spritres_groups.doors):
            remove_all_sprites_groups()

        spritres_groups.all_sprites.draw(screen)

        draw_attempts_count(screen, 0, 40)
        timer.draw(screen, 640, 0, 40)

        pygame.display.update()


def start_platformer_level(screen, lvl_number, timer):
    database = DataBase("database.sqlite")
    database.update_time_by_nickname(settings.players_name, timer.get_time())
    player, px, py, background = generate_platformer_level(load_level(f"data/lvl{lvl_number}/level{lvl_number}.txt"),
                                                           lvl_number)
    while settings.level:
        screen.blit(background, (0, 0))
        if pygame.key.get_pressed()[pygame.K_a]:
            player.update(pygame.K_a)
        if pygame.key.get_pressed()[pygame.K_d]:
            player.update(pygame.K_d)
        player.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                database.close()
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    database.close()
                    terminate()
                if event.key == pygame.K_SPACE:
                    settings.music_playing = not settings.music_playing
                    if settings.music_playing:
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()
        if pygame.sprite.spritecollideany(player, spritres_groups.doors):
            remove_all_sprites_groups()

        spritres_groups.all_sprites.draw(screen)

        draw_attempts_count(screen, 0, 40)
        timer.draw(screen, 640, 0, 40)

        pygame.display.update()
