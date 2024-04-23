import os
import pygame
from csv import reader
from os import walk

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
             terrain_map.append(list(row))
        return terrain_map


#print(import_csv_layout('../Projet_Python_Zelda/map/map_FloorBlocks.csv'))

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

#    images = []
#    for file_name in os.listdir(folder_path):
#        file_path = os.path.join(folder_path, file_name)
#        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
#            image = pygame.image.load(file_path).convert_alpha()
#            images.append(image)
#    return images

#print(import_folder('../Projet_Python_Zelda/graphics/Grass'))