
import arcade
from button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title, item_index=5, game=None):
        super().__init__(width, height, title)
        self.store_items = [("You will need a team of oxen to pull your wagon. \nYou will want at least two, but I reccomend at least 6 in case you lose any along the way\nI charge $40 an ox.",40),
                            ("You will need plenty of food for your party during the trip.\nTrail-goers without enough to eat are in increased danger of disease in addition to starvation\n I charge $0.25 per pound.",0.25),
                            ("You will need clothing for both summer and winter. I charge $15 per outfit.",0.25),
                            ("You will need ammunition for your rifles to hunt. I charge $2 per box of 20 bullets.",0.25),
                            ("The Oregon Trail is very rocky in places.  Broken wagon weels aren't uncommon, you'd best carry spares.  I charge $10 per piece.",10),
                            ("The Axle is what connects a wheel to the cart.\nIf it breaks, you can't move!  You might want to bring a spare.\nI charge $10 per axle",10),
                            ("A wagon tongue is how you yoke your oxen to your axle.  It's impossible to travel without one.  I charge $10 per spare"),10]
        self.index = item_index
        self.ss = self.store_items[item_index][0]+"\n\nHow many would you like to buy?   "
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        if not "buy?   " in self.ss: self.ss = self.store_items[self.index][0]+"\n\nHow many would you like to buy?   "

        arcade.start_render()
        arcade.draw_text("Welcome to the General Store",200, 750, arcade.color.WHITE, 40, width=1000, align="center",bold=True)
        arcade.draw_text(self.ss,200, 350, arcade.color.WHITE, 20)       
        super().on_draw()
    
    def on_show(self):
        def leaving():
            exit()
        button = ActionButton(leaving,700,100,400,50,"Exit Store",30,"Arial",arcade.color.WHITE)
        self.button_list.append(button)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed.  Updates the string."""
        if key == arcade.key.BACKSPACE:
            self.ss = self.ss[:-1]
        else:
            self.ss += chr(key)
        return None    

def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


main()