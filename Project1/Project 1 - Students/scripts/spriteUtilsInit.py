import pygame
from pygame import *

import os, math

def load_sliced_sprites(w, h, filename):
    '''
    Specs :
    	Master can be any height.
    	Sprites frames width must be the same width
    	Master width must be len(frames)*frame.width
    Assuming you ressources directory is named "ressources"
    '''
    images = []
##    master_image = pygame.image.load(os.path.join('images', filename)).convert_alpha()
    master_image = pygame.image.load(filename).convert_alpha()

    master_width, master_height = master_image.get_size()

    for j in range(int(master_height/h)):
        for i in range(int(master_width/w)):
            images.append(master_image.subsurface((i*w,j*h,w,h)))
    return images
