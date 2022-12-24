import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, image, x, y, doors, all_sprites):
        super().__init__(doors, all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y