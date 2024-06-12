import pygame

class Wave:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("wave.png")
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.5), int(self.image_size[1] * 0.8))
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2

    def update_rect(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.update_rect()

    def move(self):
        self.x -= 2
        self.update_rect()

