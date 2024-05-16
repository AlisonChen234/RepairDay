import pygame


class Vending:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("vending_machine.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
        self.image_size = self.image.get_size()
    #def set_location(self, new_x, new_y):
        #self.x = new_x
        #self.y = new_y
        #self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

