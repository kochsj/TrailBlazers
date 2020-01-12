import arcade
from visualmodules.button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"

class SuppliesExplainationView(arcade.View):
    """This view shows the player text explaining what supplies are on hand at the start of the game"""
    def on_show(self):
        """Sets up the continue button for the page before draw"""
        def proceed(btn):
            self.done_handler({"id":"general_store","action":"go_to_store"})
        button = ActionButton(proceed,600, 200,200,50,"Continue",20,"Arial",arcade.color.WHITE)
        self.button_list.append(button)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Before setting out on the trail, you should buy some supplies.",300,600,arcade.color.BLACK,30)
        super().on_draw()