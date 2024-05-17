import pygame
from settings import *

class Menu:
    def __init__(self):
        pass
        # general setup
        self.display.get_surface = pygame.display.get_surface
        self.menu_attribute_nr = 3
        self.menu_attribute_name = list(['Continue', 'Retry', 'Quit'])

        # selection system
        self.menu_open = False
        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

    def input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE] :
            self.menu_open = not self.menu_open

        if key[pygame.K_d] and self.selection_index < self.menu_attribute_nr :
            self.can_move = False
            self.selection_index += 1
            self.selection_time = pygame.time.get_ticks()

        elif key[pygame.K_q] and self.selection_index >= 1 :
            self.can_move = False
            self.selection_index -= 1
            self.selection_time = pygame.time.get_ticks()

        elif key[pygame.K_SPACE] :
            self.can_move = False
            self.selection_time = pygame.time.get_ticks()

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.attribute_nr)):
            # horizontal position
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_nr
            left = (item * increment) + (increment - self.width) // 2

            # vertical position
            top = self.display_surface.get_size()[1] * 0.1

            # create the object
            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)


    def display(self):
        self.input()
        self.selection_cooldown()

        for index, item in enumerate(self.menu_item_list):
            # get menu attributes
            name = self.menu_attribute_name[index]
            item.display(self.display_surface, self.selection_index, name)

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font

    def display_menu_names(self, surface, name, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # title
        title_surface = self.font.render(name, False, color)
        title_rect = title_surface.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0, 20))

        # draw
        surface.blit(title_surface, title_rect)


    def display_bar(self, surface, value, max_value, selected):
        # drawing setup
        top = self.rect.midtop + pygame.math.Vector2(0, 20)
        bottom = self.rect.midbottom - pygame.math.Vector2(0, 20)
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR