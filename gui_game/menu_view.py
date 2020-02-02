import arcade
from gui_game.button import ActionButton

class MainMenuView(arcade.View):

    def on_show(self): #like setup
        def travel(btn):
            self.done_handler({"id":"main_menu","action":"travel"})
        def check(btn):print('check')
        def look(btn):print('Look')
        def pace(btn):
            self.done_handler({"id":"main_menu","action":"pace"})
        def rations(btn):
            self.done_handler({"id":"main_menu","action":"rations"})
        def rest(btn):print('rest')
        def trade(btn):print('trade')
        def hunt(btn):
            self.done_handler({"id": "main_menu", "action": "hunt"})
        def buy(btn):print('buy')
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

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Main Menu",200, 600, arcade.color.BLACK, 40, width=1000, align="center",bold=True)
        
        super().on_draw() 

