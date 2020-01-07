import arcade
import main
from visualmodules.button import TextButton, TravelTextButton, LearnTextButton, QuitTextButton, check_mouse_press_for_buttons, check_mouse_release_for_buttons

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 780
SCREEN_TITLE = 'Trail_Blazers Oregon Trail'

class IntroWindow(arcade.View):
    def __init__(self, width, height, title):
        super().__init__()

    def on_show(self):
    
        # arcade.set_background_color(arcade.color.BLUE)

        # self.background_list = None

        self.setup()

        self.button_list = []

        button_center_spacing = SCREEN_WIDTH // 2
        button_center_vertical_spacing = SCREEN_HEIGHT // 2

        travel_button = TravelTextButton(button_center_spacing, button_center_vertical_spacing, self.start_travel)
        self.button_list.append(travel_button)

        learn_button = LearnTextButton(button_center_spacing, button_center_vertical_spacing - 55, self.pause_program)
        self.button_list.append(learn_button)

        quit_button = QuitTextButton(button_center_spacing, button_center_vertical_spacing - 110, self.pause_program)
        self.button_list.append(quit_button)

    def start_travel(self):
        travel_trail = TravelTrail(SCREEN_WIDTH, SCREEN_HEIGHT, 'TravelTrail')
        self.window.show_view(travel_trail)

    def setup(self):
        self.background = arcade.load_texture('./img/intro_background.png')

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                    SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

    # def on_mouse_release(self):
    #     travel_trail = TravelTrail(SCREEN_WIDTH, SCREEN_HEIGHT, 'TravelTrail')
    #     self.window.show_view(travel_trail)

    def pause_program(self):
        self.pause = True

    def resume_program(self):
        self.pause = False

    def on_update(self, delta_time):
        pass

class TravelTrail(arcade.View):
    def __init__(self, width, height, title):
        super().__init__()
        self.background = arcade.load_texture('./img/intro_background.png')

    # def setup(self):
        # self.background = arcade.load_texture('./img/intro_background.png')

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.BLACK)
        arcade.draw_text('it worked', 200, 100,
                        arcade.color.BLACK, font_size=50, anchor_x="center")
    
        
def start_game():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    intro_view = IntroWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.show_view(intro_view)
    arcade.run()


if __name__ == "__main__":
    start_game()