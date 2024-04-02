import pygame
from settings import *

Class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.imga.load('../graphics/test/rock.png').convert_alfa()
        self.rect = self.image.get_rect(topleft = pos)
