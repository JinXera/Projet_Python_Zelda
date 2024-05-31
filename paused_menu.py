import pygame
from settings import *

class PauseMenu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.options = ["Continue", "Retry", "Quit"]
        self.current_option = 0
        self.menu_open = False

        # Taille des éléments du menu
        self.menu_width = self.display_surface.get_width() // 3
        self.menu_height = self.display_surface.get_height() // len(self.options)
        self.menu_x = (self.display_surface.get_width() - self.menu_width) // 2
        self.menu_y = (self.display_surface.get_height() - self.menu_height * len(self.options)) // 2

    def display(self):
        if self.menu_open:
            for i, option in enumerate(self.options):
                rect = pygame.Rect(self.menu_x, self.menu_y + i * self.menu_height, self.menu_width, self.menu_height)
                color = TEXT_COLOR_SELECTED if i == self.current_option else TEXT_COLOR
                pygame.draw.rect(self.display_surface, UI_BG_COLOR, rect)
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, rect, 4)
                text_surface = self.font.render(option, True, color)
                text_rect = text_surface.get_rect(center=rect.center)
                self.display_surface.blit(text_surface, text_rect)

    def input(self):
        if self.menu_open:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                self.current_option = (self.current_option - 1) % len(self.options)
                pygame.time.wait(200)  # Debounce
            if keys[pygame.K_d]:
                self.current_option = (self.current_option + 1) % len(self.options)
                pygame.time.wait(200)  # Debounce
            if keys[pygame.K_SPACE]:
                return self.options[self.current_option]
        return None
