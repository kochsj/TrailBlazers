
import arcade
from button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)


    # def on_key_press(self, key, modifiers):
    #     """Called whenever a key is pressed.  Returns a string if ENTER was pressed, otherwise returns None """
    #     if key == arcade.key.BACKSPACE:
    #         self.txt = self.txt[:-1]
    #     elif key == arcade.key.ENTER:
    #         return self.txt
    #     else:
    #         self.txt += chr(key)
        # return None

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        def hi():
            print('hihi')
        
        # for i in range (l):
        #     arcade.draw_text(store_items[l-(i+1)],600,180+80*i,arcade.color.WHITE,25,)
        arcade.draw_text("Welcome to the General Store",200, 750, arcade.color.WHITE, 40, width=1000, align="center",bold=True)
        store_items = ["Oxen","Food","Clothing","Ammunition","Wagon Wheel","Wagon Axle","Wagon Tongue"]
        l=len(store_items)
        super().on_draw()
      
    
    def on_show(self):
        def leaving():
            print('leaving')
        button = ActionButton(leaving,700,100,400,50,"Exit Store",30,"Arial",arcade.color.WHITE)
        self.button_list.append(button)
        




def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


main()