import pygame


class RedArrow:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("redarrow.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .3, self.image_size[1] * .3)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1

    def change_direction(self, direction):
        if direction == "left":
            self.image = pygame.transform.rotate(self.image, 91)

