import arcade
from arcade.gui import *
from trail_animation.trail_animation import TraverseTheTrail
from visualmodules.menu_view import MainMenuView
from gui_game.game_play import IntroWindow
from hunting_animation.hunting_animation import HuntingView
# from random_events import random_events, test_input_variable, more_input, MenuButton, return_to_game



class OregonTrail:
    """ Main application class. """

    def __init__(self, landmarks, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE):
        """ Initializer """

        #window created
        self.window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_TITLE = SCREEN_TITLE
        self._state = "INTRO_WINDOW"
        self.current_location=0
        self.days_traveled=0
        self.miles_traveled=0
        self.changed_view = True
        self.landmarks = landmarks

        view = IntroWindow(SCREEN_WIDTH, SCREEN_HEIGHT,None)
        view.done_handler = self.done_handler
        self.window.show_view(view)

    def done_handler(self, info=None):
        print(info)
        action = info['action']
        source = info['id']
        if source == "opening_menu":
            if action == "begin":
                view = MainMenuView()
                view.done_handler = self.done_handler

        if source == "main_menu":
            if action == "travel":
                view = TraverseTheTrail(self.current_location,0,self.landmarks,self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
                view.done_handler = self.done_handler
                view.days_traveled = self.days_traveled
                view.miles_traveled = self.miles_traveled

            if action == "hunt":
                view = HuntingView()
                view.done_handler = self.done_handler

        if source == "trail_animation":
            if action == 'pause':
                view = MainMenuView()
                view.done_handler = self.done_handler
                self.days_traveled = info["current_day"]
                self.current_location = info["current_location"]
                self.miles_traveled = info["miles_traveled"]
        if source == "hunt":
            view = MainMenuView()
            view.done_handler = self.done_handler


        self.window.show_view(view)
        print(self.current_location)
    
    
            


        

if __name__ == "__main__":

    
    landmark_list = [[6664.0, 'Oregon City'], [5531.200000000001, 'Fort Walla Walla'], [5179.200000000001, 'The Blue Mountains'], [4155.200000000001, 'Fort Boise'], [3483.2000000000007, 'the Snake River crossing'], [2536.0, 'Fort Hall'], [1665.6000000000004, 'Soda Springs'], [974.4000000000005, 'The Green River Crossing'], [-62.399999999999636, 'Fort Bridger'], [-427.1999999999998, 'SouthPass [Butte Mtns]'], [-1080.0, 'Independence Rock'], [-2296.0, 'Fort Laramie'], [-2846.3999999999996, 'Chimney Rock'], [-4446.4, 'Fort Kearny'], [-5208.0, 'the Blue River crossing'], [-5739.2, 'the Kansas River crossing']]
    
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "OREGON TRAIL"
    game = OregonTrail(landmark_list, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run() 
    