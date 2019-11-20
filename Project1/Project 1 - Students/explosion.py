# Explosion
# Demonstrates creating an animation

import os, math
from livewires import games
from spriteUtils import load_sliced_sprites

games.init(screen_width = 640, screen_height = 480, fps = 50)

nebula_image = games.load_image(os.path.join('images', "nebula.jpg"), transparent = 0)
games.screen.background = nebula_image

##explosion_list = load_sliced_sprites(16, 16, 'explosed-sprite.png')
explosion_list = load_sliced_sprites(64, 64, 'explosed-Big-sprite.png')
          
explosion = games.Animation(images = explosion_list,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            n_repeats = 10,
                            repeat_interval = 10)
games.screen.add(explosion)

games.screen.mainloop()
