import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100  # default
        self.max_health = 100
        self.attack = 10
        self.velocity = 10 # vitesse de deplacement du player
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
