from trail_modules.flow.prints import print_the_intro
from trail_modules.flow.player import character_creation

class Game:
    def __init__(self):
        self.party = None #list of party members
        self.day = 1
        self.month = "March"

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
        


if __name__ == "__main__":
    game = Game()
    game.play()