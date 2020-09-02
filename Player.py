import pygame

from Game2.Projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100  # default
        self.max_health = 100
        self.attack = 10
        self.velocity = 40 # vitesse de deplacement du player
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()

    def throw_projectile(self):
        #creer instance de la class projectile
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)


    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
