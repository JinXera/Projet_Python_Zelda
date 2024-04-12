import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../Projet_Python_Zelda/graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        #graphics setup
        self.import_player_assets()

        # movement
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        self.obstacle_sprites = obstacle_sprites

    def import_player_assets(self):
        character_path = '../Projet_Python_Zelda/graphics/player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                          'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                          'right_attack':[], 'left_attack':[], 'up_attack':[], 'down_attack':[]}
       # for animation in self.animations.keys():
       #     full_path = character_path + animation*
           # self.animations[animation] = import_folder
    def input(self):
        keys = pygame.key.get_pressed()

        # movement input
        if keys[pygame.K_z]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_q]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # attack input
        if keys[pygame.K_SPACE] and not self.attacking: # à changer avec le clic gauche de la souris
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print('attack')

        # magic input
        if keys[pygame.K_LCTRL] and not self.attacking: # à changer avec le clic droit de la souris
            self.attacking = True
            self.attack_time = pygame.time.get_ticks()
            print('magic')

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        #self.rect.center += self.direction * speed

    def collision(self, direction):
        if direction == 'horizontal' :
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: #moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: #moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical' :
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: #moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: #moving top
                        self.rect.top = sprite.rect.bottom

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def update(self):
        self.input()
        self.cooldowns()
        self.move(self.speed)