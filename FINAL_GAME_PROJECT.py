'''
FINAL GAME PROJECT
------------------
Here you will start the beginning of a game that you will be able to update as we
learn more in upcoming chapters. Below are some ideas that you could include:

1.) Find some new sprite images.
2.) Move the player sprite with arrow keys rather than the mouse. Don't let it move off the screen.
3.) Move the other sprites in some way like moving down the screen and then re-spawning above the window.
4.) Use sounds when a sprite is killed or the player hits the sidewall.
5.) See if you can reset the game after 30 seconds. Remember the on_update() method runs every 1/60th of a second.
6.) Try some other creative ideas to make your game awesome. Perhaps collecting good sprites while avoiding bad sprites.
7.) Keep score and use multiple levels. How do you keep track of an all time high score?
8.) Make a two player game.

'''

import random
import arcade
import math

# --- Constants ---
SW = 800
SH = 600
player_scale = .5
MOVEMENT_SPEED = 5
ANGLE_SPEED = 5
BULLET_SPEED = 10
E_BULLET_SPEED = 5
BULLET_PTS = -1
ENEMY_PTS = 5


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("Space/PNG/playerShip1_blue.png", player_scale)
        self.speed = 0
        self.change_angle = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        self.angle += self.change_angle
        angle_rad = math.radians(self.angle)

        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

        if self.left < 0:
            self.left = 0
        if self.right > SW:
            self.right = SW
        if self.top > SH:
            self.top = SH
        if self.bottom < 0:
            self.bottom = 0


# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self,SW,SH,title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_update(self, dt):
        self.player_list.update()

    def setup(self):
        self.player_list = arcade.SpriteList()

        self.ship = Player()
        self.ship.center_x = SW/2
        self.ship.center_y = SH/2
        self.player_list.append(self.ship)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ship.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ship.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ship.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ship.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.ship.change_angle = ANGLE_SPEED
        elif key == arcade.key.F:
            self.ship.change_angle = -ANGLE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.ship.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ship.change_y = 0
        elif key == arcade.key.D or key == arcade.key.F:
            self.ship.change_angle = 0


#-----Main Function--------
def main():
    window = MyGame(SW,SH,"My Game")
    window.setup()
    arcade.run()

#------Run Main Function-----
if __name__ == "__main__":
    main()
