import pygame

from settings import TILE_WIDTH, TILE_HEIGHT


class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y, blocks, all_sprites):
        super().__init__(blocks, all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_WIDTH
        self.rect.y = y * TILE_HEIGHT
