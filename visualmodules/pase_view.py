import arcade
from button import ActionButton


class PaceView(arcade.View):
    """ Pace View """

    def on_show(self):
        def steady_pace_action():
            self.props["done_handler"](1)

        def strenuous_pace_action():
            self.props["done_handler"](2)

        def grueling_pace_action():
            self.props["done_handler"](3)

        steady_button = ActionButton( steady_pace_action, 700, 500, 400, 50, "Filling", 30, "Arial", arcade.color.WHITE,)

        strenuous_button = ActionButton( strenuous_pace_action, 700, 300, 400, 50, "Meager", 30, "Arial", arcade.color.WHITE,)

        grueling_button = ActionButton( grueling_pace_action, 700, 100, 400, 50, "Bare Bones", 30, "Arial", arcade.color.WHITE,)

        self.button_list.append(steady_button)

        self.button_list.append(strenuous_button)

        self.button_list.append(grueling_button)


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