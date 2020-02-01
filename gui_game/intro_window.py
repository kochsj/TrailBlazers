import arcade
from gui_game.button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Trail_Blazers Oregon Trail'

class Pages(arcade.View):
    def __init__(self, width, height, props):
        super().__init__()
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.state = {'wagon_party' : None ,'funds' : None}
        self.props = {}

        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)


    def button_handler(self, button):
        self.props['done_handler']()

    def on_draw(self):
        super().on_draw()
        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
    
    def quit_game(self):
        arcade.close_window()


class IntroWindow(Pages):

    background = arcade.load_texture('gui_game/media/intro_background.png')

    def on_show(self):

        travel_trail_button = ActionButton(self.button_handler, self.center_x, self.center_y, 300, 40, 'Travel the trail', name='travel_trail_button', font_color=arcade.color.WHITE)
        learn_more = ActionButton(self.button_handler, self.center_x, self.center_y - 55, 300, 40, 'learn more', name='learn_more', font_color=arcade.color.WHITE)
        quit_button = ActionButton(self.button_handler, self.center_x, self.center_y - 110, 100, 40, 'Quit', name='quit', font_color=arcade.color.WHITE)

        self.button_list.append(travel_trail_button)
        self.button_list.append(learn_more)
        self.button_list.append(quit_button)

    def button_handler(self, button):
        if button.name == 'travel_trail_button':
            self.done_handler({"id":"opening_menu","action":"begin"})

        elif button.name == 'learn_more':
            self.done_handler({"id":"opening_menu","action":"learn_more"})

        elif button.name == 'quit':
            arcade.close_window()


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.center_x, self.center_y, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        super().on_draw()