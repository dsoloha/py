# Space Invaders
# Dan Soloha
# 11/16/2019

import math, random
from superwires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 60)

class Wrapper(games.Sprite):
    """A sprite that can wrap around the screen"""

    def update(self):
        """Wrap sprite around screen"""
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """Destroy self"""
        self.destroy()

class Collider(Wrapper):
    """A Wrapper that can collide with another object"""

    def update(self):
        """Check for overlapping sprites"""
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """Destroy self and leave behind explosion"""
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()

class Ship(Collider):
    """A ship object"""
    image = games.load_image("ship.bmp")
    sound = games.load_sound("thrust.wav")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    VELOCITY_MAX = 3
    MISSILE_DELAY = 25

    def __init__(self, game, x, y):
        """Initialize ship sprite"""
        super(Ship, self).__init__(image = Ship.image, x = x, y = y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        # if waiting until ship can fire, decrease wait
        if self.missile_wait > 0:
            self.missile_wait -= 1

    def fire(self):
        """Fire missile if possible"""
        new_missile = Missile(self.x, self.y, self.angle)
        games.screen.add(new_missile)
        self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        """Destroy ship and end game"""
        self.game.end()
        super(Ship, self).die()

class Player(Ship):
    """The player's ship"""

    def update(self):
        """ Rotate and thrust based on keys pressed. """
        super(Player, self).update()

        # rotate based on left and right arrow keys
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        # apply thrust based on up arrow key
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()

            # change velocity components based on ship's angle
            angle = self.angle * math.pi / 180  # convert to radians
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        # fire missile if spacebar pressed
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            super(Player, self).fire()

        # cap velocity in each direction
        self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
        self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

class Alien(Ship):
    """An alien ship"""
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total = 0

    def __init__(self, game, x, y):
        """Initialize alien sprite"""
        super(Alien, self).__init__(
            game = game,
            x = x, y = y)

        self.game = game
        Alien.total += 1

        # if all aliens are gone advance to the next level
        if Alien.total == 0:
            self.game.advance()

    def die(self):
        """Destroy alien"""
        super(Alien, self).die
        Alien.total -= 1
        self.game.score.value += int(Alien.POINTS)
        self.game.score.right = games.screen.width - 10

class Missile(Collider):
    """A missile launched by the player's ship"""
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        """Initialize missile sprite"""
        Missile.sound.play()

        # convert to radians
        angle = ship_angle * math.pi / 180

        # calculate missile's starting position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        # calculate missile's velocity components
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # create the missile
        super(Missile, self).__init__(image=Missile.image,
                                      x=x, y=y,
                                      dx=dx, dy=dy)

        self.lifetime = Missile.LIFETIME

    def update(self):
        """Move the missile"""
        super(Missile, self).update()

        # if lifetime is up, destroy the missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

class Explosion(games.Animation):
    """Explosion animation"""
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)
        Explosion.sound.play()

class Game(object):
    """The game itself"""

    def __init__(self):
        """Initialize Game object"""
        # set level
        self.level = 0

        # load sound for level advance
        self.sound = games.load_sound("level.wav")

        # create score
        self.score = games.Text(value=0,
                                size=30,
                                color=color.white,
                                top=5,
                                right=games.screen.width - 10,
                                is_collideable=False)
        games.screen.add(self.score)

        # create player's ship
        self.player = Player(game=self,
                         x=games.screen.width / 2,
                         y=games.screen.height / 2)
        games.screen.add(self.player)

    def play(self):
        """Play the game"""
        # begin theme music
        games.music.load("theme.mid")
        games.music.play(-1)

        # load and set background
        nebula_image = games.load_image("nebula.jpg")
        games.screen.background = nebula_image

        # advance to level 1
        self.advance()

        # start play
        games.screen.mainloop()

    def advance(self):
        """Advance to the next level"""
        self.level += 1

        # amount of space around ship to preserve when creating aliens
        BUFFER = 150

        # create new aliens
        for i in range(self.level):
            # calculate an x and y at least BUFFER distance from ship

            # choose minimum distance along x-axis and y-axis
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            # choose distance along x-axis and y-axis based on minimum distance
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            # calculate location based on distance
            x = self.player.x + x_distance
            y = self.player.y + y_distance

            # wrap around screen if necessary
            x %= games.screen.width
            y %= games.screen.width

            # create the alien
            new_alien = Alien(game = self,
                                    x = x, y = y)
            games.screen.add(new_alien)

            i += 1

        # display level number
        level_message = games.Message(value="Level " + str(self.level),
                                      size=40,
                                      color=color.yellow,
                                      x=games.screen.width / 2,
                                      y=games.screen.width / 10,
                                      lifetime=3 * games.screen.fps,
                                      is_collideable=False)
        games.screen.add(level_message)

        # play new level sound, except at first level
        if self.level > 1:
            self.sound.play()

    def end(self):
        """End the game"""
        # show 'Game Over' for 5 seconds
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)

def main():
    space_invaders = Game()
    space_invaders.play()

main()
