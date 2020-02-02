import arcade
from gui_game.button import ActionButton


class RationsView(arcade.View):
    """ Rations View """

    def on_show(self):
        def filling_ration_action(btn):
            self.done_handler({"id":"rations_view","action":"filling","rations":"filling"})

        def meager_ration_action(btn):
            self.done_handler({"id":"rations_view","action":"meager","rations":"meager"})

        def bare_ration_action(btn):
            self.done_handler({"id":"rations_view","action":"bare","rations":"bare-bones"})

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

        arcade.draw_text( "Choose your rationing level:", 200, 750, arcade.color.WHITE, 40, width=1000, align="center", bold=True,)

        super().on_draw()

