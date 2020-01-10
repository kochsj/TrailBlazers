
import arcade
from gui_game.test_module import BaseView

class TestView(arcade.View):
    def on_show(self):
        btn = arcade.TextButton(100,100,200,50,'Button')
        self.button_list.append(btn)