import pygame
from support import import_folder

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            'flame': import_folder('../Projet_Python_Zelda/graphics/particles/flame/frames'),
            'aura': import_folder('../Projet_Python_Zelda/graphics/particles/aura'),
            'heal': import_folder('../Projet_Python_Zelda/graphics/particles/heal/frames'),

            # attacks
            'claws': import_folder('../Projet_Python_Zelda/graphics/particles/claws'),
            'slash': import_folder('../Projet_Python_Zelda/graphics/particles/slash'),
            'sparkle': import_folder('../Projet_Python_Zelda/graphics/particles/sparkle'),
            'leaf_attack': import_folder('../Projet_Python_Zelda/graphics/particles/leaf_attack'),
            'thunder': import_folder('../Projet_Python_Zelda/graphics/particles/thunder'),

            # monster deaths
            'squid': import_folder('../Projet_Python_Zelda/graphics/particles/smoke_orange'),
            'racoon': import_folder('../Projet_Python_Zelda/graphics/particles/raccoon'),
            'spirit': import_folder('../Projet_Python_Zelda/graphics/particles/nova'),
            'bamboo': import_folder('../Projet_Python_Zelda/graphics/particles/bamboo'),

            # leaf
            'leaf': (
                import_folder('../Projet_Python_Zelda/graphics/particles/leaf1'),
                import_folder('../Projet_Python_Zelda/graphics/particles/leaf2'),
                import_folder('../Projet_Python_Zelda/graphics/particles/leaf3'),
                import_folder('../Projet_Python_Zelda/graphics/particles/leaf4'),
                import_folder('../Projet_Python_Zelda/graphics/particles/leaf5'),
                import_folder('../Projet_Python_Zelda/graphics/particles/leaf6'),
                self.reflect_images(import_folder('../Projet_Python_Zelda/graphics/particles/leaf1')),
                self.reflect_images(import_folder('../Projet_Python_Zelda/graphics/particles/leaf2')),
                self.reflect_images(import_folder('../Projet_Python_Zelda/graphics/particles/leaf3')),
                self.reflect_images(import_folder('../Projet_Python_Zelda/graphics/particles/leaf4')),
                self.reflect_images(import_folder('../Projet_Python_Zelda/graphics/particles/leaf5')),
                self.reflect_images(import_folder('../Projet_Python_Zelda/graphics/particles/leaf6'))
            )
        }

    def  reflect_images(self, frames):
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.image.get_rect[self.frame_index]

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frames >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()