import pygame


class ScaleLine:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("scalerline.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .06, self.image_size[1] * .04)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .8

    def move_direction(self, direction):
        if direction == "down":
            self.y = self.y + self.delta
        if direction == "up":
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

