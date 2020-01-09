import arcade
from button import ActionButton


class PaceView(arcade.View):
    """ Pace View """

    def on_show(self):
        def fast_pace_action():
            self.props["done_handler"](1)

        def medium_pace_action():
            self.props["done_handler"](2)

        def slow_pace_action():
            self.props["done_handler"](3)

        fast_button = ActionButton( fast_pace_action, 700, 500, 400, 50, "Filling", 30, "Arial", arcade.color.WHITE,)

        medium_button = ActionButton( medium_pace_action, 700, 300, 400, 50, "Meager", 30, "Arial", arcade.color.WHITE,)

        slow_button = ActionButton( slow_pace_action, 700, 100, 400, 50, "Bare Bones", 30, "Arial", arcade.color.WHITE,)

        self.button_list.append(fast_button)

        self.button_list.append(medium_button)

        self.button_list.append(slow_button)


    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        arcade.draw_text( "Change your pace here!", 200, 750, arcade.color.WHITE, 40, width=1000, align="center", bold=True,)

        super().on_draw()


def main():
    PaceView(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "Pace"
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = PaceView()

    def pace_selected(val):
        print(val)

    props = {"done_handler": pace_selected}
    view.props = props
    window.show_view(view)
    arcade.run()