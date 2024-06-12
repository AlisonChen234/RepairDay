import pygame

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("goomba_sprite.png")
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.5), int(self.image_size[1] * 0.5))
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.4
        self.hammer = None

    def set_hammer(self, hammer):
        self.hammer = hammer
        self.update_hammer_position()

    def update_hammer_position(self):
        if self.hammer:
            # Position the hammer relative to the character
            self.hammer.x = self.x + self.image_size[0] +10 # Adjust as necessary
            self.hammer.y = self.y + self.image_size[1] // 2

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.update_hammer_position()

    def move_direction(self, direction):
        if direction == "right":
            self.x += self.delta*10
        if direction == "left":
            self.x -= self.delta*10
        if direction == "up":
            self.y -= self.delta*10
        if direction == "down":
            self.y += self.delta*10
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.update_hammer_position()

