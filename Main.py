import pygame

from Game2.Game import Game
from Game2.Player import Player

pygame.init()

# first class Player



# first step window
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1000,720))

# arriere plan
background = pygame.image.load('assets/bg.jpg')

#call class Game
#player = Player()
game = Game()


running = True
#boucle tant que running true
while running:
    # applique le background(arriere plan)
    screen.blit(background, (0, -200))

    #image of player
    screen.blit(game.player.image, game.player.rect)

    #mettre à jour l'ecran update screen
    pygame.display.flip()

    for event in pygame.event.get():
        # si event is quit
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("STOP")
        # si event touche clavier
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and game.player.rect.x + game.player.rect.width < 1000: #size screen max in right
                print("right")
                game.player.move_right()
            elif event.key == pygame.K_LEFT and game.player.rect.x > 0: #axe abscice
                print("left")
                game.player.move_left()


