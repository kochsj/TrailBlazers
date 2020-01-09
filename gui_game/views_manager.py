import arcade
import game_play
from gui_game.choose_party import ChoosePartyView

class Views:
    def __init__(self):
        self.window = arcade.Window(game_play.SCREEN_WIDTH, game_play.SCREEN_HEIGHT, 'OREGON TRAIL')
        self.state = {}

    def start(self):
        self.show_next_view(self, game_play.IntroWindow)
        arcade.run()

    def show_next_view(self, ViewClass, props):
        view = ViewClass(self.window.width, self.window.height)
        self.window.show(view)

    def intro_done(self):
        props = {'done_handler' : self.choose_party_done}

        self.show_next_view(ChoosePartyView, props)

    def choose_party_done(self):
        self.state['wagon_party'] = wagon_party
        self.state['funds'] = funds
        props = {
            # 'done handler' = TBD

        }

    def learn_more_done(self):
        props = {'done_handler' : self.choose_party_done}
        self.show_next_view(ChoosePartyView, props)

    def view_party_done(self):
        pass
    

if __name__ == '__main__':
    game = Views()
    game.start()
