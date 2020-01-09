import arcade
from main import Game
from visualmodules.button import *
import gui_game.player_gui as char 

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Trail_Blazers Oregon Trail'


class Pages(arcade.View):
    def __init__(self, width, height, title):
        super().__init__()
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.state = {'wagon_party' : None ,'funds' : None}

        self.text = ''

    background = arcade.load_texture('./img/intro_background.png')

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.center_x, self.center_y, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.ECRU)
        # arcade.draw_texture_rectangle(
        #     SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.25,
        #                              SCREEN_WIDTH // 1.25, SCREEN_HEIGHT // 1.75, arcade.color.BLACK)
        # for button in self.button_list:
        #     button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        check_mouse_release_for_buttons(x, y, self.button_list)

    
    def quit_game(self):
        arcade.close_window()

    
    def rechoose_party(self):
        choose_party = ChooseParty(self.center_x, self.center_y, 'show party')
        self.window.show_view(choose_party)


class IntroWindow(Pages):

    background = arcade.load_texture('./img/intro_background.png')

    def on_show(self):

        profession_button = ProfessionButton(
            self.center_x, self.center_y, self.choose_profession)
        self.button_list.append(profession_button)

        learn_button = LearnTextButton(
            self.center_x, self.center_y - 55, self.learn_more)
        self.button_list.append(learn_button)

        quit_button = QuitTextButton(
            self.center_x, self.center_y - 110, self.quit_game)
        self.button_list.append(quit_button)

    def choose_profession(self):
        travel_trail = ChooseParty(self.center_x, self.center_y, 'Profession')
        self.window.show_view(travel_trail)

    def learn_more(self):
        learn_more = LearnMore(self.center_x, self.center_y, 'learn more')
        self.window.show_view(learn_more)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.center_x, self.center_y,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # super().on_draw()
        for button in self.button_list:
            button.on_draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        check_mouse_release_for_buttons(x, y, self.button_list)


class ChooseParty(Pages):

    def on_show(self):
        self.button_list = []
        for button in self.button_list:
            button.on_draw()

        banker_button = BankerButton(self.center_x, self.center_y, self.banker_party)
        self.button_list.append(banker_button)

        carpenter_button = CarpenterButton(self.center_x, self.center_y - 55, self.charpenter_party)
        self.button_list.append(carpenter_button)

        farmer_button = FarmerButton(self.center_x, self.center_y - 110, self.farmer_party)
        self.button_list.append(farmer_button)

        quit_button = QuitTextButton(self.center_x, self.center_y - 165, self.quit_game)
        self.button_list.append(quit_button)

    def banker_party(self):
        banker = char.Banker()
        banker_party = banker.wagon_party
        wagon_party = [member.__dict__['name'] for member in banker_party]
        wagon_party.append(banker.name)
        self.state['wagon_party']= wagon_party
        self.state['funds']= banker.funds
        self.rechoose_party()


    def charpenter_party(self):
        charpenter = char.Carpenter()
        charpenter_party = charpenter.wagon_party
        wagon_party = [member.__dict__['name'] for member in charpenter_party]
        wagon_party.append(charpenter.name)
        self.state['wagon_party']= wagon_party
        self.state['funds']= charpenter.funds
        self.rechoose_party()

    def farmer_party(self):
        farmer = char.Farmer()
        farmer_party = farmer.wagon_party
        wagon_party = [memeber.__dict__['name'] for memeber in farmer_party]
        wagon_party.append(farmer.name)
        self.state['wagon_party']= wagon_party
        self.state['funds']= farmer.funds
        self.rechoose_party()

class ShowParty(Pages):

    def on_show(self):
        self.button_list = []
        for button in self.button_list:
            button.on_draw()

        banker_button = BankerButton(self.center_x, self.center_y, self.banker_party)
        self.button_list.append(banker_button)

        carpenter_button = CarpenterButton(self.center_x, self.center_y - 55, self.charpenter_party)
        self.button_list.append(carpenter_button)

        farmer_button = FarmerButton(self.center_x, self.center_y - 110, self.farmer_party)
        self.button_list.append(farmer_button)

        quit_button = QuitTextButton(self.center_x, self.center_y - 165, self.quit_game)
        self.button_list.append(quit_button)

    def banker_party(self):
        banker = char.Banker()
        banker_party = banker.wagon_party
        wagon_party = [member.__dict__['name'] for member in banker_party]
        wagon_party.append(banker.name)
        self.state['wagon_party']= wagon_party
        self.state['funds']= banker.funds
        print('we made it')
        self.rechoose_party()



    def charpenter_party(self):
        charpenter = char.Carpenter()
        charpenter_party = charpenter.wagon_party
        wagon_party = [member.__dict__['name'] for member in charpenter_party]
        wagon_party.append(charpenter.name)
        self.state['wagon_party']= wagon_party
        self.state['funds']= charpenter.funds
        self.rechoose_party()


    def farmer_party(self):
        farmer = char.Farmer()
        farmer_party = farmer.wagon_party
        wagon_party = [memeber.__dict__['name'] for memeber in farmer_party]
        wagon_party.append(farmer.name)
        self.state['wagon_party']= wagon_party
        self.state['funds']= farmer.funds
        self.rechoose_party()


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Your party is: ', (self.center_x + 50), self.center_y, arcade.color.BLACK, font_size=20, anchor_x='right')
        travelers = self.state['wagon_party']
        travelers = [travelers.name for traveler in travelers]
        print('hello', travelers)
        arcade.draw_text(f"{', '.join(travelers)}", self.center_x + 50, self.center_y - 40, arcade.color.BLACK, anchor_x='right')
        super().on_draw()
    # def chose_profession(self):
    #     travel_trail = TravelTrail(self.center_x, self.center_y, 'Profession')
    #     self.window.show_view(travel_trail)



    # def character_creation(self):

    #     self.button_list = []

    #     wagon_party = []
    #     bank_roll = None

        # banker_button = BankerButton(self.center_x, self.center_y, self.banker)
        # self.button_list.append(banker_button)

        # def banker_char(self, wagon):
        #     banker = 'billie bob'
        #     wagon_party.append(banker)
        #     starting_funds = 1600
        #     bank_roll.append(starting_funds)
        #     banker = Banker()
        #     Game.party.append(banker)
        #     add_to_party = AddPartyMembers(SCREEN_WIDTH, SCREEN_HEIGHT, 'Add memebers to Party')
        #     self.window.show_view(add_to_party)

        # def charpenter_char(self):
        #     pass

    # def add_dialog_box(self):
    #     dialogobx = arcade.gui.DialogueBox()

    # def setup(self):
    #     self.add_dialog_box

    # def set_button(self, button_center_spacing, button_center_vertical_spacing, banker):
    #     self.button_list.append(BankerButton(button_center_spacing, button_center_vertical_spacing, banker))

    # def on_show(self):
    #     add_dialog_box()
    #     setup()
    #     set_button()


class LearnMore(Pages):
    pass


class AddPartyMembers(Pages):
    pass


def start_game():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    intro_view = IntroWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.show_view(intro_view)
    arcade.run()


if __name__ == "__main__":
    start_game()
