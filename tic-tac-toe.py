import random
import arcade

SW = 800
SH = 600


class Circle:
    def __init__(self, pos_x, pos_y, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rad = rad
        self.col = col

    def draw(self):
        arcade.draw_circle_outline(self.pos_x, self.pos_y, self.rad, self.col)


class MyGame(arcade.Window):
    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.move_list = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(300, 50, 300, 550, arcade.color.BLACK, 4)
        arcade.draw_line(500, 50, 500, 550, arcade.color.BLACK, 4)
        arcade.draw_line(100, 400, 700, 400, arcade.color.BLACK, 4)
        arcade.draw_line(100, 200, 700, 200, arcade.color.BLACK, 4)

        for move in self.move_list:
            move.draw()

    def on_update(self, dt):
        for i in range(len(self.move_list)):
            if i == 0:
                self.p1move.col = arcade.color.RED
            else:
                self.p1move.col = arcade.color.BLACK
        if len(self.move_list) > 3:
            self.move_list.pop(0)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.p1move = Circle(x, y, 50, arcade.color.BLACK)
            self.move_list.append(self.p1move)



# -----Main Function--------
def main():
    window = MyGame(SW,SH,"My Game")
    arcade.run()

#------Run Main Function-----
if __name__ == "__main__":
    main()

