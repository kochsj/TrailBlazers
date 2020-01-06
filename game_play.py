import arcade
import main

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 780
SCREEN_TITLE = 'Trail_Blazers Oregon Trail'
GAME_SCREEN_WIDTH = 800
GAME_SCREEN_HEIGHT = 600

class test_game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLUE)

        self.background_list = None

        self.setup()

    def setup(self):
        self.background = arcade.load_texture('./img/intro_background.png')
        # self.game_screen = arcade.color.BLACK

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                    SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # arcade.draw_texture_rectangle(GAME_SCREEN_HEIGHT // 2, GAME_SCREEN_WIDTH // 2, 
        #                             GAME_SCREEN_WIDTH, GAME_SCREEN_HEIGHT, self.game_screen)

    def on_update(self, delta_time):
        pass

    # def game_intro(self):
    #     game.play()
        
def start_game():
    """ Main method """
    window = test_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    start_game()