import arcade
from visualmodules.button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"

class CharacterCreationView(arcade.View):
    """
    View that asks player to choose a starting leader
    # Returns a tuple of (the name of the leader, and the starting_funds (based on leader's profession))
    """
    def on_show(self): #to set up view
        def banker(btn):
            self.done_handler({"id":"char_creation","action":"banker"})
        def carpenter(btn):
            self.done_handler({"id":"char_creation","action":"carpenter"})
        def farmer(btn):
            self.done_handler({"id":"char_creation","action":"farmer"})
        menu_actions = [banker,carpenter,farmer]
        menu_items = ["Banker", "Carpenter", "Farmer"]

        shift = 200 #px that each button is shifted

        for i in range(len(menu_actions)):
            button = ActionButton(menu_actions[i], 150, 600-shift*i,200,50,menu_items[i],20,"Arial",arcade.color.WHITE)
            self.button_list.append(button)


    def on_draw(self): #drawn continuously
        
        arcade.start_render()
        arcade.draw_text("Every wagon train needs a leader...",200, 725, arcade.color.BLACK, 40, width=1000, align="center",bold=True)
        arcade.draw_text("Here is some BANKER info...",350, 580, arcade.color.BLACK, 40, width=1000, align="center",bold=True)
        arcade.draw_text("Here is some CARPENTER info...",350, 380, arcade.color.BLACK, 40, width=1000, align="center",bold=True)
        arcade.draw_text("Here is some FARMER info...",350, 180, arcade.color.BLACK, 40, width=1000, align="center",bold=True)
        super().on_draw()

class BankerView(arcade.View):
    """
    View that shows the player info about the banker, Matthew Wilder
    """
    def on_show(self):
        """Sets up the continue button for the page before draw"""
        def proceed(btn):
            self.done_handler({"id":"char_creation","action":"finish_creation"})
        button = ActionButton(proceed,600, 200,200,50,"Continue",20,"Arial",arcade.color.WHITE)
        self.button_list.append(button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Matthew Wilder",300,600,arcade.color.BLACK,30)
        super().on_draw()

class CarpenterView(arcade.View):
    """
    View that shows the player info about the carpenter, Jeddidiah McHugh
    """
    def on_show(self):
        """Sets up the continue button for the page before draw"""
        def proceed(btn):
            self.done_handler({"id":"char_creation","action":"finish_creation"})
        button = ActionButton(proceed,600, 200,200,50,"Continue",20,"Arial",arcade.color.WHITE)
        self.button_list.append(button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Jeddidiah McHugh",300,600,arcade.color.BLACK,30)
        super().on_draw()

class FarmerView(arcade.View):
    """
    View that shows the player info about the farmer, Levi Lapp
    """
    def on_show(self):
        """Sets up the continue button for the page before draw"""
        def proceed(btn):
            self.done_handler({"id":"char_creation","action":"finish_creation"})
        button = ActionButton(proceed,600, 200,200,50,"Continue",20,"Arial",arcade.color.WHITE)
        self.button_list.append(button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Levi Lapp",300,600,arcade.color.BLACK,30)
        super().on_draw()
