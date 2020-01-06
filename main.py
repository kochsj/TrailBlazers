from trail_modules.flow.intro_prints import print_the_intro, choose_month_to_depart

class Game:
    def __init__(self):
        self.party = None #list of party members
        self.day = 1
        self.month = None

    def play(self):
        """
        print the intro
        create the char
        set departure date
        buy the stuff
        set out on the trail (while alive: )       
            encounter random events
            encounter set locations
            hunting
            river crossing
            trading
            talking
            weather
            status (health, days, miles, money, food, pace)
        """
        self.party = print_the_intro()
        self.month = choose_month_to_depart()
        print(self.month)


if __name__ == "__main__":
    game = Game()
    game.play()