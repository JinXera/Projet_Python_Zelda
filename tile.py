import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../Projet_Python_semestre_2/graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
