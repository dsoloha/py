# Astrocrash
# Dan Soloha
# 11/12/2019

from superwires import games

class Ship(games.Sprite):
    """The player's ship"""
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3

    def update(self):
        """Rotate based on keys pressed"""
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

    # create the ship
    the_ship = Ship(image = Ship.image,
                    x = games.screen.width / 2,
                    y = games.screen.height / 2)
    games.screen.add(the_ship)