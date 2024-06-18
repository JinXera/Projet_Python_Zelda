import pygame
import time
from random import choice, randint
from particle import AnimationPlayer
from support import *
from settings import *
from tile import Tile
from player import Player
from debug import debug
from weapon import Weapon
from ui import UI
from enemy import Enemy
from magic import MagicPlayer
from upgrade import Upgrade
from menu import Menu
from paused_menu import PauseMenu
from death_menu import DeathMenu
from game_over import GameOver

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

        # user interface
        self.ui = UI()
        self.upgrade = Upgrade(self.player)
        #self.paused_menu = PauseMenu(self)
        #self.menu = Menu(self.player)

        # particles
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

        self.death_sound = pygame.mixer.Sound('../Projet_Python_Zelda/audio/death.wav')
        self.death_sound.set_volume(0.2)
        self.player_death_sound = pygame.mixer.Sound('../Projet_Python_Zelda/audio/game_over.wav')
        self.player_death_sound.set_volume(0.4)

        # upgrade menu
        self.upgrade_menu = False
        self.open_upgrade_menu = False

        # paused menu
        # self.game_menu = False
        self.paused_menu = PauseMenu()
        self.open_pause_menu = False

        # death menu
        self.death_menu = DeathMenu()
        self.game_over = False

        # game over
        self.game_over_info = GameOver()

    def create_map(self):
        layout = {
            'boundary': import_csv_layout('../Projet_Python_Zelda/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('../Projet_Python_Zelda/map/map_Grass.csv'),
            'object': import_csv_layout('../Projet_Python_Zelda/map/map_Objects.csv'),
            'entities': import_csv_layout('../Projet_Python_Zelda/map/map_Entities.csv'),
        }

        graphics = {
            'grass': import_folder('../Projet_Python_Zelda/graphics/Grass'),
            'objects': import_folder('../Projet_Python_Zelda/graphics/objects')
        }

        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            # create a grass tile
                            random_grass_image = choice(graphics['grass'])
                            Tile(
                                (x, y),
                                [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites],
                                'grass',
                                random_grass_image)

                        if style == 'object':
                            # create an object tile
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)

                        if style == 'entities':
                            if col == '394':
                                self.player = Player(
                                    (2000, 1430),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic)
                            else:
                                if col == '390': monster_name = 'bamboo'
                                elif col == '391': monster_name = 'spirit'
                                elif col == '392': monster_name = 'raccoon'
                                else: monster_name = 'squid'
                                Enemy(
                                    monster_name,
                                    (x, y),
                                    [self.visible_sprites, self.attackable_sprites],
                                    self.obstacle_sprites,
                                    self.damage_player,
                                    self.trigger_death_particles,
                                    self.add_exp)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def create_magic(self, style, strength, cost):
        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])

        if style == 'flame':
            self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0, 60)
                            for leaf in range(randint(3, 6)):
                                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def damage_player(self, amount, attack_type, game):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])
            if self.player.health <= 0:
                self.player.death_sound.play()
                self.player.kill()
                self.game_over = True
                self.game_paused = True

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, [self.visible_sprites])

    def add_exp(self, amount):
        self.player.exp += amount

    def toggle_menu(self):
        if self.open_upgrade_menu & self.game_over == False:
            self.upgrade_menu = not self.upgrade_menu
            self.game_paused = not self.game_paused

    def toggle_game_menu(self):
        if self.open_pause_menu & self.game_over == False:
            # self.game_menu = not self.game_menu
            self.game_paused = not self.game_paused
            self.pause_menu = not self.pause_menu

    def run(self, game):
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)

        if self.game_paused:
            if self.upgrade_menu:
                self.upgrade.display()
                # display upgrade menu

            elif self.pause_menu:
                self.paused_menu.display(self, game)
                # display pause menu

            elif self.game_over:
                self.game_over_info.display()
                self.death_menu.display(self, game)
                #display death menu

        else:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player, game)
            self.player_attack_logic()
            self.upgrade_menu = False
            self.pause_menu = False
            self.open_upgrade_menu = False
            self.open_pause_menu = False
            self.open_pause_menu = False

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('../Projet_Python_Zelda/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player, game):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player, game)

