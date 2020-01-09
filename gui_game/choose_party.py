import arcade
from game_play import *
from visualmodules.button import ActionButton

class ChoosePartyView(Pages):
    def __init__(self, width, height, props):
        super().__init__(width, height, props)
        self.wagon_party = []
        self.funds = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.ECRU)
    
        button_list = []

        banker_button = ActionButton(self.center_x - 100, self.center_y + 100, 300, 40, 'Billie Bob the banker', self.button_handler)
        carpenter_button = ActionButton(self.center_x, self.center_y + 100, 300, 40, 'Carl the carpenter', self.button_handle)
        farmer_button = ActionButton(self.center_x + 100, self.center_y + 100, 300, 40, 'Mac the farmer', self.button_handle)

        self.button_list.append(banker_button)
        self.button_list.append(carpenter_button)
        self.button_list.append(farmer_button)

        next_button = ActionButton(self.center_x, self.center_y - 165, 100 , 40,  'next', self.button_handler)
        self.button_list.append(next_button)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text('Choose wagon party', self.center_x, self.center_y + 55, arcade.color.BLACK, font_size=38, anchor_x='center')

    