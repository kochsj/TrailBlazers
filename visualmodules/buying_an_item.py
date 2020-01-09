
import arcade
from button import ActionButton
import re

class StoreView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__()
        self.store_items = [("You will need a team of oxen to pull your wagon. \nYou will want at least two, but I reccomend at least 6 in case you lose any along the way\nI charge $40 an ox.",40),
                            ("You will need plenty of food for your party during the trip.\nTrail-goers without enough to eat are in increased danger of disease in addition to starvation\n I charge $0.25 per pound.",0.25),
                            ("You'll want cold weather gear for the winter, espescially if you end up stuck in the mountains\nYou'll also want light clothing for the summers to protect against sunburn and heatstroke\nI sell outfits for $15 each",15),
                            ("Hunting is an invaluable way to re-provision your wagon beteween towns.\nIn a pinch, you can even trade hunted game to travelers for other supplies.\n  I reccomend a healthy pile of ammunition, which I sell for $2 per box of 20 bullets.",0.25),
                            ("The Oregon Trail is very rocky in places.  If your wheel hits a rock hard enough it can break clean off!\nObviously if your wagon doesn't have a wheel, it can't even carry you into town to buy a spare!\nWise travellers keeps spares with them for precisely such emergencies.",10),
                            ("The Axle is what connects a wheel to the cart.\nIf it breaks, you can't move!  You might want to bring a spare.\n I sell them for $10 per axle",10),
                            ("A wagon tongue is how you yoke your oxen to your axle.\nThey're subject to a lot of strain and prone to breaking, which is unfortunate, because your wagon can't move without one.\n  Buying a spare now for only $10 could save you a lot of trouble down the line"),10]
        self.item_to_buy = "axle"
        self.index = 5
        self.cost = self.store_items[self.index][1]
        self.ss = self.store_items[self.index][0]+"\n\nHow many would you like to buy?   "
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """
        if not "buy?   " in self.ss: self.ss = self.store_items[self.index][0]+"\n\nHow many would you like to buy?   "  # repairs the string it the user deletes too many characters
        arcade.start_render()
        arcade.draw_text("Welcome to the General Store",200, 750, arcade.color.WHITE, 40, width=1000, align="center",bold=True)
        arcade.draw_text(self.ss,200, 350, arcade.color.WHITE, 20)       
        super().on_draw()
    

    def on_show(self):
        def buying():
            quantity = self.ss[-10:]
            quantity = int(re.sub('[^0-9]','', quantity))
            print(f"buying {quantity} {self.item_to_buy} for {quantity * self.cost}")
        def leaving():
            exit()
        button = ActionButton(leaving,700,100,400,50,"Exit Store",30,"Arial",arcade.color.WHITE)
        self.button_list.append(button)
        button = ActionButton(buying,700,250,90,50,"buy",30,"Arial",arcade.color.WHITE)
        self.button_list.append(button)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed.  Updates the string."""
        if key == arcade.key.BACKSPACE:
            self.ss = self.ss[:-1]
        else:
            self.ss += chr(key) 

    

def main():
    StoreView(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "Store"
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = StoreView()
    window.show_view(view)
    arcade.run()