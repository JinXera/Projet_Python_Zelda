import pygame
#from support import *
from settings import *

class GameOver:

    def __init__(self):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.over = ["GAME OVER"]
        self.over_name = list(self.over)
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE * 3)

        # item creation
        self.height = self.display_surface.get_size()[1] * 0.17
        self.width = self.display_surface.get_size()[0] // 2.5
        self.create_items()

        # Taille du GAME OVER
        self.menu_width = self.display_surface.get_width() // 3
        self.menu_height = self.display_surface.get_height() // len(self.over)
        self.menu_x = (self.display_surface.get_width() - self.menu_width) // 2
        self.menu_y = (self.display_surface.get_height() - self.menu_height * len(self.over)) // 2

    def create_items(self):
        self.item_list = []

        for item in [0]:
            # horizontal position
            full_width = self.display_surface.get_size()[0]
            increment = full_width
            left = (item * increment) + (increment - self.width) // 2

            # vertical position
            top = self.display_surface.get_size()[1] * 0.1

            # create the object
            item = Item(left, top, self.width, self.height, self.font)
            self.item_list.append(item)

    def display(self):

        # get attributes
        name = self.over_name[0]
        for item in self.item_list:
            item.display(self.display_surface, name)

class Item:
    def __init__(self, l, t, w, h, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.font = font

    def display_names(self, surface, name):
        color = GAME_OVER_TEXT_COLOR

        # title
        title_surface = self.font.render(name, False, color)
        title_rect = title_surface.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 25))

        # draw
        surface.blit(title_surface, title_rect)

    def display(self, surface, name):

        pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
        pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.display_names(surface, name)