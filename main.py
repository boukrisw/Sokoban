import pygame
from game import Game


pygame.init()
pygame.display.set_caption("SOKOBAN")
screen = pygame.display.set_mode((520,360))

#importer les images!
background = pygame.image.load("Ressources/Images/background.png")
background = pygame.transform.scale(background,(520,360))

running = True

#Une partie de jeu
game=Game()

#nombre d'obstacle eviter

while running:
    #arriere plan
    screen.blit(background, (0,0))
    screen.blit(game.player.image,game.player.rect)

    add=True
    #Mouvements des obstacles!
    for o in game.all_obstacles:
        o.move()
        if(o.rect.y < 58):
            add=False
        if o.rect.y < game.player.rect.y and o.rect.y > game.player.rect.y-45 and o.rect.x > game.player.rect.x-45 and o.rect.x < game.player.rect.x+45  :
            #Le jeune homme a touche un Obstacle
            running=False
    #Ajout d'un nouveau obstacle
    if add:
        game.add_obstacle()


    #Dessiner les obstacles
    game.all_obstacles.draw(screen)

    #Gerer les mouvements de joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>0:
        game.player.move_left()

    #mettre a jour
    pygame.display.flip()


    #Gestion des evenments!!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

print("nb Obstacle eviter :")
print(game.nbOb)
