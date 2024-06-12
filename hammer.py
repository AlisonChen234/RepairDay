import pygame

class Hammer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("hammer.png")
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.2), int(self.image_size[1] * 0.2))
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.4

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_direction(self, direction):
        if direction == "right":
            self.x += self.delta
        if direction == "left":
            self.x -= self.delta
        if direction == "up":
            self.y -= self.delta
        if direction == "down":
            self.y += self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

