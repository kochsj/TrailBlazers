import arcade
from gui_game.game_play import IntroWindow
from gui_game.choose_party import ChoosePartyView
from gui_game.test_view import TestView

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'View Runner'

def start_game():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = IntroWindow(SCREEN_WIDTH, SCREEN_HEIGHT, {})
    # view = ChoosePartyView(SCREEN_WIDTH, SCREEN_HEIGHT, {})
    # view = TestView()
    window.show_view(view)
    arcade.run()



if __name__ == "__main__":
    start_game()