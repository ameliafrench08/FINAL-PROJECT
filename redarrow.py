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


    def move(self, new_x, new_y):
        change_x = True
        change_y = True
        if self.x == new_x:
            change_x = False
        if self.x != new_x and change_x:
            self.x += self.delta
        if self.y == new_y:
            change_y = False
        if self.y != new_y and change_y:
            self.y -= self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
