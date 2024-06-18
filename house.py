import pygame
from settings import *
from support import *

class Portal:
    def __init__(self, pos):

        # position
        self.rect = self.image.get_rect(topleft=pos)

        # player interaction
        self.transport = False

    def get_player_distance_direction(self, player):
        portal_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - portal_vec).magnitude()

        if distance > 0:
            direction = (player_vec - portal_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def transport(self, player, game):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= 64:
            self.display_proposition() # Display 'Press f key for going to your hidden house'
            if game.event.type == pygame.KEYDOWN:
                if game.event.key == pygame.K_f:
                    self.transport = True
                    self.display_hidden_house()
        else:
            pass