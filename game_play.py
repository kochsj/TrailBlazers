import arcade
from s
class test_game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(600, 400)

        arcade.set_background_color(arcade.color.RED)

        self.background_list = None

        self.setup()

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

    def on_update(self, delta_time):
        pass

    def game_intro(self):
        

def main():
    """ Main method """
    window = test_game(600, 400, 'test')
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()