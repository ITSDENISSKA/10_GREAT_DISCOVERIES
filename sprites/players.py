import pygame

from helpers.settings import *
from sprites.all_sprites_groups import spritres_groups


class PlayerForMaze(pygame.sprite.Sprite):
    def __init__(self, image, x, y, all_sprites):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_WIDTH
        self.rect.y = y * TILE_HEIGHT

    def update(self, *args):
        if args:
            if args[0] == pygame.K_w and self.rect.y > 0:
                self.rect.y -= 5
            if args[0] == pygame.K_s and self.rect.y < HEIGHT - 40:
                self.rect.y += 5
            if args[0] == pygame.K_d and self.rect.x < WIDTH - 40:
                self.rect.x += 5
            if args[0] == pygame.K_a and self.rect.x > 0:
                self.rect.x -= 5
            if pygame.sprite.spritecollideany(self, spritres_groups.blocks):
                if args[1][0]:
                    self.rect.y += 5
                if args[1][1]:
                    self.rect.y -= 5
                if args[1][2]:
                    self.rect.x += 5
                if args[1][3]:
                    self.rect.x -= 5


class PlayerForPlatformer(pygame.sprite.Sprite):
    def __init__(self, image, x, y, all_sprites):
        super().__init__(all_sprites)
        self.right = True
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_WIDTH
        self.rect.y = y * TILE_HEIGHT
        self.change_x = 0
        self.change_y = 0

    def update(self, *args):
        if args:
            if args[0] == pygame.K_w and self.rect.y > 0:
                self.jump()
            if args[0] == pygame.K_d and self.rect.x < WIDTH - 40:
                self.go_right()
            if args[0] == pygame.K_a and self.rect.x > 0:
                self.go_left()
        self.calculate_gravitation()
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, spritres_groups.blocks, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, spritres_groups.blocks, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0

    def calculate_gravitation(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .025
        if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, spritres_groups.blocks, False)
        self.rect.y -= 10
        if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
            self.change_y = -2

    def go_left(self):
        self.change_x = -1
        if self.right:
            self.flip()
            self.right = False

    def go_right(self):
        self.change_x = 1
        if not self.right:
            self.flip()
            self.right = True

    def stop(self):
        self.change_x = 0

    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
