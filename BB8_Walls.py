# 14.0 BB8 ATTACK GAME   Name:________________

# You will use the starting code below and build the program "BB8 Attack" as you go through Chapter 14.


import random
import arcade
import math

# --- Constants ---
BB8_scale = 0.3
trooper_scale = 0.1
bullet_scale = 1
wall_scale = .5
SPEED = 5
ANGLE_SPEED = 7
BULLET_SPEED = 10
E_BULLET_SPEED = 5
SW = 800
SH = 600
EXPLOSION_TEXTURE_COUNT = 50
trooper_c = [0, 1, 2, 3, 0]

INSTRUCTIONS = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
GAME_OVER = 4

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

        self.speed = 0
        self.change_angle = 0

    def update(self):
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


class Trooper(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/stormtrooper.png", trooper_scale)
        self.w = int(self.width)
        self.h = int(self.height)
        self.dx = random.randrange(-1, 2, 2)
        self.dy = random.randrange(-1, 2, 2)

    def update(self):
        self.center_y += self.dy
        self.center_x += self.dx
        if self.bottom < 0 or self.top > SH:
            self.dy *= -1
        elif self.left < 0 or self.right > SW:
            self.dx *= -1


class Bullet(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/bullet.png", bullet_scale)
        self.speed = 0
    def update(self):
        angle_shoot = math.radians(self.angle - 90)
        self.center_x += -self.speed * math.sin(angle_shoot)
        self.center_y += self.speed * math.cos(angle_shoot)
        if self.bottom > SH or self.top < 0 or self.right < 0 or self.left > SW:
            self.kill()


class EnemyBullet(arcade.Sprite):
    def __init__(self):
        super().__init__("Images/rbullet.png", bullet_scale)
        self.angle_list = [0, 90, 180, 270]
        self.angle = random.choice(self.angle_list)
    def update(self):
        if self.angle == 0:
            self.center_x += E_BULLET_SPEED
        elif self.angle == 90:
            self.center_y += E_BULLET_SPEED
        elif self.angle == 180:
            self.center_x -= E_BULLET_SPEED
        else:
            self.center_y -= E_BULLET_SPEED

        if self.bottom > SH or self.top < 0 or self.right < 0 or self.left > SW:
            self.kill()


# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)

        self.current_state = 0
        self.game_running = False

        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(False)

        self.explosion_texture_list = []
        for i in range(EXPLOSION_TEXTURE_COUNT):
            texture_name = f"Images/explosions/explosion{i:04}.png"
            self.explosion_texture_list.append(arcade.load_texture(texture_name))

    def on_draw(self):
        arcade.start_render()
        if self.current_state == 0:
            arcade.draw_rectangle_filled(SW // 2, SH // 2, SW, SH, arcade.color.BLACK)
            arcade.draw_text("Use arrow keys to move BB8 and SPACE to fire. Press P to play!"
                             , SW / 2 - 250, SH / 2, (0, 255, 0), 14)
        elif self.game_running is True:
            arcade.draw_texture_rectangle(SW // 2, SH // 2, SW, SH, self.background)

            self.bullets.draw()
            self.trooper_list.draw()
            self.player_list.draw()
            self.explosions.draw()
            self.ebullets.draw()
            self.walls.draw()

            arcade.draw_lrtb_rectangle_filled(SW - 95, SW, SH, SH - 35, arcade.color.WHITE)
            output = f"Level: {self.current_state}"
            arcade.draw_text(output, SW - 90, SH - 15, arcade.color.BLACK, 14)
            output = f"Score: {self.score}"
            arcade.draw_text(output, SW - 90, SH - 30, arcade.color.BLACK, 14)

        else:
            output = f"Score: {self.score}"
            arcade.draw_rectangle_filled(SW // 2, SH // 2, SW, SH, arcade.color.BLACK)
            arcade.draw_text("Game Over! Press P to play again!", SW / 2 - 140, SH / 2, (0, 255, 0), 14)
            arcade.draw_text("Choose I for instructions", SW / 2 - 90, SH / 2 - 20, (0, 255, 0), 14)
            arcade.draw_text(output, SW / 2 - 35, SH / 2 - 40, (0, 255, 0), 14)

    def on_update(self, dt):
        if 0 < self.current_state < 4:
            self.game_running = True
        else:
            self.game_running = False

        if self.game_running is True:

            self.player_list.update()
            self.trooper_list.update()
            self.bullets.update()
            self.explosions.update()
            self.ebullets.update()

            if len(self.trooper_list) == 0:
                self.current_state += 1
                self.setup()

            bb8_hit = arcade.check_for_collision_with_list(self.BB8, self.trooper_list)
            if len(bb8_hit) > 0:
                self.BB8.kill()
                self.current_state = 4

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
                    self.score += 4

                bullet_hit_wall = arcade.check_for_collision_with_list(bullet, self.walls)
                if len(bullet_hit_wall) > 0 :
                    self.bullet.kill()

            for trooper in self.trooper_list:
                if random.randrange(800) == 0:
                    ebullet = EnemyBullet()
                    ebullet.center_x = trooper.center_x
                    ebullet.center_y = trooper.center_y
                    self.ebullets.append(ebullet)

                trooper_hit_wall = arcade.check_for_collision_with_list(trooper, self.walls)
                if len(trooper_hit_wall) > 0:
                    if trooper.center_x < trooper_hit_wall[0].left or trooper.center_x > trooper_hit_wall[0].right:
                        trooper.dx *= -1
                    elif trooper.center_y < trooper_hit_wall[0].bottom or trooper.center_y > trooper_hit_wall[0].top:
                        trooper.dy *= -1

                    trooper_hit_wall.clear()

            bb8_bombed = arcade.check_for_collision_with_list(self.BB8, self.ebullets)
            if len(bb8_bombed) > 0:
                arcade.play_sound(self.BB8.explosion_sound)
                self.BB8.kill()
                bb8_bombed[0].kill()
                self.current_state = 4

            bb8_hit_wall = arcade.check_for_collision_with_list(self.BB8, self.walls)
            if len(bb8_hit_wall) > 0:
                self.BB8.speed *= -1
                bb8_hit_wall.clear()


            for ebullet in self.ebullets:
                ebullet_hit_wall = arcade.check_for_collision_with_list(ebullet, self.walls)
                if len(ebullet_hit_wall) > 0:
                    ebullet.kill()

    def setup(self):

        if self.current_state == 1:
            arcade.set_background_color(arcade.color.SKY_BLUE)
            self.background = arcade.load_texture("Images/sky1.png")
        elif self.current_state == 2:
            arcade.set_background_color(arcade.color.WHITE_SMOKE)
            self.background = arcade.load_texture("Images/sky2.png")
        elif self.current_state == 3:
            arcade.set_background_color(arcade.color.ROSE_RED)
            self.background = arcade.load_texture("Images/sky3.png")

        self.player_list = arcade.SpriteList()
        self.trooper_list = arcade.SpriteList()
        self.bullets = arcade.SpriteList()
        self.explosions = arcade.SpriteList()
        self.ebullets = arcade.SpriteList()
        self.walls = arcade.SpriteList()


        self.BB8 = Player()
        self.BB8.center_x = SW / 2
        self.BB8.bottom = 2
        self.player_list.append(self.BB8)

        for i in range(1, trooper_c[self.current_state] + 1):
            trooper = Trooper()
            if i % 2 == 0:
                trooper.center_x = random.randrange(trooper.w, int(SW/4))
                trooper.center_y = random.randrange(trooper.h, SH - trooper.h)
            else:
                trooper.center_x = random.randrange(int(SW * 3/4), SW - trooper.w)
                trooper.center_y = random.randrange(trooper.h, SH - trooper.h)
            self.trooper_list.append(trooper)

        for y in range(5):
            wall = arcade.Sprite("Images/wall.png", wall_scale)
            wall.center_x = int(SW / 3)
            wall.center_y = int(SH / 4) + y * wall.width
            self.walls.append(wall)

        coordinate_list = [[469, 278],
                           [533, 278],
                           [533, 214],
                           [469, 214]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("Images/wall.png", wall_scale)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.walls.append(wall)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT and self.game_running:
            self.BB8.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT and self.game_running:
            self.BB8.change_angle = -ANGLE_SPEED
        elif key == arcade.key.UP and self.game_running:
            self.BB8.speed = SPEED
        elif key == arcade.key.DOWN and self.game_running:
            self.BB8.speed = -SPEED
        elif key == arcade.key.P and not self.game_running:
            self.score = 0
            self.current_state = 1
            self.setup()
        elif key == arcade.key.I and not self.game_running:
            self.current_state = 0
            self.setup()
        elif key == arcade.key.SPACE and self.game_running:
            self.bullet = Bullet()
            self.bullet.center_x = self.BB8.center_x
            self.bullet.center_y = self.BB8.center_y
            self.bullet.angle = self.BB8.angle + 90
            self.bullet.speed = BULLET_SPEED
            self.bullets.append(self.bullet)
            arcade.play_sound(self.BB8.laser_sound)
            self.score -= 1

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT and self.game_running:
            self.BB8.change_angle = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN and self.game_running:
            self.BB8.speed = 0


# -----Main Function--------
def main():
    window = MyGame(SW, SH, "BB8 Walls")
    arcade.run()


# ------Run Main Function-----
if __name__ == "__main__":
    main()
