# 14.0 BB8 ATTACK GAME   Name:________________
 
#You will use the starting code below and build the program "BB8 Attack" as you go through Chapter 14.


import random
import arcade

# --- Constants ---
BB8_scale = 0.3
trooper_scale = 0.1
trooper_count = 5
SPEED = 3
SW = 800
SH = 600


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/bb8.png", BB8_scale)
        self.laser_sound = arcade.load_sound("sounds/laser.wav")

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.top >= SH:
            self.center_y -= self.change_y
        if self.bottom <= 0:
            self.center_y -= self.change_y
        if self.right >= SW:
            self.center_x -= self.change_x
        if self.left <= 0:
            self.center_x -= self.change_x


class Trooper(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/stormtrooper.png", trooper_scale)
        self.w = int(self.width)
        self.h = int(self.height)

    def update(self):
        pass


# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self,SW,SH,title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        self.trooper_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

    def on_update(self, dt):
        self.BB8.update()
        self.player_list.update()
        self.trooper_list.update()

        trooper_hit_list = arcade.check_for_collision_with_list(self.BB8, self.trooper_list)
        for trooper in trooper_hit_list:
            trooper.kill()
            self.score += 1
            arcade.play_sound(self.BB8.laser_sound)

        if self.score == trooper_count:
            self.reset()

    def reset(self):
        self.player_list = arcade.SpriteList()
        self.trooper_list = arcade.SpriteList()

        self.score = 0

        self.BB8 = Player()
        self.BB8.center_x = SW/2
        self.BB8.center_y = SH/2
        self.player_list.append(self.BB8)

        for i in range(trooper_count):
            trooper = Trooper()
            trooper.center_x = random.randrange(trooper.w, SW - trooper.w)
            trooper.center_y = random.randrange(trooper.h, SH - trooper.h)
            self.trooper_list.append(trooper)

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.BB8.center_x = x
    #     self.BB8.center_y = y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.BB8.change_x = -SPEED
        elif key == arcade.key.RIGHT:
            self.BB8.change_x = SPEED
        elif key == arcade.key.UP:
            self.BB8.change_y = SPEED
        elif key == arcade.key.DOWN:
            self.BB8.change_y = -SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.BB8.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.BB8.change_y = 0


#-----Main Function--------
def main():
    window = MyGame(SW,SH,"BB8 Attack")
    window.reset()
    arcade.run()

#------Run Main Function-----
if __name__ == "__main__":
    main()
