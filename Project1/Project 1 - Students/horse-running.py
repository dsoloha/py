# Explosion
# Demonstrates creating an animation

import sys, os, math
from livewires import games
from spriteUtils import *

filename = sys.argv[1]
x = int(sys.argv[2])
y = int(sys.argv[3])

games.init(screen_width = 1152, screen_height = 864, fps = 50)

nebula_image = games.load_image(os.path.join('images', "race_track.jpg"), transparent = 0)
games.screen.background = nebula_image

anim_list = load_2d_sheets(x, y, filename)
          
anim = games.Animation(images = anim_list,
                            x = games.screen.width/2,
                            y = 2*games.screen.height/4,
                            n_repeats = 10,
                            repeat_interval = 5)
games.screen.add(anim)

games.screen.mainloop()
