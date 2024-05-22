# 14.0 BB8 ATTACK GAME   Name:________________
 
#You will use the starting code below and build the program "BB8 Attack" as you go through Chapter 14.


import random
import arcade
import numpy as np

# --- Constants ---
BB8_scale = 0.3
trooper_scale = 0.1
trooper_count = 5
SPEED = 3

rows = 10
cols = 13

width = 20
height = 20
margin = 5

SW = (width + margin) * cols + margin
SH = (height + margin) * rows + margin


# ------MyGame Class--------------
class MyGame(arcade.Window):

    def __init__(self,SW,SH,title):
        super().__init__(SW, SH, title)
        self.grid = np.zeros((rows, cols))
        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(True)

    def on_draw(self):
        arcade.start_render()

        for row in range(rows):
            for column in range(cols):
                if self.grid[row][column] == 1:
                    color = arcade.color.BLUE
                else:
                    color = arcade.color.WHITE
                x = (margin + width) * column + margin + width//2
                y = (margin + height) * row + margin + height//2

                arcade.draw_rectangle_filled(x, y, width, height, color)

    def on_mouse_press(self, x, y, button, modifiers):
        column = x // (width + margin)
        row = y // (height + margin)

        if row < rows and column < cols:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

#-----Main Function--------
def main():
    window = MyGame(SW,SH,"Grid Game")
    arcade.run()

#------Run Main Function-----
if __name__ == "__main__":
    main()
