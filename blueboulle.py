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
        x_speed = 0
        y_speed = 0
        if (self.x + 55) < new_x:
            x_speed = speed
            self.x = self.x + x_speed
            self.image = pygame.transform.scale(self.image, (self.image.get_width() - (1 * (10 ** -14.9)), self.image.get_height() * 1))
        elif (self.x + 55) > new_x:
            x_speed = speed
            self.x = self.x - x_speed
        if self.y > new_y:
            y_speed = speed
            self.y = self.y - y_speed
        elif self.y < new_y:
            self.y = self.y + y_speed
        # speed -= 0.9
        # x_speed -= 0.9
        # y_speed -= 0.9
        # self.image_size = self.image.get_size()
        # scale_size = (self.image_size[0] * .9999, self.image_size[1] * .9999)
        # self.image = pygame.transform.scale(self.image, scale_size)
        # self.image_size = self.image.get_size()
        # self.image = pygame.transform.scale(self.image, (self.image.get_width() - (1 * (10 ** -14.9)), self.image.get_height() - (1 * (10 ** -14.9))))
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
