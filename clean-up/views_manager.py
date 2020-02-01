import arcade
from gui_game.game_play import *
from visualmodules import *

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Trail_Blazers Oregon Trail'

class Views:
    def __init__(self):
        self.window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, 'OREGON TRAIL')
        self.state = {}

    def start(self):
        print (IntroWindow)
        self.show_next_view(IntroWindow,None)   #  Checked, Intro Window is an arcade View
        arcade.run()

    def show_next_view(self, ViewClass, props):
        self.window.show_view(ViewClass)

    def intro_done(self):
        props = {'done_handler' : self.choose_party_done}
        self.show_next_view(ChoosePartyView, props)

    def choose_party_done(self):
        self.state['wagon_party'] = wagon_party
        self.state['funds'] = funds
        # props = {
        #     'done handler' = 

        # }

    def learn_more_done(self):
        props = {'done_handler' : self.choose_party_done}
        self.show_next_view(ChoosePartyView, props)

    def view_party_done(self):
        pass
    

if __name__ == '__main__':
    game = Views()
    game.start()
