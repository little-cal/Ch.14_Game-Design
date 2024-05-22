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
bullet_scale = 1
asteroid_scale = 1
MOVEMENT_SPEED = 5
ANGLE_SPEED = 4
BULLET_SPEED = 10
E_BULLET_SPEED = 5
BULLET_PTS = 1
ENEMY_PTS = 3
EXPLOSION_TEXTURE_COUNT = 50
asteroid_c = [0, 2, 3, 5, 0]

big_choice = ["Space/PNG/Meteors/meteorBrown_big1.png", "Space/PNG/Meteors/meteorBrown_big2.png",
              "Space/PNG/Meteors/meteorBrown_big3.png", "Space/PNG/Meteors/meteorBrown_big4.png"]
med_choice = ["Space/PNG/Meteors/meteorBrown_med1.png", "Space/PNG/Meteors/meteorBrown_med2.png"]
small_choice = ["Space/PNG/Meteors/meteorBrown_small1.png", "Space/PNG/Meteors/meteorBrown_small2.png"]
tiny_choice = ["Space/PNG/Meteors/meteorBrown_tiny1.png", "Space/PNG/Meteors/meteorBrown_tiny2.png"]


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("Space/PNG/playerShip1_blue.png", player_scale, hit_box_algorithm="Detailed")
        self.laser1 = arcade.load_sound("Space/Bonus/sfx_laser1.wav")
        self.laser2 = arcade.load_sound("Space/Bonus/sfx_laser2.wav")
        self.speed = 0
        self.change_angle = 0

    def update(self):

        self.angle += self.change_angle
        angle_rad = math.radians(self.angle)

        self.center_x += -self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)

        if self.angle >= 360:
            self.angle -= 360
        elif self.angle <= -360:
            self.angle += 360

        if self.left < 0:
            self.left = 0
        if self.right > SW:
            self.right = SW
        if self.top > SH:
            self.top = SH
        if self.bottom < 0:
            self.bottom = 0


class Bullet(arcade.Sprite):
    def __init__(self):
        super().__init__("Space/PNG/Lasers/laserBlue01.png", bullet_scale)
        self.speed = 0

    def update(self):
        angle_shoot = math.radians(self.angle)
        self.center_x += -self.speed * math.sin(angle_shoot)
        self.center_y += self.speed * math.cos(angle_shoot)
        if self.bottom > SH or self.top < 0 or self.right < 0 or self.left > SW:
            self.kill()


class Asteroid1(arcade.Sprite):
    def __init__(self):
        super().__init__(random.choice(big_choice), asteroid_scale, hit_box_algorithm="Detailed")
        self.w = int(self.width)
        self.h = int(self.height)
        self.dx = random.randrange(-1, 2, 2)
        self.dy = random.randrange(-1, 2, 2)
        self.num = 0

    def update(self):
        self.center_y += self.dy
        self.center_x += self.dx
        if self.bottom < 2:
            self.bottom = 2
            self.dy *= -1
        if self.top > SH - 2:
            self.top = SH - 2
            self.dy *= -1
        if self.left < 2:
            self.left = 2
            self.dx *= -1
        if self.right > SW - 2:
            self.right = SW - 2
            self.dx *= -1


class Asteroid2(arcade.Sprite):
    def __init__(self):
        super().__init__(random.choice(med_choice), asteroid_scale, hit_box_algorithm="Detailed")
        self.w = int(self.width)
        self.h = int(self.height)
        self.dx = random.randrange(-1, 2, 2)
        self.dy = random.randrange(-1, 2, 2)
        self.num = 0

    def update(self):
        self.center_y += self.dy
        self.center_x += self.dx
        if self.bottom < 2:
            self.bottom = 2
            self.dy *= -1
        if self.top > SH - 2:
            self.top = SH - 2
            self.dy *= -1
        if self.left < 2:
            self.left = 2
            self.dx *= -1
        if self.right > SW - 2:
            self.right = SW - 2
            self.dx *= -1


class Asteroid3(arcade.Sprite):
    def __init__(self):
        super().__init__(random.choice(small_choice), asteroid_scale, hit_box_algorithm="Detailed")
        self.w = int(self.width)
        self.h = int(self.height)
        self.dx = random.randrange(-1, 2, 2)
        self.dy = random.randrange(-1, 2, 2)
        self.num = 0

    def update(self):
        self.center_y += self.dy
        self.center_x += self.dx
        if self.bottom < 2:
            self.bottom = 2
            self.dy *= -1
        if self.top > SH - 2:
            self.top = SH - 2
            self.dy *= -1
        if self.left < 2:
            self.left = 2
            self.dx *= -1
        if self.right > SW - 2:
            self.right = SW - 2
            self.dx *= -1


class Asteroid4(arcade.Sprite):
    def __init__(self):
        super().__init__(random.choice(tiny_choice), asteroid_scale, hit_box_algorithm="Detailed")
        self.w = int(self.width)
        self.h = int(self.height)
        self.dx = random.randrange(-1, 2, 2)
        self.dy = random.randrange(-1, 2, 2)
        self.num = 0

    def update(self):
        self.center_y += self.dy
        self.center_x += self.dx
        if self.bottom < 2:
            self.bottom = 2
            self.dy *= -1
        if self.top > SH - 2:
            self.top = SH - 2
            self.dy *= -1
        if self.left < 2:
            self.left = 2
            self.dx *= -1
        if self.right > SW - 2:
            self.right = SW - 2
            self.dx *= -1


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

# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self,SW,SH,title):
        super().__init__(SW, SH, title)
        self.secondary = arcade.SpriteList()
        arcade.set_background_color(arcade.color.WHITE)
        self.set_mouse_visible(False)

        self.current_state = 0
        self.game_running = False

        self.explosion_texture_list = []
        for i in range(EXPLOSION_TEXTURE_COUNT):
            texture_name = f"Images/explosions/explosion{i:04}.png"
            self.explosion_texture_list.append(arcade.load_texture(texture_name))

    def on_draw(self):
        arcade.start_render()
        if self.current_state == 0:
            arcade.draw_rectangle_filled(SW // 2, SH // 2, SW, SH, arcade.color.BLACK)
            arcade.draw_text("Use arrow keys to move the ship and SPACE to fire. Press P to play!"
                             , SW / 2 - 270, SH / 2, (0, 0, 255), 14)
            arcade.draw_text("Split all the asteroids to win!"
                             , SW / 2 - 110, SH / 2 - 50, (0, 0, 255), 14)
        elif self.game_running is True:
            arcade.draw_texture_rectangle(SW // 2, SH // 2, SW, SH, self.background)
            self.player_list.draw()
            self.bullets_right.draw()
            self.bullets_left.draw()
            self.asteroid_list.draw()
            self.explosions.draw()

            arcade.draw_lrtb_rectangle_filled(SW - 95, SW, SH, SH - 35, arcade.color.WHITE)
            output = f"Level: {self.current_state}"
            arcade.draw_text(output, SW - 90, SH - 15, arcade.color.BLACK, 14)
            output = f"Score: {self.score}"
            arcade.draw_text(output, SW - 90, SH - 30, arcade.color.BLACK, 14)

        else:
            output = f"Score: {self.score}"
            arcade.draw_rectangle_filled(SW // 2, SH // 2, SW, SH, arcade.color.BLACK)
            arcade.draw_text("Game Over! Press P to play again!", SW / 2 - 140, SH / 2, (0, 0, 255), 14)
            arcade.draw_text("Choose I for instructions", SW / 2 - 90, SH / 2 - 20, (0, 0, 255), 14)
            arcade.draw_text(output, SW / 2 - 35, SH / 2 - 40, (0, 0, 255), 14)

    def on_update(self, dt):
        if 0 < self.current_state < 4:
            self.game_running = True
        else:
            self.game_running = False

        if self.game_running is True:
            self.player_list.update()
            self.bullets_right.update()
            self.bullets_left.update()
            self.asteroid_list.update()
            self.explosions.update()

            if len(self.asteroid_list) == 0:
                self.current_state += 1
                self.setup()

            player_hit = arcade.check_for_collision_with_list(self.ship, self.asteroid_list)
            if len(player_hit) > 0:
                self.ship.kill()
                self.current_state = 4

            for asteroid in self.asteroid_list:

                asteroid_hit = arcade.check_for_collision_with_list(asteroid, self.asteroid_list)
                if len(asteroid_hit) > 0:
                    if asteroid.center_x < asteroid_hit[0].left or asteroid.center_x > asteroid_hit[0].right:
                        asteroid.dx *= -1
                    elif asteroid.center_y < asteroid_hit[0].bottom or asteroid.center_y > asteroid_hit[0].top:
                        asteroid.dy *= -1

                    asteroid_hit.clear()

            for bullet in self.bullets_left:
                hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)
                if len(hit_list) > 0:
                    explosion = Explosion(self.explosion_texture_list)
                    explosion.center_x = hit_list[0].center_x
                    explosion.center_y = hit_list[0].center_y
                    self.explosions.append(explosion)
                    arcade.play_sound(explosion.explosion_sound)
                    bullet.kill()
                    self.score += ENEMY_PTS
                for asteroid in hit_list:
                    if asteroid.num == 1:
                        self.split2(3, asteroid.center_x, asteroid.center_y)
                        asteroid.kill()
                    if asteroid.num == 2:
                        self.split3(2, asteroid.center_x, asteroid.center_y)
                        asteroid.kill()
                    if asteroid.num == 3:
                        self.split4(2, asteroid.center_x, asteroid.center_y)
                        asteroid.kill()
                    if asteroid.num == 4:
                        asteroid.kill()
                    hit_list.clear()

            for bullet in self.bullets_right:
                hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)
                if len(hit_list) > 0:
                    if len(hit_list) > 0:
                        explosion = Explosion(self.explosion_texture_list)
                        explosion.center_x = hit_list[0].center_x
                        explosion.center_y = hit_list[0].center_y
                        self.explosions.append(explosion)
                        arcade.play_sound(explosion.explosion_sound)
                        bullet.kill()
                        self.score += ENEMY_PTS
                    bullet.kill()
                for asteroid in hit_list:
                    if asteroid.num == 1:
                        self.split2(3, asteroid.center_x, asteroid.center_y)
                        asteroid.kill()
                    if asteroid.num == 2:
                        self.split3(2, asteroid.center_x, asteroid.center_y)
                        asteroid.kill()
                    if asteroid.num == 3:
                        self.split4(2, asteroid.center_x, asteroid.center_y)
                        asteroid.kill()
                    if asteroid.num == 4:
                        asteroid.kill()
                    hit_list.clear()

    def setup(self):
        if self.current_state == 1:
            arcade.set_background_color(arcade.color.SKY_BLUE)
            self.background = arcade.load_texture("Space/Backgrounds/lvl1.png")
        elif self.current_state == 2:
            arcade.set_background_color(arcade.color.WHITE_SMOKE)
            self.background = arcade.load_texture("Space/Backgrounds/lvl2.png")
        elif self.current_state == 3:
            arcade.set_background_color(arcade.color.ROSE_RED)
            self.background = arcade.load_texture("Space/Backgrounds/lvl3.png")
        self.player_list = arcade.SpriteList()
        self.bullets_right = arcade.SpriteList()
        self.bullets_left = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.explosions = arcade.SpriteList()

        self.ship = Player()
        self.ship.center_x = SW/2
        self.ship.center_y = SH/2
        self.player_list.append(self.ship)

        for i in range(1, asteroid_c[self.current_state] + 1):
            asteroid = Asteroid1()
            asteroid.num = 1

            if i % 2 == 0:
                asteroid.center_x = random.randrange(asteroid.w, int(SW/3))
                asteroid.center_y = random.randrange(asteroid.h, SH - asteroid.h)
            else:
                asteroid.center_x = random.randrange(int(SW * 2/3), SW - asteroid.w)
                asteroid.center_y = random.randrange(asteroid.h, SH - asteroid.h)
            self.asteroid_list.append(asteroid)

    def split2(self, num, x, y):

        for i in range(num):
            asteroid = Asteroid2()
            asteroid.center_x = x + random.randint(-75, 75)
            asteroid.center_y = y + random.randint(-75, 75)
            asteroid.num = 2
            self.asteroid_list.append(asteroid)

    def split3(self, num, x, y):

        for i in range(num):
            asteroid = Asteroid3()
            asteroid.center_x = x + random.randint(-60, 60)
            asteroid.center_y = y + random.randint(-60, 60)
            asteroid.num = 3
            self.asteroid_list.append(asteroid)

    def split4(self, num, x, y):

        for i in range(num):
            asteroid = Asteroid4()
            asteroid.center_x = x + random.randint(-50, 50)
            asteroid.center_y = y + random.randint(-50, 50)
            asteroid.num = 4
            self.asteroid_list.append(asteroid)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP and self.game_running:
            self.ship.speed = MOVEMENT_SPEED
        elif key == arcade.key.DOWN and self.game_running:
            self.ship.speed = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT and self.game_running:
            self.ship.change_angle = ANGLE_SPEED
        elif key == arcade.key.RIGHT and self.game_running:
            self.ship.change_angle = -ANGLE_SPEED
        elif key == arcade.key.P and not self.game_running:
            self.score = 0
            self.current_state = 1
            self.setup()
        elif key == arcade.key.I and not self.game_running:
            self.current_state = 0
            self.setup()
        elif key == arcade.key.SPACE and self.game_running:
            num = random.randint(0, 1)
            self.bullet = Bullet()
            self.bullet_2 = Bullet()

            if self.ship.angle >= 45 and self.ship.angle <= 135 or self.ship.angle <= -45 and self.ship.angle >= -135:
                self.bullet.center_y = self.ship.top
                self.bullet_2.center_y = self.ship.bottom

                self.bullet.center_x = self.ship.center_x
                self.bullet_2.center_x = self.ship.center_x
            if self.ship.angle >= 225 and self.ship.angle <= 315 or self.ship.angle <= -225 and self.ship.angle >= -315:
                self.bullet.center_y = self.ship.top
                self.bullet_2.center_y = self.ship.bottom

                self.bullet.center_x = self.ship.center_x
                self.bullet_2.center_x = self.ship.center_x
            if self.ship.angle <= 45 and self.ship.angle >= 0 or self.ship.angle >= -45 and self.ship.angle <= 0 \
                    or self.ship.angle <= 360 and self.ship.angle >= 315 \
                    or self.ship.angle >= -360 and self.ship.angle <= -315:
                self.bullet.center_y = self.ship.center_y
                self.bullet_2.center_y = self.ship.center_y

                self.bullet.center_x = self.ship.left
                self.bullet_2.center_x = self.ship.right
            if self.ship.angle >= 135 and self.ship.angle <= 180 or self.ship.angle <= 225 and self.ship.angle >= 180 \
                    or self.ship.angle <= -135 and self.ship.angle >= -180 \
                    or self.ship.angle >= -225 and self.ship.angle <= -180:
                self.bullet.center_y = self.ship.center_y
                self.bullet_2.center_y = self.ship.center_y

                self.bullet.center_x = self.ship.left
                self.bullet_2.center_x = self.ship.right

            self.bullet.angle = self.ship.angle
            self.bullet_2.angle = self.ship.angle

            self.bullet.speed = BULLET_SPEED
            self.bullet_2.speed = BULLET_SPEED

            self.bullets_right.append(self.bullet)
            self.bullets_left.append(self.bullet_2)
            if num == 0:
                arcade.play_sound(self.ship.laser1)
            else:
                arcade.play_sound(self.ship.laser2)
            self.score -= BULLET_PTS

    def on_key_release(self, key, modifiers):
        if key == arcade.key.DOWN:
            self.ship.speed = -1
        elif key == arcade.key.UP:
            self.ship.speed = 1
        elif key == arcade.key.LEFT:
            self.ship.change_angle = 1
        elif key == arcade.key.RIGHT:
            self.ship.change_angle = -1


#-----Main Function--------
def main():
    window = MyGame(SW, SH, "Caleb Little - Asteroid Splitter")
    window.setup()
    arcade.run()

#------Run Main Function-----
if __name__ == "__main__":
    main()
