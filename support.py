import os
import pygame

def import_folder(folder_path):
    images = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = pygame.image.load(file_path).convert_alpha()
            images.append(image)
    return images