
import arcade
from gui_game.button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"


class DepartureView(arcade.View):
    """
    Main application class.
    """
    def on_show(self):
        # def leaving(btn):
        #     exit()
        
        def march(btn):
            self.done_handler({"id":"opening_menu","action":"decide_month", "month":"March"})
        def april(btn):
            self.done_handler({"id":"opening_menu","action":"decide_month", "month":"April"})
        def may(btn):
            self.done_handler({"id":"opening_menu","action":"decide_month", "month":"May"})
        def june(btn):
            self.done_handler({"id":"opening_menu","action":"decide_month", "month":"June"})
       

        action_array = [march,april,may,june]
        months = ["March","April","May","June"]
        
        for i in range (4):
            button = ActionButton(action_array[i],700,(180+80*i),200,50,months[i],30,"Arial",arcade.color.WHITE)
            self.button_list.append(button)

    # def on_show(self):
    #     """Sets up the continue button for the page before draw"""
    #     def proceed(btn):
    #         self.done_handler({"id":"char_creation","action":"finish_creation"})
    #     button = ActionButton(proceed,600, 200,200,50,"Continue",20,"Arial",arcade.color.WHITE)
    #     self.button_list.append(button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Matthew Wilder",300,600,arcade.color.BLACK,30)
        super().on_draw()

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        
        arcade.draw_text("When Do You Want To Depart?",200, 500, arcade.color.WHITE, 40, width=1000, align="center",bold=True)

        
        super().on_draw()




# def main():
#     DepartureView(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#     arcade.run()


# if __name__ == "__main__":
#     SCREEN_WIDTH = 1400
#     SCREEN_HEIGHT = 800
#     SCREEN_TITLE = "Departure"
#     window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#     view = DepartureView()

#     window.show_view(view)
#     arcade.run()