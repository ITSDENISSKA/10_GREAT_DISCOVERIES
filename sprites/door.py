import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, doors, all_sprites):
        super().__init__(doors, all_sprites)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y