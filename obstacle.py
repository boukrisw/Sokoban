import pygame
import random


class Obstacle(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 1
        self.image = pygame.image.load("Ressources/Images/Mur.png")
        self.image = pygame.transform.scale(self.image,(58,58))
        self.rect =self.image.get_rect()
        i=random.randint(0, 562)/58
        self.rect.x =i*58

    def remove(self):
        self.game.all_obstacles.remove(self)

    def move(self):
        self.rect.y +=self.velocity
        if self.rect.y > 520:
            self.remove()
            self.game.nbOb+=1
