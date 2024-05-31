import pygame


class Blueboulle:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("blueboulle.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1
        self.size = .2

    def move_direction(self, speed, new_x, new_y):
        if self.x < new_x:
            self.x = self.x + speed
        elif self.x > new_x:
            self.x = self.x - speed
        if self.y > new_y:
            self.y = self.y - speed
        speed -= 0.05
        # self.size -= 0.0001
        # self.image_size = self.image.get_size()
        # scale_size = (self.image_size[0] * self.size, self.image_size[1] * self.size)
        # self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

