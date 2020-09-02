import pygame

#class of projectile
class Projectile(pygame.sprite.Sprite):

    def __init__(self,player):
        super().__init__()
        self.player = player
        self.velocity = 1
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(60,60)) # transfrom size of image
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120 # position of projectile
        self.rect.y = player.rect.y + 90 # position of projectile

        # for rotate
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # déplace le projectile en rotation
        self.angle +=50
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle,1)
        # rotate in center of rect
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        if self.rect.x > 1000: #delete si le projectile sort de l'ecran ici(largeur de l'ecran = 1000)
            self.player.all_projectiles.remove(self)

    def move_left(self):
        self.rect.x -= self.velocity
        self.rotate()
        if self.rect.x > 1000: #delete si le projectile sort de l'ecran ici(largeur de l'ecran = 1000)
            self.player.all_projectiles.remove(self)







