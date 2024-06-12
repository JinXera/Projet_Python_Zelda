import pygame
import sys
from settings import *

class DeathMenu:
    def __init__(self):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.options = ["Retry", "Quit"]
        self.option_nr = len(self.options)
        self.option_names = list(self.options)
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.menu_open = False

        # item creation
        self.height = self.display_surface.get_size()[1] * 0.1
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()

        # selection system
        self.selection_option = 0
        self.selection_option_time = None
        self.can_move = True

        # Taille des éléments du menu
        self.menu_width = self.display_surface.get_width() // 3
        self.menu_height = self.display_surface.get_height() // len(self.options)
        self.menu_x = (self.display_surface.get_width() - self.menu_width) // 2
        self.menu_y = (self.display_surface.get_height() - self.menu_height * len(self.options)) // 2

    def input(self, level, game):
            keys = pygame.key.get_pressed()

            if self.can_move:
                if keys[pygame.K_d] and self.selection_option < self.option_nr - 1:
                    self.selection_option += 1
                    self.can_move = False
                    self.selection_option_time = pygame.time.get_ticks()

                elif keys[pygame.K_q] and self.selection_option >= 1:
                    self.selection_option -= 1
                    self.can_move = False
                    self.selection_option_time = pygame.time.get_ticks()

                if keys[pygame.K_SPACE]:
                    self.can_move = False
                    self.selection_option_time = pygame.time.get_ticks()
                    self.item_list[self.selection_option].trigger(level, game)

    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_option_time >= 300:
                self.can_move = True

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.option_nr)):
            # horizontal position
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.option_nr
            left = (item * increment) + (increment - self.width) // 2

            # vertical position
            top = self.display_surface.get_size()[1] * 0.5

            # create the object
            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)

    def display(self, level, game):
        self.input(level, game)
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):

            # get attributes
            name = self.option_names[index]
            item.display(self.display_surface, self.selection_option, name)

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font

    def display_names(self, surface, name, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR

        # title
        title_surface = self.font.render(name, False, color)
        title_rect = title_surface.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 25))

        # draw
        surface.blit(title_surface, title_rect)

    def trigger(self, level, game):
        death_option = level.death_menu.options[self.index]
        if death_option == "Retry":
            level.death_menu.display(level, game)
            level.game_paused = False
            game.var_running = False

        elif death_option == "Quit":
            pygame.quit()
            sys.exit()

    def display(self, surface, option_num, name):
        if self.index == option_num:
            pygame.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)

        self.display_names(surface, name, self.index == option_num)

