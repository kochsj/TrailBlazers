import arcade
from gui_game.button import ActionButton

class LearnMore(arcade.View):
    """
    View that asks player to choose a starting leader
    # Returns a tuple of (the name of the leader, and the starting_funds (based on leader's profession))
    """
    def on_show(self): #to set up view
        def finish_learning(btn):
            self.done_handler({"id":"opening_menu","action":"finish_learning"})

        button = ActionButton(finish_learning, 700, 200,200,50,"Return to Menu",20,"Arial",arcade.color.WHITE)
        self.button_list.append(button)


    def on_draw(self): #drawn continuously
        
        arcade.start_render()
        arcade.draw_text("You\'re about to begin a great adventure, traveling the Oregon Trail.",180, 725, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("Your party of 5, in a covered wagon pulled by a team of oxen, will",180, 700, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("travel from Independence, Missouri, to Oregon City, Oregon -- a",180, 675, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("journey of approximately 2,040 miles, across plains, rivers, and",180, 650, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("mountains. Along the way you will face obstacles, like crossing rivers,",180, 625, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("bad weather, lack of food, illnesses.  How you over come these challenges",180, 600, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("are based on the decisions you make, if you choose wisely you will make",180, 575, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("it all the way to Oregon",180, 550, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("This trail was used by hundreds of thousands of American pioneers",180, 475, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("in the mid-1800s to emigrate west. It was a long and dangerous",180, 450, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("journey that went through Missouri, Kansas, Nebraska, Wyoming, Idaho",180, 425, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("and finally into Oregon. Without the Oregon Trail and the passing of",180, 400, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("the Oregon Donation Land Act in 1850, which encouraged settlement in",180, 375, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("the Oregon Territory, American pioneers would have been slower to settle",180, 350, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        arcade.draw_text("the American West in the 19th century.",180, 325, arcade.color.WHITE, 20, width=1000, align="center",bold=True)
        super().on_draw()