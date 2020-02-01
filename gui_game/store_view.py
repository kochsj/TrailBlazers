
import arcade
from gui_game.button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"


class StoreView(arcade.View):
    """
    Main application class.
    """

    def __init__(self, inventory, funds):
        super().__init__()
        self.store_items = ["Oxen","Food","Clothing","Ammunition","Wagon Wheel","Wagon Axle","Wagon Tongue"]
        self.inventory = inventory
        self.funds = funds
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        
        l=len(self.store_items)
        for i in range (l):
            arcade.draw_text(f"Current quantity: {self.inventory[self.store_items[l-i-1]]}",600,180+80*i,arcade.color.WHITE,25,)
        arcade.draw_text("Welcome to the General Store",200, 750, arcade.color.WHITE, 40, width=1000, align="center",bold=True)
        arcade.draw_text(f"Current Funds: {self.funds}", 1000,650,arcade.color.WHITE,20)
        
        super().on_draw()

    def on_show(self):
        def leaving(btn):
            self.done_handler({"id":"general_store","action":"head_to_trail"})       
        def oxen(btn):
            self.done_handler({"id":"general_store","action":"buy_oxen"})
        def food(btn):
            self.done_handler({"id":"general_store","action":"buy_food"})
        def clothing(btn):
            self.done_handler({"id":"general_store","action":"buy_clothing"})
        def ammunition(btn):
            self.done_handler({"id":"general_store","action":"buy_ammo"})
        def wheel(btn):
            self.done_handler({"id":"general_store","action":"buy_wheel"})
        def axle(btn):
            self.done_handler({"id":"general_store","action":"buy_axle"})
        def tongue(btn):
            self.done_handler({"id":"general_store","action":"buy_tongue"})

        action_array = [oxen,food,clothing,ammunition,wheel,axle,tongue]
        
        l=len(self.store_items)
        for i in range (l):
            button = ActionButton(action_array[l-i-1],450,(180+80*i),200,50,self.store_items[l-i-1],20,"Arial",arcade.color.WHITE)
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