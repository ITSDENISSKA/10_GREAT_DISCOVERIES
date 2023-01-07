import pygame

from settings import TILE_WIDTH, TILE_HEIGHT
from sprites.all_sprites_groups import spritres_groups


class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y, all_sprites):
        super().__init__(all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.w = 1280
        self.h = 720
        self.rect.x = x * TILE_WIDTH
        self.rect.y = y * TILE_HEIGHT

    def update(self, *args):
        if args:
            if args[0] == pygame.K_w and self.rect.y > 0:
                self.rect.y -= 40
            if args[0] == pygame.K_s and self.rect.y < self.h - 40:
                self.rect.y += 40
            if args[0] == pygame.K_d and self.rect.x < self.w - 40:
                self.rect.x += 40
            if args[0] == pygame.K_a and self.rect.x > 0:
                self.rect.x -= 40
            if pygame.sprite.spritecollideany(self, spritres_groups.blocks):
                if args[1][0]:
                    self.rect.y += 40
                if args[1][1]:
                    self.rect.y -= 40
                if args[1][2]:
                    self.rect.x += 40
                if args[1][3]:
                    self.rect.x -= 40
