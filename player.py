import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        #super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.image = pygame.image.load("Ressources/Images/Pousseur.png")
        self.image = pygame.transform.scale(self.image,(78,78))
        self.rect =self.image.get_rect()
        self.rect.x =250
        self.rect.y =290

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
