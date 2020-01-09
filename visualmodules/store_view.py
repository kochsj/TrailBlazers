
import arcade
from button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"


class StoreView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__()
        self.store_items = ["Oxen","Food","Clothing","Ammunition","Wagon Wheel","Wagon Axle","Wagon Tongue"]
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        
        l=len(self.store_items)
        for i in range (l):
            arcade.draw_text(self.store_items[l-(i+1)],600,180+80*i,arcade.color.WHITE,25,)
        arcade.draw_text("Welcome to the General Store",200, 750, arcade.color.WHITE, 40, width=1000, align="center",bold=True)
        
        super().on_draw()

    def on_show(self):
        def leaving():
            exit()
        
        def oxen(): print('attempting to buy oxen')
        def food(): print('attempting to buy food')
        def clothing(): print('attempting to buy clothing')
        def ammunition(): print('attempting to buy ammo'),
        def wheel(): print('attempting to buy wheels')
        def axle(): print('attempting to buy axles')
        def tongue(): print('attempting to buy tongues')

        action_array = [oxen,food,clothing,ammunition,wheel,axle,tongue]
        
        l=len(self.store_items)
        for i in range (l):
            button = ActionButton(action_array[l-i-1],450,(180+80*i),200,50,"buy",30,"Arial",arcade.color.WHITE)
            self.button_list.append(button)


        button = ActionButton(leaving,700,100,400,50,"Exit Store",30,"Arial",arcade.color.WHITE)
        self.button_list.append(button)
        


def main():
    StoreView(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "Pace"
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = StoreView()

    window.show_view(view)
    arcade.run()