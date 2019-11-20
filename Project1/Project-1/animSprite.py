# Project 1
# Demonstrates creating an animation from a sprite sheet

import sys, os, math
from superwires import games
import pygame
from spriteUtils import *

filename = sys.argv[1]
width = int(sys.argv[2])
height = int(sys.argv[3])

games.init(screen_width = 600, screen_height = 424, fps = 50)

streetScene = games.load_image(os.path.join('./images', "flower-market.jpg"), transparent = 0)
games.screen.background = streetScene

anim_list = load_2d_sheets(width, height, filename)
          
anim = games.Animation(images = anim_list,
                            x = games.screen.width/2,
                            y = 4*games.screen.height/5,
                            n_repeats = 30,
                            repeat_interval = 5)

##The following segment will save each frame in the list
##tag = 1
##for img in anim_list:
##    imgname = "Image" + str(tag) + ".jpg"
##    pygame.image.save(img, imgname)
##    tag += 1

games.screen.add(anim)

games.screen.mainloop()
