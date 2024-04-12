import os
import pygame

def import_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = pygame.image.load(filepath).convert_alpha()
            images.append(image)
    return images