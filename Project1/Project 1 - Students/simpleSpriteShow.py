# Explosion
# Demonstrates creating an animation

import sys, os, math
from livewires import games
from spriteUtils import *

filename = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

games.init(fps = 50)

animation_list = load_2d_sheets(x, y, filename)
          
animation = games.Animation(images = animation_list,\
                            x = games.screen.width/2,\
                            y = games.screen.height/2,\
                            n_repeats = -1,\
                            repeat_interval = 10)
games.screen.add(animation)

games.screen.mainloop()
