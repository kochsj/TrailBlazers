import os
import random
from weather import get_weather
from trail_modules.flow.intro_prints import print_the_intro, choose_month_to_depart, explain_starting_inventory_and_shopping
import time
from trail_modules.events.shopping import buy_items_from_store
from trail_modules.events.hunting import generate_animal
from trail_modules.events.trading import trade_resource
from trail_modules.events.sickness import get_sick, get_well
from trail_modules.events.random_events import random_events
from trail_modules.events.dictionary import talk_to_people


class Game:
    def __init__(self):
        self.party = None #list of party members
        self.day = 1
        self.month = None
        self.year = 1884
        self.bank_roll = 0
        self.inventory = {'Oxen': 0, 'Food': 0, 'Clothing': 0, 'Ammunition': 0, 'Wagon Wheel': 1, 'Wagon Axle': 1, 'Wagon Tongue': 1}
        self.pace = "Steady"
        self.possible_paces = ["Steady", "Strenuous", "Grueling"]
        self.rations = "filling" 
        self.possible_rations = ["filling", 'meager','bare-bones']
        self.miles_from_missouri = 0
        self.year = 1848
        self.weather = (0,0)
        self.location_mileposts_left=[2040,1863,1808,1648,1543,1359,1259,1151,989,932,830,640,554,304,185,102]

###########################################################################################################
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
        self.bank_roll = start[1] #starting money from print_the_intro
        self.month = choose_month_to_depart() #asks player to choose month to start and assigns
        explain_starting_inventory_and_shopping()
        shopping_result = buy_items_from_store(self.bank_roll, self.inventory) #opens shop interface, allows user to purchase goods. returns updates to inventory and updates bank_roll
        self.inventory = shopping_result[0] #dict of inventory items
        self.bank_roll = shopping_result[1] #reassigns bank_roll with remaining money after shopping
        self.traverse_the_trail()

    def increment_day(self):
        cal = [('Jan',31) ('Feb',28) ('Mar',31) ('Arp',30) ('May',31) ('Jun',30) ('Jul',31) ('Aug',31) ('Sep',30) ('Oct',31) ('Nov',30) ('Dec',31)]
        self.day +=1
        # month = 0
        for i in range(len(cal)):
            if cal[i][0] == self.month:
                # month = 1
                if self.day > cal[i][1]:
                    self.day = 1
                    self.month = cal[(i+1)%12][0]
                    if self.month == 'Jan':
                        # month = 0
                        self.year += 1

###########################################################################################################



###########################################################################################################
    def traverse_the_trail(self):
        """
        Controls the movement of the player down the trail
        Player continues down the trail as long as any number of party members are alive
        when there are no more party members - GAME OVER
        when you reach Oregon City - YOU WIN
        """

        while self.party: # while someone is alive still...
            interfacing_with_menu = True

            self.weather = get_weather (self.miles_from_missouri, self.month)
            while interfacing_with_menu:
                menu = self.define_the_menu()
                response = self.print_menu_and_require_new_input(menu)
                while response != '1' and response != '2' and response != '3' and response != '4' and response != '5' and response != '6' and response != '7' and response != '8' and response != '9':
                    response = input('What is your selection?  ')

                if response == "1": #continue on the trail  
                    interfacing_with_menu = False
                    break

                if response == "2": #check supplies
                    self.print_inventory()

                if response == "3": #TODO: check map
                    pass
                    # check the map function - shows a map 

                if response == "4": #set pace
                    res = 0
                    while res != 1 and res != 2 and res !=3:
                        res = int(input ("What pace would you like to set?\n1:  Steady\n2:  Strenuous\n3:  Grueling\n   "))
                    self.pace = self.possible_paces[res-1]

                if response == "5": #set rations
                    res = 0
                    while res != 1 and res != 2 and res !=3:
                        res = int(input ("What rations would you like to set?\n1:  filling\n2:  meager\n3:  bare-bones\n   "))
                    self.rations = self.possible_rations[res-1]
 
                if response == "6": #stop to rest
                    self.rest()

                if response == "7": #handle trading
                    self.print_inventory()
                    inventory_after_trading = trade_resource(self.inventory)
                    self.inventory = inventory_after_trading
                    #TODO: handle days
                    # self.increment_day()
                    

                if response == "8": #handle hunting
                    os.system('clear')
                    if game.inventory["Ammunition"] >= 1:
                        generate_animal(game)
                    else:

                        print('You have no Ammunition')
                    time.sleep(1)
                    response = self.print_menu_and_require_new_input(menu)


                if response == "9":
                    if self.miles_from_missouri == 0 or self.miles_from_missouri == 304 or self.miles_from_missouri == 640 or self.miles_from_missouri == 932 or self.miles_from_missouri == 989 or self.miles_from_missouri == 1295 or self.miles_from_missouri == 1648 or self.miles_from_missouri == 1863:
                        buy_items_from_store(self.bank_roll, self.inventory)

                    else:
                        input('Unfortunately there are no shops nearby.')
                response = self.print_menu_and_require_new_input(menu)

            self.travel_for_one_day()

        input('GAME OVER')
        exit()

        
            
###########################################################################################################



###########################################################################################################
    def print_inventory(self):
        inventory = f"""Current Inventory of Supplies:
Oxen: {self.inventory['Oxen']}
Food: {self.inventory['Food']}
Clothing: {self.inventory['Clothing']}
Ammunition: {self.inventory['Ammunition']}
Wagon Wheel: {self.inventory['Wagon Wheel']}
Wagon Axle: {self.inventory['Wagon Axle']}
Wagon Tongue: {self.inventory['Wagon Tongue']}
Money left: {self.bank_roll}
"""
        os.system('clear')
        print(inventory)
        input('Return to continue....')

###########################################################################################################



###########################################################################################################
    def rest(self):
        """heals up to 20 health per party member, and gives them a 20% chance of recovering from a disease"""
        for party_member in self.party:
            party_member.health += 20
            if party_member.health > 100: party_member.health = 100
            if party_member.sick:
                healed = 0.2 > random.uniform(0, 1)
                if healed : get_well(party_member)
        self.consume_rations()
        #TODO: incriment days
        # self.increment_day()

###########################################################################################################



###########################################################################################################

    def travel_for_one_day(self):
        ####
        #  Travel Miles, and update illnesses based on pace#
        ###
        if self.inventory["Wagon Wheel"] <1 or self.inventory["Wagon Axle"] <1 or self.inventory["Wagon Tongue"] <1:
            input ("You can't move until you repair your wagon.  Try trading for the part you need or buying one in a store (press enter to continue)")
            return
        #TODO: handle days
        # self.increment_day()
        miles = 0
        chance_of_illness = 0
        chance_of_recovery = 0.1
        ## adjust chance of illness due to wagon pace
        if self.pace == 'Steady' : 
            miles = 8
            chance_of_illness = 0.01
        if self.pace == 'Strenuous' : 
            miles = 12
            chance_of_illness = 0.02
        if self.pace == 'Grueling' :
            miles = 16
            chance_of_illness = 0.05
        self.miles_from_missouri += miles  # travel miles
        for party_member in self.party: # see if anyone gets sick or recovers from illness
            if party_member.sick:
                num = random.uniform(0, 1)
                if num < chance_of_recovery: get_well(party_member)
            num = random.uniform(0, 1)
            if num < chance_of_illness: get_sick(party_member)           
        self.consume_rations()

        next_milepost = self.location_mileposts_left.pop()
        if next_milepost <= self.miles_from_missouri: ###  If you've passed a landmark, be sure to stop at it!
            self.miles_from_missouri = next_milepost
            self.talk_to_strangers()
        else: 
            self.location_mileposts_left.append(next_milepost)
            random_events(self)

###########################################################################################################



###########################################################################################################
    def consume_rations(self):
        if self.inventory["Food"] == 0:
            party_member = random.choice(self.party)
            get_sick(party_member)
        for party_member in self.party:
            if self.rations == 'filling':
                self.inventory["Food"] -= 5
            elif self.rations == "meager":
                self.inventory["Food"] -= 3
                if party_member.health > 60: party_member.health -= 3
            elif self.rations == "bare-bones":
                self.inventory["Food"] -= 2
                if party_member.health > 40: party_member.health -= 3
            if self.inventory["Food"] < 0:
                self.inventory["Food"] = 0

    
###########################################################################################################
    def talk_to_strangers(self):
        """ Prompts an option to talk to the locals and learn more facts about the landmark, river crossing, or outpost you have reached"""

        print('You come across a friendly stranger at this stop. Do you want to talk to them?')
        response = input('y/n?  ')
        mile_post = (self.miles_from_missouri)
        if mile_post in  talk_to_people('talking_dictionary') and response == 'y' :
            print(talk_to_people('talking_dictionary')[mile_post])
            input('Return to continue....')
        else:
            print('Alrighty then, safe travels!')
            


###########################################################################################################
    def print_menu_and_require_new_input(self, menu):
        """
        "re"-prints the menu
        returns a null string for response, to restart prompts from menu.
        """
        os.system('clear')
        print(menu)
        return ''
###########################################################################################################
    def define_the_menu(self):
        def return_health_data_for_menu(party):
            party_health_string = '\n'
            for party_member in party:
                party_health_string += party_member.return_health_status_report()
                party_health_string += '\n'
            return party_health_string[:-1]

        health_string = return_health_data_for_menu(self.party)
        menu = f"""{self.month} {self.day}, {self.year}
Today's low temperature: {self.weather[0]}
Today's high temperature: {self.weather[1]}
Health: {health_string}
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
        return menu

    
if __name__ == "__main__":
    game = Game()
    game.play()



