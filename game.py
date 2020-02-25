import pygame
from player import Player
from obstacle import Obstacle

class Game(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player = Player()
        self.all_obstacles = pygame.sprite.Group()
        self.pressed = {
        }
        self.nbOb=0

    def add_obstacle(self):
        obs = Obstacle(self)
        self.all_obstacles.add(obs)
