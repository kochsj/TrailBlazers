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
        arcade.draw_text("You start your journey with a wagon, a wagon wheel, wagon axle,",150,750,arcade.color.BLACK,20)
        arcade.draw_text("and a wagon tongue for attaching the oxen to the wagon.",150,700,arcade.color.BLACK,20)
        arcade.draw_text("It is advisable to pick up spare parts, food, ammunition, and",150,650,arcade.color.BLACK,20) 
        arcade.draw_text("other necessiary supplies for your journey.",150,600,arcade.color.BLACK,20)
        arcade.draw_text("Let's head to the store to begin.",150,550,arcade.color.BLACK,20)
        super().on_draw()