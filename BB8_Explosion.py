# 14.0 BB8 ATTACK GAME   Name:________________

# You will use the starting code below and build the program "BB8 Attack" as you go through Chapter 14.


import random
import arcade

# --- Constants ---
BB8_scale = 0.3
trooper_scale = 0.1
bullet_scale = 1
trooper_count = 40
SPEED = 3
SW = 800
SH = 600
EXPLOSION_TEXTURE_COUNT = 50

class Explosion(arcade.Sprite):
    def __init__(self, texture_list):
        super().__init__("Images/explosions/explosion0000.png")

        self.current_texture = 0
        self.textures = texture_list
        self.explosion_sound = arcade.load_sound("sounds/explosion.wav")

    def update(self):
        self.current_texture += 1

        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.kill()


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/bb8.png", BB8_scale)

        self.laser_sound = arcade.load_sound("sounds/laser.wav")
        self.explosion_sound = arcade.load_sound("sounds/explosion.wav")

    def update(self):
        self.center_x += self.change_x

        if self.right < 0:
            self.left = SW
        if self.left > SW:
            self.right = 0


class Trooper(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/stormtrooper.png", trooper_scale)
        self.w = int(self.width)
        self.h = int(self.height)

    def update(self):
        self.center_y -= 2

        if self.top < 0:
            self.center_x = random.randrange(self.w, SW - self.w)
            self.center_y = random.randrange(SH + self.h, SH * 2)


class Bullet(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/bullet.png", bullet_scale)

    def update(self):
        self.center_y += 10
        if self.bottom > SH:
            self.kill()


class EnemyBullet(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/rbullet.png", bullet_scale)

    def update(self):
        self.center_y -= 10
        self.angle = -90
        if self.top < 0:
            self.kill()


# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(False)

        self.explosion_texture_list = []
        for i in range(EXPLOSION_TEXTURE_COUNT):
            texture_name = f"Images/explosions/explosion{i:04}.png"
            self.explosion_texture_list.append(arcade.load_texture(texture_name))

    def on_draw(self):
        arcade.start_render()
        self.bullets.draw()
        self.trooper_list.draw()
        self.player_list.draw()
        self.explosions.draw()
        self.ebullets.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, SW - 80, SH - 15, arcade.color.WHITE, 14)

        if self.Gameover:
            arcade.draw_rectangle_filled(SW // 2, SH // 2, SW, SH, arcade.color.BLACK)
            arcade.draw_text("Game Over! Press P to Play Again!", SW / 2 - 150, SH / 2, (0, 255, 0), 14)
            arcade.draw_text(output, SW / 2 - 50, SH / 2 - 20, (0, 255, 0), 14)

    def on_update(self, dt):
        self.player_list.update()
        self.trooper_list.update()
        self.bullets.update()
        self.explosions.update()
        self.ebullets.update()

        if len(self.trooper_list) == 0:
            self.Gameover = True

        bb8_hit = arcade.check_for_collision_with_list(self.BB8, self.trooper_list)
        if len(bb8_hit) > 0:
            self.BB8.kill()
            self.Gameover = True

        for bullet in self.bullets:
            hit_list = arcade.check_for_collision_with_list(bullet, self.trooper_list)

            if len(hit_list) > 0:
                explosion = Explosion(self.explosion_texture_list)
                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y
                self.explosions.append(explosion)
                arcade.play_sound(explosion.explosion_sound)
                bullet.kill()

            for trooper in hit_list:
                trooper.kill()
                self.score += 2

        for trooper in self.trooper_list:
            if random.randrange(800) == 0 and self.Gameover is False:
                ebullet = EnemyBullet()
                ebullet.center_x = trooper.center_x
                ebullet.top = trooper.bottom
                self.ebullets.append(ebullet)

        bb8_bombed = arcade.check_for_collision_with_list(self.BB8, self.ebullets)
        if len(bb8_bombed) > 0:
            arcade.play_sound(self.BB8.explosion_sound)
            self.BB8.kill()
            bb8_bombed[0].kill()
            self.Gameover = True

    def reset(self):
        self.Gameover = False

        self.player_list = arcade.SpriteList()
        self.trooper_list = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.explosions = arcade.SpriteList()
        self.ebullets = arcade.SpriteList()

        self.score = 0

        self.BB8 = Player()
        self.BB8.center_x = SW / 2
        self.BB8.bottom = 2
        self.player_list.append(self.BB8)

        for i in range(trooper_count):
            trooper = Trooper()
            trooper.center_x = random.randrange(trooper.w, SW - trooper.w)
            trooper.center_y = random.randrange(300, SH * 2)
            self.trooper_list.append(trooper)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.BB8.change_x = -SPEED
        elif key == arcade.key.RIGHT:
            self.BB8.change_x = SPEED
        elif key == arcade.key.P and self.Gameover is True:
            self.reset()
        elif key == arcade.key.SPACE and self.Gameover is False:
            self.bullet = Bullet()
            self.bullet.center_x = self.BB8.center_x
            self.bullet.bottom = self.BB8.top
            self.bullet.angle = 90
            self.bullets.append(self.bullet)
            arcade.play_sound(self.BB8.laser_sound)
            self.score -= 1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.BB8.change_x = 0


# -----Main Function--------
def main():
    window = MyGame(SW, SH, "BB8 Explosions")
    window.reset()
    arcade.run()


# ------Run Main Function-----
if __name__ == "__main__":
    main()
