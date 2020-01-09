import arcade
from button import ActionButton

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Oregon Trail"

class MainMenuView(arcade.View):

    def on_draw(self):
        arcade.start_render()
        # menu_items = ["Travel the Trail","Check Supplies", "Look at map", "Change Pace","Change Rations","Stop to Rest", "Attempt to trade", "Hunt", "Buy Supplies"]

        # l = len(menu_items)
        # for i in range(l):
        #     arcade.draw_text(menu_items[l-(i+1)],600,100+50*i,arcade.color.WHITE,25,)
        arcade.draw_text("Main Menu",200, 600, arcade.color.WHITE, 40, width=1000, align="center",bold=True)
        
        super().on_draw()

    def on_show(self):
        def travel():print('Traveled the Trail')
        def check():print('check')
        def look():print('Look')
        def pace():print('Pace')
        def rations():print('rations')
        def rest():print('rest')
        def trade():print('trade')
        def hunt():print('hunt')
        def buy():print('buy')
        menu_actions = [travel,check,look,pace,rations,rest,trade,hunt,buy]
        menu_items = ["Travel the Trail","Check Supplies", "Look at map", "Change Pace","Change Rations","Stop to Rest", "Attempt to trade", "Hunt", "Buy Supplies"]
        l=len(menu_actions)
        shift = 40
        for i in range (l-5):
            button = ActionButton(menu_actions[l-i-1],900 + shift,(180+80*i),300,50,menu_items[l-i-1],30,"Arial",arcade.color.WHITE)
            self.button_list.append(button)
        for i in range (l-5,l-1):
            button = ActionButton(menu_actions[l-i-1],450 + shift,(-140+80*i),300,50,menu_items[l-i-1],30,"Arial",arcade.color.WHITE)
            self.button_list.append(button)
        button = ActionButton(menu_actions[0],675 + shift,(500),300,50,menu_items[0],30,"Arial",arcade.color.WHITE)
        self.button_list.append(button)
        
    
        


#         button = ActionButton(leaving,700,100,400,50,"Exit Store",30,"Arial",arcade.color.WHITE)
#         self.button_list.append(button)
        


def main():
    MainMenuView(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    SCREEN_TITLE = "Main Menu"
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = MainMenuView()

    window.show_view(view)
    arcade.run()

