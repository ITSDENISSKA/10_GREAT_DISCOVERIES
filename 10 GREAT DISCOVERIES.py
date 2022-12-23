import pygame
import sys

from moviepy.editor import VideoFileClip

from levels import levels
from buttons.menu_button import MenuButton
from buttons.question_button import QuestionButton
from sprites.player import Player
from sprites.road import Road
from sprites.block import Block
from sprites.door import Door
from sprites.all_sprites_groups import spritres_groups

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()


def load_level(lvl, lvl_number):
    px, py = 0, 0
    file = open(lvl, "r", encoding="utf-8")
    x = y = 0
    for line in file.readlines():
        for char in line:
            if char == "d":
                Door(f"all_levels/lvl{lvl_number}/door.png", x, y, spritres_groups.doors, spritres_groups.all_sprites)
            if char == "x":
                Block(f"all_levels/lvl{lvl_number}/block.png", x, y, spritres_groups.blocks, spritres_groups.all_sprites)
            if char == ".":
                Road(f"all_levels/lvl{lvl_number}/road.png", x, y, spritres_groups.roads, spritres_groups.all_sprites)
            if char == "@":
                Road(f"all_levels/lvl{lvl_number}/road.png", x, y, spritres_groups.roads, spritres_groups.all_sprites)
                px, py = x, y
            x = x + 40
        x = 0
        y = y + 40
    file.close()
    return px, py


w = 1280
h = 720


screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('10 GREAT DISCOVERIES')
click = pygame.mixer.Sound("sounds/button.wav")
pygame.mixer.music.load("sounds/music.wav")
pygame.mixer.music.play(-1)

clip = VideoFileClip('video/123.mp4')

while levels.menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
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

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while levels.level1:
    px, py = load_level("all_levels/lvl1/level1.txt", 1)

    player = Player("all_levels/lvl1/player.png", px, py, w, h, spritres_groups.all_sprites)

    while levels.level1:
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
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flPause = not levels.flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
        menu_background = pygame.image.load("backgrounds/question1.png")
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
            levels.level2 = True
            click.play()
        if false1_btn.clicked:
            levels.question = False
            levels.level1 = True
            break
        if false2_btn.clicked:
            levels.question = False
            levels.level1 = True
            break

        pygame.display.update()

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
while levels.level2:
    px, py = load_level("all_levels/lvl2/level2.txt", 2)

    player = Player("all_levels/lvl2/player.png", px, py, w, h, spritres_groups.all_sprites)

    while levels.level2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update(pygame.K_w, (1, 0, 0, 0))
                if event.key == pygame.K_s:
                    player.update(pygame.K_s, (0, 1, 0, 0))
                if event.key == pygame.K_a:
                    player.update(pygame.K_a, (0, 0, 1, 0))
                if event.key == pygame.K_d:
                    player.update(pygame.K_d, (0, 0, 0, 1))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        levels.flPause = not levels.flPause
                        if levels.flPause:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
        if pygame.sprite.spritecollideany(player, spritres_groups.doors):
            spritres_groups.all_sprites.remove(spritres_groups.all_sprites)
            spritres_groups.doors.remove(spritres_groups.doors)
            spritres_groups.blocks.remove(spritres_groups.blocks)
            spritres_groups.roads.remove(spritres_groups.roads)
            levels.level2 = False
            levels.question = True
        spritres_groups.all_sprites.draw(screen)
        pygame.display.update()

    # ———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    while levels.question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    levels.flPause = not levels.flPause
                    if levels.flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
        menu_background = pygame.image.load("backgrounds/question2.png")
        screen.blit(menu_background, (0, 0))

        true_btn = QuestionButton(355, 120, (255, 140, 0), (255, 215, 0), screen, True)
        false1_btn = QuestionButton(335, 120, (255, 140, 0), (255, 215, 0), screen, False)
        false2_btn = QuestionButton(350, 120, (255, 140, 0), (255, 215, 0), screen, False)

        true_btn.draw(95, 450, "   Колесо", 90)
        false1_btn.draw(473, 268, " Изолента", 90)
        false2_btn.draw(840, 450, "   Камень", 90)
        levels.question = true_btn.answer
        if true_btn.clicked:
            levels.question = False
            levels.level3 = True
            click.play()
        if false1_btn.clicked:
            levels.question = False
            levels.level2 = True
            break
        if false2_btn.clicked:
            levels.question = False
            levels.level2 = True
            break

        pygame.display.update()


pygame.quit()
