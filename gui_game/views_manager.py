import arcade
import game_play

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

if __name__ == '__main__':
    game = Views()
    game.start()
