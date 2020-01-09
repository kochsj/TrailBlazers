
import arcade
from button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"


class DepartureView(arcade.View):
    """
    Main application class.
    """

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.draw_text("When Do You Want To Depart?",200, 500, arcade.color.WHITE, 40, width=1000, align="center",bold=True)

        
        super().on_draw()

    def on_show(self):
        def leaving():
            exit()
        
        def march(): print('March')
        def april(): print('April')
        def may(): print('May')
        def june(): print('June'),
       

        action_array = [march,april,may,june]
        months = ["March","April","May","June"]
        
        for i in range (4):
            button = ActionButton(action_array[i],700,(180+80*i),200,50,months[i],30,"Arial",arcade.color.WHITE)
            self.button_list.append(button)



def main():
    DepartureView(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "Departure"
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = DepartureView()

    window.show_view(view)
    arcade.run()