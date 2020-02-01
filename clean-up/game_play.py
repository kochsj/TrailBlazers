import arcade
# from main import Game
from visualmodules.button import ActionButton
# from gui_game.player_gui import Character
# import gui_game.player_gui as char 

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Trail_Blazers Oregon Trail'


class Pages(arcade.View):
    def __init__(self, width, height, props):
        super().__init__()
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.state = {'wagon_party' : None ,'funds' : None}
        self.props = {}

        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)


    def button_handler(self, button):
        self.props['done_handler']()

    def on_draw(self):
        super().on_draw()
        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
    
    def quit_game(self):
        arcade.close_window()


class IntroWindow(Pages):

    background = arcade.load_texture('./img/intro_background.png')

    def on_show(self):

        travel_trail_button = ActionButton(self.button_handler, self.center_x, self.center_y, 300, 40, 'Travel the trail', name='travel_trail_button', font_color=arcade.color.WHITE)
        learn_more = ActionButton(self.button_handler, self.center_x, self.center_y - 55, 300, 40, 'learn more', name='learn_more', font_color=arcade.color.WHITE)
        quit_button = ActionButton(self.button_handler, self.center_x, self.center_y - 110, 100, 40, 'Quit', name='quit', font_color=arcade.color.WHITE)

        self.button_list.append(travel_trail_button)
        self.button_list.append(learn_more)
        self.button_list.append(quit_button)

    def button_handler(self, button):
        if button.name == 'travel_trail_button':
            travel_trail = ChoosePartyView(self.center_x, self.center_y, 'Profession')
            self.window.show_view(travel_trail)
            self.done_handler({"id":"opening_menu","action":"begin"})

        elif button.name == 'learn_more':
            learn_more = LearnMore(self.center_x, self.center_y, 'learn more')
            self.window.show_view(learn_more)
            # self.props['done_hanler']()

        elif button.name == 'quit':
            arcade.close_window()


    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(self.center_x, self.center_y,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        super().on_draw()

    
class LearnMore(Pages):
    pass



class ChoosePartyView(Pages):
    def __init__(self, width, height, props):
        super().__init__(width, height, props)
        self.wagon_party = []
        self.funds = 0

    def on_show(self):

        banker_button = ActionButton( self.button_handler,self.center_x - 400, self.center_y, 300, 40, 'Billie Bob the banker', self.button_handler, name='banker')
        carpenter_button = ActionButton( self.button_handler,self.center_x, self.center_y, 300, 40, 'Carl the carpenter', self.button_handler, name='carpenter')
        farmer_button = ActionButton( self.button_handler,self.center_x + 400, self.center_y, 300, 40, 'Mac the farmer', self.button_handler, name='farmer')

        self.button_list.append(banker_button)
        self.button_list.append(carpenter_button)
        self.button_list.append(farmer_button)

        next_button = ActionButton(self.center_x, self.center_y - 200, 100 , 50,  'next', self.button_handler, name='next')
        self.button_list.append(next_button)

    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_text('Choose wagon party', self.center_x, self.center_y + 150, arcade.color.BLACK, font_size=38, anchor_x='center')

        arcade.draw_text('Jill \nBill \nFred \nAmy', self.center_x - 400, self.center_y - 120, arcade.color.BLACK, font_size=20)
        arcade.draw_text('Travis \nJim \nPhil \nLillie', self.center_x - 35, self.center_y - 120, arcade.color.BLACK, font_size=20)
        arcade.draw_text('Terrell \nMerry \nAshlyn \nPhil', self.center_x + 400, self.center_y - 120, arcade.color.BLACK, font_size=20)
        super().on_draw()

    def button_handler(self, button):
        if button.name == 'next':
            self.props['done_handler'](self.wagon_party, self.funds)
            print(self.wagon_party, self.funds)

        elif button.name == 'banker':
            self.funds = 1600
            self.wagon_party = [Character('Chris') ,Character('Jill'), Character('Bill'), Character('Fred'), Character('Amy')]

        elif button.name == 'carpenter':
            self.funds = 1600
            self.wagon_party = [Character('Ting'), Character('Travis'), Character('Jim'), Character('Phil'), Character('Lillie')]
        
        elif button.name == 'farmer':
            self.funds = 1600
            self.wagon_party = [Character('Stephen'), Character('Terrel'), Character('Merry'), Character('Ashlyn'), Character('Phil')]




# def start_game():
#     """ Main method """
#     window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#     intro_view = IntroWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#     window.show_view(intro_view)
#     arcade.run()


# if __name__ == "__main__":
#     start_game()
