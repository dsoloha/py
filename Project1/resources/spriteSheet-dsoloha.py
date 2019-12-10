# Animated Sprite Sheet
# Dan Soloha
# 11/20/2019

import pygame

BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
BLUE    = (  0,   0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey(BLACK)

        return image


GRASS_LEFT = (576, 720, 70, 70)
GRASS_RIGHT = (576, 576, 70, 70)
GRASS_MIDDLE = (504, 576, 70, 70)
STONE_PLATFORM_LEFT = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT = (792, 648, 70, 40)


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        sprite_sheet = SpriteSheet("tiles_spritesheet.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        self.rect.x += self.change_x

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:




            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:

                self.player.rect.left = self.rect.right

        self.rect.y += self.change_y

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:



            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom


        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1


class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """


        self.platform_list = None
        self.enemy_list = None

        self.background = None

        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """



        screen.fill(BLUE)
        screen.blit(self.background, (self.world_shift // 3, 0))

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x



class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        Level.__init__(self, player)

        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(WHITE)
        self.level_limit = -2500

        level = [[GRASS_LEFT, 500, 500],
                 [GRASS_MIDDLE, 570, 500],
                 [GRASS_RIGHT, 640, 500],
                 [GRASS_LEFT, 800, 400],
                 [GRASS_MIDDLE, 870, 400],
                 [GRASS_RIGHT, 940, 400],
                 [GRASS_LEFT, 1000, 500],
                 [GRASS_MIDDLE, 1070, 500],
                 [GRASS_RIGHT, 1140, 500],
                 [STONE_PLATFORM_LEFT, 1120, 280],
                 [STONE_PLATFORM_MIDDLE, 1190, 280],
                 [STONE_PLATFORM_RIGHT, 1260, 280],
                 ]

        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        block = MovingPlatform(STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        Level.__init__(self, player)

        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(WHITE)
        self.level_limit = -1000

        level = [[STONE_PLATFORM_LEFT, 500, 550],
                 [STONE_PLATFORM_MIDDLE, 570, 550],
                 [STONE_PLATFORM_RIGHT, 640, 550],
                 [GRASS_LEFT, 800, 400],
                 [GRASS_MIDDLE, 870, 400],
                 [GRASS_RIGHT, 940, 400],
                 [GRASS_LEFT, 1000, 500],
                 [GRASS_MIDDLE, 1070, 500],
                 [GRASS_RIGHT, 1140, 500],
                 [STONE_PLATFORM_LEFT, 1120, 280],
                 [STONE_PLATFORM_MIDDLE, 1190, 280],
                 [STONE_PLATFORM_RIGHT, 1260, 280],
                 ]

        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        block = MovingPlatform(STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    def __init__(self):
        """ Constructor function """

        super().__init__()


        self.change_x = 0
        self.change_y = 0


        self.walking_frames_l = []
        self.walking_frames_r = []

        self.direction = "R"

        self.level = None

        sprite_sheet = SpriteSheet("p1_walk.png")

        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)


        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """

        self.calc_grav()

        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:

                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(
            self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0


def main():
    """ Main Program """
    pygame.init()

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    player = Player()

    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))

    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()

        current_level.update()

        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        current_level.draw(screen)
        active_sprite_list.draw(screen)



        clock.tick(60)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
