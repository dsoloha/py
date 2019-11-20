# Explosion
# Demonstrates creating an animation

import sys, os, math
from livewires import games
from spriteUtils import *

filename = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

##print(filename, "\t", x, "\t", y)

games.init(screen_width = 1024, screen_height = 768, fps = 50)

nebula_image = games.load_image(os.path.join('assets', "BG_1.png"), transparent = 0)
games.screen.background = nebula_image

anim_list = load_2d_sheets(x, y, filename)
          
anim = games.Animation(images = anim_list,
                            x = games.screen.width/2,
                            y = 3*games.screen.height/4,
                            n_repeats = -1,
                            repeat_interval = 10)
games.screen.add(anim)

games.screen.mainloop()
