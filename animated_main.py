import arcade
from arcade.gui import *
from trail_animation.trail_animation import TraverseTheTrail
from visualmodules.menu_view import MainMenuView
# from random_events import random_events, test_input_variable, more_input, MenuButton, return_to_game



class OregonTrail(arcade.Window):
    """ Main application class. """

    def __init__(self, landmarks, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self._state = "INTRO_WINDOW"

        self.party = None #list of party members
        self.day = 1
        self.month = None
        self.year = 1884
        self.bank_roll = 0
        self.inventory = {'Oxen': 0, 'Food': 0, 'Clothing': 0, 'Ammunition': 0, 'Wagon Wheel': 1, 'Wagon Axle': 1, 'Wagon Tongue': 1}
        self.pace = "Steady"
        self.possible_paces = ["Steady", "Strenuous", "Grueling"]
        self.rations = "filling" 
        self.possible_rations = ["filling", 'meager','bare-bones']
        self.miles_from_missouri = 0
        self.year = 1848
        self.weather = (0,0)
        self.location_mileposts_left=[(2040,"the Barlow road"),(1863,"Fort Walla Walla"),(1808,"the Grande Ronde valley"),(1648,"Fort Boise"),(1543,"the Snake river crossing"),(1359,"Fort Hall"),(1259,"Soda Springs"),(1151,"the Green river crossing"),(989,"Fort Bridger"),(932,"South Pass (Butte mountains)"),(830, "Independence Rock"),(640,"Fort Laramie"),(554,"Chimney Rock"),(304,"Fort Kearny"),(185,"the Blue river crossing"),(102, "the Kansas river crossing"),(0,"Independece Missouri")]
        self.landmarks = landmarks
        self.menu = None

        self.changed_view = True

        # Setup
        self.trail = None

        

    def setup(self):
        """ Set up the game and initialize the variables. """
        # self.trail = TraverseTheTrail(0,2, self.landmarks, self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # self.trail.setup()
        self.menu = MainMenuView()
        print("setup")
        
    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()
        # print(self.changed_view)

        # if self.changed_view == True: 
        #     self.changed_view = False
        #     if self._state == "INTRO_WINDOW":
        #         # view = MainMenuView()
        #         self.show_view(self.menu)
        #         print(self.menu)
                

 

    def on_mouse_press(self, x, y, button, modifiers):
        """
        """
        pass

    def on_key_press(self, key, modifiers):
        """
        """
        pass

    def on_update(self, delta_time):
        """ Movement and game logic """
        pass


if __name__ == "__main__":

    
    landmark_list = [[2040,"Oregon City"],[1863,"Fort Walla Walla"],[1808,"The Blue Mountains"],[1648,"Fort Boise"],[1543,"the Snake River crossing"],[1395,"Fort Hall"],[1259,"Soda Springs"],[1151,"The Green River Crossing"],[989,"Fort Bridger"],[932,"South Pass [Butte Mtns]"],[830,"Independence Rock"],[640,"Fort Laramie"],[554,"Chimney Rock"],[304,"Fort Kearny"],[185,"the Blue River crossing"],[102, "the Kansas River crossing"]]
    
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "OREGON TRAIL"
    game = OregonTrail(landmark_list, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # game.setup()
    # window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = MainMenuView()
    game.show_view(view)
    # props = {"done_handler": miles_traveled, "random_event": random_events, "input_var": (test_input_variable, more_input), "menu_func": return_to_game} # dictionary of a pointer to function in memory
    # game.props = props # add the dictionary to the game as attribute 'props'
    
    arcade.run() 