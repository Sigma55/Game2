import pygame
pygame.init()

# first class Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100  # default
        self.max_health = 100
        self.attack = 10
        self.velocity = 5 # vitesse de deplacement du player
        self.image = pygame.image.load('assets/player.png')


# first step window
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1000,720))

# arriere plan
background = pygame.image.load('assets/bg.jpg')


running = True
#boucle tant que running true
while running:
    # applique le background(arriere plan)
    screen.blit(background, (0, -200))

    #mettre à jour l'ecran update screen
    pygame.display.flip()

    for event in pygame.event.get():
        # si event is quit
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("STOP")







if __name__ == "__main__":
  print("hello")