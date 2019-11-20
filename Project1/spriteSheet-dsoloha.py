# Animated Sprite Sheet
# Dan Soloha
# 11/20/2019

import pygame, os, superwires

def load_sliced_sprites(w, h, filename):
    images = []
    master_image = pygame.image.load(os.path.join('sprites', filename)).convert_alpha()

    master_width, master_height = master_image.get_size()
    for i in range(int(master_height/h)):
        for j in range(int(master_width/w)):
            images.append(master_image.subsurface((j*w, i*h, w, h)))

    return images