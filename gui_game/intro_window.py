import arcade
from gui_game.button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "OREGON TRAIL"

class IntroView(arcade.View):

    background = arcade.load_texture('gui_game/media/intro_background.png')

    def on_show(self):

        travel_trail_button = ActionButton(self.button_handler, 700, 400, 300, 40, 'Travel the trail', name='travel_trail_button', font_color=arcade.color.WHITE)
        learn_more = ActionButton(self.button_handler, 700, 400 - 55, 300, 40, 'Learn More', name='learn_more', font_color=arcade.color.WHITE)
        quit_button = ActionButton(self.button_handler, 700, 400 - 110, 100, 40, 'Quit', name='quit', font_color=arcade.color.WHITE)

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
        arcade.draw_texture_rectangle(700, 400, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        super().on_draw()
