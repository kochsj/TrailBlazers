import arcade
from button import ActionButton


class RationsView(arcade.View):
    """ Rations View """

    def on_show(self):
        def filling_ration_action():
            self.props["done_handler"](1)

        def meager_ration_action():
            self.props["done_handler"](2)

        def bare_ration_action():
            self.props["done_handler"](3)

        filling_button = ActionButton( filling_ration_action, 700, 500, 400, 50, "Filling", 30, "Arial", arcade.color.WHITE,)

        meager_button = ActionButton( meager_ration_action, 700, 300, 400, 50, "Meager", 30, "Arial", arcade.color.WHITE,)

        bare_button = ActionButton( bare_ration_action, 700, 100, 400, 50, "Bare Bones", 30, "Arial", arcade.color.WHITE,)

        self.button_list.append(filling_button)

        self.button_list.append(meager_button)

        self.button_list.append(bare_button)


    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        arcade.draw_text( "Welcome to Rations R Us", 200, 750, arcade.color.WHITE, 40, width=1000, align="center", bold=True,)

        super().on_draw()


def main():
    RationsView(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "Rations"
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = RationsView()

    def rations_selected(val):
        print(val)

    props = {"done_handler": rations_selected}
    view.props = props
    window.show_view(view)
    arcade.run()
