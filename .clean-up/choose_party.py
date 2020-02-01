import arcade
from gui_game.game_play import Pages
from visualmodules.button import ActionButton
from gui_game.player_gui import Character

class ChoosePartyView(Pages):
    def __init__(self, width, height, props):
        super().__init__(width, height, props)
        self.wagon_party = []
        self.funds = 0

    def on_show(self):
        # arcade.set_background_color(arcade.color.ANTIQUE_WHITE)

        banker_button = ActionButton(self.center_x - 400, self.center_y, 300, 40, 'Billie Bob the banker', self.button_handler, name='banker')
        carpenter_button = ActionButton(self.center_x, self.center_y, 300, 40, 'Carl the carpenter', self.button_handler, name='carpenter')
        farmer_button = ActionButton(self.center_x + 400, self.center_y, 300, 40, 'Mac the farmer', self.button_handler, name='farmer')

        self.button_list.append(banker_button)
        self.button_list.append(carpenter_button)
        self.button_list.append(farmer_button)

        next_button = ActionButton(self.center_x, self.center_y - 200, 100 , 50,  'next', self.button_handler, name='next')
        self.button_list.append(next_button)

    def on_draw(self):
        arcade.start_render()
        super().on_draw()
        
        arcade.draw_text('Choose wagon party', self.center_x, self.center_y + 150, arcade.color.BLACK, font_size=38, anchor_x='center')

        arcade.draw_text('Jill \nBill \nFred \nAmy', self.center_x - 400, self.center_y - 120, arcade.color.BLACK, font_size=20)
        arcade.draw_text('Travis \nJim \nPhil \nLillie', self.center_x - 35, self.center_y - 120, arcade.color.BLACK, font_size=20)
        arcade.draw_text('Terrell \nMerry \nAshlyn \nPhil', self.center_x + 400, self.center_y - 120, arcade.color.BLACK, font_size=20)

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

