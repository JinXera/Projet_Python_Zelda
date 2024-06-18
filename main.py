import pygame
import sys
from settings import *
from level import Level




class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        self.var_running = True

        # sound
        main_sound = pygame.mixer.Sound('./audio/main.ogg')
        main_sound.set_volume(0.4)
        main_sound.play(loops = -1)
        self.main_sound = main_sound


    def run(self, game):
                while game.var_running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_m:
                                if self.level.open_pause_menu:
                                    pass
                                else:
                                    self.level.open_upgrade_menu = True
                                    self.level.toggle_menu()
                            elif event.key == pygame.K_ESCAPE:
                                if self.level.open_upgrade_menu:
                                    pass
                                else:
                                    self.level.open_pause_menu = True
                                    self.level.toggle_game_menu()
                                    self.level.open_upgrade_menu = False
                        if game.var_running == False:
                            pygame.quit()
                    self.level.run(game)
                    pygame.display.update()
                    self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    while True:
        game.run(game)
        game.main_sound.stop()
        game.__init__()
        game.var_running = True