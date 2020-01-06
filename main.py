from trail_modules.flow.intro_prints import print_the_intro, choose_month_to_depart

class Game:
    def __init__(self):
        self.party = None #list of party members
        self.day = 1
        self.month = None
        self.bank_roll = None
        self.inventory = {}

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
        start = print_the_intro()
        self.party = start[0]
        self.bank_roll = start [1]
        self.month = choose_month_to_depart()
        print(f'bank roll: {self.bank_roll}')
        print(f'party {self.party[0].health}')


if __name__ == "__main__":
    game = Game()
    game.play()