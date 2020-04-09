import arcade
# from arcade.gui import *
from gui_game.trail_animation.trail_animation import TraverseTheTrail
from gui_game.menu_view import MainMenuView
from gui_game.store_view import StoreView
from gui_game.departure_view import DepartureView
from gui_game.intro_window import IntroView
from gui_game.learn_more import LearnMore
from gui_game.hunting_animation.hunting_animation import HuntingView
from gui_game.character_creation_view import CharacterCreationView, BankerView, CarpenterView, FarmerView
from gui_game.general_store_view import SuppliesExplainationView, BuyingAnItemView, FinalTransactionView
from gui_game.pace_view import PaceView
from gui_game.rations_view import RationsView
# from random_events import random_events, test_input_variable, more_input, MenuButton, return_to_game



class OregonTrail:
    """ Main application class. """

    def __init__(self, landmarks, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fs):
        """ Initializer """

        #window created
        self.window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=fs)
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_TITLE = SCREEN_TITLE

        #game attributes to track distance/days from missouri
        self.current_location=0
        self.days_traveled=0
        self.miles_traveled=0
        self.landmarks = landmarks

        #game attributes that track player attributes/status
        self.party = None #list of party members
        self.day = 1
        self.month = None
        self.year = 1848
        self.bank_roll = 0
        self.inventory = {'Oxen': 0, 'Food': 0, 'Clothing': 0, 'Ammunition': 0, 'Wagon Wheel': 1, 'Wagon Axle': 1, 'Wagon Tongue': 1}
        self.pace = 0
        self.rations = "filling"

        #Initializes window with into screen view
        view = IntroView()
        view.done_handler = self.done_handler
        arcade.set_background_color(arcade.color.BLACK)
        self.window.show_view(view)

    def done_handler(self, info=None):
        action = info['action']
        source = info['id']
        if source == "opening_menu":
            if action == "begin":
                view = CharacterCreationView()
                view.done_handler = self.done_handler
            if action == "decide_month":
                self.month = info['month']
                view = SuppliesExplainationView()
                view.done_handler = self.done_handler
            if action == "learn_more":
                view = LearnMore()
                view.done_handler = self.done_handler
            if action == "finish_learning":
                view = IntroView()
                view.done_handler = self.done_handler

        if source == "char_creation":
            if action == "banker":
                self.bank_roll = info["starting_funds"]
                self.party = []
                view = BankerView()
                view.done_handler = self.done_handler
            if action == "carpenter":
                self.bank_roll = info["starting_funds"]
                self.party = []
                view = CarpenterView()
                view.done_handler = self.done_handler
            if action == "farmer":
                self.bank_roll = info["starting_funds"]
                self.party = []
                view = FarmerView()
                view.done_handler = self.done_handler
            if action == "finish_creation":
                view = DepartureView()
                view.done_handler = self.done_handler

        if source == "general_store":
            if action == "go_to_store":
                view = StoreView(self.inventory, self.bank_roll)
                view.done_handler = self.done_handler
            if action == "buy_oxen":
                view = BuyingAnItemView('Oxen', 0, self.bank_roll)
                view.done_handler = self.done_handler
            if action == "buy_food":
                view = BuyingAnItemView('Food', 1, self.bank_roll)
                view.done_handler = self.done_handler
            if action == "buy_clothing":
                view = BuyingAnItemView('Clothing', 2, self.bank_roll)
                view.done_handler = self.done_handler
            if action == "buy_ammo":
                view = BuyingAnItemView('Ammunition', 3, self.bank_roll)
                view.done_handler = self.done_handler
            if action == "buy_wheel":
                view = BuyingAnItemView('Wagon Wheel', 4, self.bank_roll)
                view.done_handler = self.done_handler
            if action == "buy_axle":
                view = BuyingAnItemView('Wagon Axle', 5, self.bank_roll)
                view.done_handler = self.done_handler
            if action == "buy_tongue":
                view = BuyingAnItemView('Wagon Tongue', 6, self.bank_roll)
                view.done_handler = self.done_handler
            if action == "finish_transaction":
                self.inventory[info['item']] += info['quantity']
                self.bank_roll -= info['cost']
                view = FinalTransactionView(info['item'], info['quantity'], info['cost'])
                view.done_handler = self.done_handler
            if action == "head_to_trail":
                view = view = TraverseTheTrail(self.current_location,self.pace,self.landmarks,self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
                view.done_handler = self.done_handler
                view.days_traveled = self.days_traveled
                view.miles_traveled = self.miles_traveled

        if source == "main_menu":
            if action == "travel":
                view = TraverseTheTrail(self.current_location,self.pace,self.landmarks,self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
                view.done_handler = self.done_handler
                view.days_traveled = self.days_traveled
                view.miles_traveled = self.miles_traveled

            if action == "hunt":
                view = HuntingView()
                view.done_handler = self.done_handler

            if action == "pace":
                view = PaceView()
                view.done_handler = self.done_handler

            if action == "rations":
                view = RationsView()
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

        if source == "pace_view":
            if action == "steady":
                self.pace = info["pace"]
            if action == "strenuous":
                self.pace = info["pace"]
            if action == "grueling":
                self.pace = info["pace"]
            view = MainMenuView()
            view.done_handler = self.done_handler

        if source == "rations_view":
            if action == "filling":
                self.rations = info["rations"]
            if action == "meager":
                self.rations = info["rations"]
            if action == "bare":
                self.rations = info["rations"]
            print("rations :", self.rations)
            view = MainMenuView()
            view.done_handler = self.done_handler

        self.window.show_view(view)

if __name__ == "__main__":

    landmark_list = [[6664.0, 'Oregon City'], [5531.200000000001, 'Fort Walla Walla'], [5179.200000000001, 'The Blue Mountains'], [4155.200000000001, 'Fort Boise'], [3483.2000000000007, 'the Snake River crossing'], [2536.0, 'Fort Hall'], [1665.6000000000004, 'Soda Springs'], [974.4000000000005, 'The Green River Crossing'], [-62.399999999999636, 'Fort Bridger'], [-427.1999999999998, 'SouthPass [Butte Mtns]'], [-1080.0, 'Independence Rock'], [-2296.0, 'Fort Laramie'], [-2846.3999999999996, 'Chimney Rock'], [-4446.4, 'Fort Kearny'], [-5208.0, 'the Blue River crossing'], [-5739.2, 'the Kansas River crossing']]
    
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "OREGON TRAIL"

    # TODO: added this temporarily
    # Full-Screen looks weird on hi-res monitors && good on low-res
    response = input('Do you want to run in FullScreen mode? (y/n)')
    while response:
        if response == 'y':
            game = OregonTrail(landmark_list, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, True)
            break
        if response == 'n':
            game = OregonTrail(landmark_list, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, False)
            break
        response = input('Do you want to run in FullScreen mode? (y/n)')
         
    arcade.run() 
    