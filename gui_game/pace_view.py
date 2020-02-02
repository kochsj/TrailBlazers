import arcade
from gui_game.button import ActionButton


class PaceView(arcade.View):
    """ Pace View """

    def on_show(self):
        def steady_pace_action(btn):
            self.done_handler({"id":"pace_view", "action":"steady", "pace":0})

        def strenuous_pace_action(btn):
            self.done_handler({"id":"pace_view", "action":"strenuous", "pace":1})

        def grueling_pace_action(btn):
            self.done_handler({"id":"pace_view", "action":"grueling", "pace":2})

        steady_button = ActionButton( steady_pace_action, 700, 500, 400, 50, "Steady", 30, "Arial", arcade.color.WHITE,)

        strenuous_button = ActionButton( strenuous_pace_action, 700, 300, 400, 50, "Strenuous", 30, "Arial", arcade.color.WHITE,)

        grueling_button = ActionButton( grueling_pace_action, 700, 100, 400, 50, "Greuling", 30, "Arial", arcade.color.WHITE,)

        self.button_list.append(steady_button)

        self.button_list.append(strenuous_button)

        self.button_list.append(grueling_button)


    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        arcade.draw_text( "Change your pace here!", 200, 750, arcade.color.WHITE, 40, width=1000, align="center", bold=True,)

        super().on_draw()
