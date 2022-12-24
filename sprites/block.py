import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y, blocks, all_sprites):
        super().__init__(blocks, all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y