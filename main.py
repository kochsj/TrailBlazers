from trail_modules.flow.intro_prints import print_the_intro, choose_month_to_depart
from trail_modules.events.shopping import buy_items_from_store

class Game:
    def __init__(self):
        self.party = None #list of party members
        self.day = 1
        self.month = None
        self.bank_roll = 0
        self.inventory = {'Oxen': 0, 'Food': 0, 'Clothing': 0, 'Ammunition': 0, 'Wagon Wheel': 0, 'Wagon Axle': 0, 'Wagon Tongue': 0}
        self.pace = None #['Steady', 'Strenuous', 'Grueling']
        self.rations = None #['filling', 'meager', 'bare-bones]
        self.miles_from_missouri = 0

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
        start = print_the_intro() #prints intro and handles user response
        self.party = start[0] #starting wagon party from print_the_intro
        self.bank_roll = start [1] #starting money from print_the_intro
        self.month = choose_month_to_depart() #asks player to choose month to start and assigns
        shopping_result = buy_items_from_store(self.bank_roll,self.inventory) #opens shop interface, allows user to purchase goods. returns updates to inventory and updates bank_roll
        self.inventory = shopping_result[0] #dict of inventory items
        self.bank_roll = shopping_result[1] #reassigns bank_roll with remaining money after shopping
        self.traverse_the_trail()
    
    def traverse_the_trail(self):
        """
        Controls the movement of the player down the trail
        Player continues down the trail as long as any number of party members are alive
        when there are no more party members - GAME OVER
        when you reach Oregon City - YOU WIN
        """
        while self.party:
            #TODO: incorporate weather / create class(?)
            #TODO: keep track of everyone's health in the party
            # weather = Weather(self.month)
            # health = for member in self.party: grab the health
            menu = f"""Weather: cold
Health: good
Pace: {self.pace}
Rations: {self.rations}

You may:
    1. Continue down the trail.
    2. Check your supplies.
    3. Look at the map.
    4. Change pace.
    5. Change food rations.
    6. Stop to rest.
    7. Attempt to trade.
    8. Go hunting.
    9. Buy supplies.
"""         
            print(menu)
            response = ''
            can_not_proceed = True
            while can_not_proceed:
                while response != '1' and response != '2' and response != '3' and response != '4' and response != '5' and response != '6' and response != '7' and response != '8' and response != '9':
                    response = input('What is your selection?  ')

                if response == "1":
                    #continue on the trail
                    can_not_proceed = False
                if response == "2":
                    #check supplies
                    self.print_inventory()
                    input('Return to continue....')
                    print(menu)
                    response = ''    
                if response == "3":
                    #TODO: check map
                    pass
                if response == "4":
                    #TODO: change pace (determines hours per day)
                    pass
                if response == "5":
                    #TODO: change food rations (determines amount of food per person)
                    pass
                if response == "6":
                    #TODO: stop to rest
                    pass
                if response == "7":
                    #TODO: handle trading
                    pass
                if response == "8":
                    #TODO: handle talking to people
                    pass
                if response == "9":
                    if self.miles_from_missouri == 304 or self.miles_from_missouri == 640 or self.miles_from_missouri == 932 or self.miles_from_missouri == 989 or self.miles_from_missouri == 1295 or self.miles_from_missouri == 1648 or self.miles_from_missouri == 1863:
                        buy_items_from_store(self.bank_roll, self.inventory)
                    else:
                        print('Unfortunately there are no shops nearby.')
                        response = ''
            print('were going down the trail! yay')
        print('GAME OVER')
        exit()
            
    def print_inventory(self):
        inventory = f"""Oxen: {self.inventory['Oxen']}
Food: {self.inventory['Food']}
Clothing: {self.inventory['Clothing']}
Ammunition: {self.inventory['Ammunition']}
Wagon Wheel: {self.inventory['Wagon Wheel']}
Wagon Axle: {self.inventory['Wagon Axle']}
Wagon Tongue: {self.inventory['Wagon Tongue']}
Money left: {self.bank_roll}
"""
        print(inventory)


if __name__ == "__main__":
    game = Game()
    game.play()