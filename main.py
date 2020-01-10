import os
import random
from termcolor import colored
from weather import get_weather
from trail_modules.flow.intro_prints import print_the_intro, choose_month_to_depart, explain_starting_inventory_and_shopping
from trail_modules.events.shopping import buy_items_from_store
from trail_modules.events.hunting import generate_animal
from trail_modules.events.trading import trade_resource
from trail_modules.events.sickness import get_sick, get_well
from trail_modules.events.random_events import random_events
from trail_modules.events.dictionary import talk_to_people
from trail_modules.events.river_raft import cross
from trail_modules.events.map import check_map


class Game:
    def __init__(self):
        self.party = None #list of party members
        self.day = 1
        self.month = None
        self.year = 1848
        self.bank_roll = 0
        self.inventory = {'Oxen': 0, 'Food': 0, 'Clothing': 0, 'Ammunition': 0, 'Wagon Wheel': 1, 'Wagon Axle': 1, 'Wagon Tongue': 1}
        self.pace = "Steady"
        self.possible_paces = ["Steady", "Strenuous", "Grueling"]
        self.rations = "filling" 
        self.possible_rations = ["filling", 'meager','bare-bones']
        self.miles_from_missouri = 0
        self.weather = (0,0)
        self.location_mileposts_left=[(2040,"the Barlow road"),(1863,"Fort Walla Walla"),(1808,"the Grande Ronde valley"),(1648,"Fort Boise"),(1543,"the Snake river crossing"),(1359,"Fort Hall"),(1259,"Soda Springs"),(1151,"the Green river crossing"),(989,"Fort Bridger"),(932,"South Pass (Butte mountains)"),(830, "Independence Rock"),(640,"Fort Laramie"),(554,"Chimney Rock"),(304,"Fort Kearny"),(185,"the Blue river crossing"),(102, "the Kansas river crossing"),(0,"Independece Missouri")]

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

###########################################################################################################



###########################################################################################################
    def increment_day(self):
        """moves us 1 day ahead on the calender.  Also eats food and and updates the daily weather.  no return."""
        cal = [('January',31), ('February',28), ('March',31), ('April',30), ('May',31), ('June',30), ('July',31), ('August',31), ('September',30), ('October',31), ('November',30), ('December',31)]
        self.day +=1
        month = 0
        for i in range(len(cal)):
            if cal[i][0] == self.month:
                month = i
        if self.day > cal[month][1]:
            self.day = 1
            self.month = cal[(month+1)%12][0]
            if self.month == 'January':
                self.year += 1
        self.consume_rations()
        self.weather = get_weather (self.miles_from_missouri, self.month)
        output = ""
        i = 0
        for player in self.party:
            if player.health < 1:
                self.party.pop(i)
                disease = ''
                if player.sick: 
                    disease = player.sick[0]
                else:
                    disease = "exhaustion"
                output += f"\nObituary alert!!! {player.name} has died of {disease}.\n"
            i+=1
        if output : input (colored(output, 'red'))


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
            while interfacing_with_menu:
                crossing_a_river=False
                menu = self.define_the_menu()
                response = self.print_menu_and_require_new_input(menu)
                while response != '1' and response != '2' and response != '3' and response != '4' and response != '5' and response != '6' and response != '7' and response != '8' and response != '9'and response != '10':
                    response = input('What is your selection?  ')

                if response == "1": #continue on the trail  
                    interfacing_with_menu = False
                    response = input(f"\nToday is: \n{self.month} {self.day}, {self.year}\nAnd you have traveled {self.miles_from_missouri} miles so far on your journey")

                    if "crossing" in menu : crossing_a_river = True
                    break

                if response == "2": #check supplies
                    self.print_inventory()

                if response == "3": 
                    map_result = check_map(self.miles_from_missouri)
                    
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
                    response = input("You have chosen to take one day of rest")
                    self.rest()

                if response == "7": #handle trading
                    self.print_inventory()
                    inventory_after_trading = trade_resource(self.inventory)
                    self.inventory = inventory_after_trading
                    self.increment_day()
                    
                if response == "8": #handle hunting
                    os.system('clear')
                    if self.inventory["Ammunition"] >= 1:
                        generate_animal(self)
                    else:
                        input('You have no Ammunition')

                if response == "9":
                    if self.miles_from_missouri == 0 or self.miles_from_missouri == 304 or self.miles_from_missouri == 640 or self.miles_from_missouri == 932 or self.miles_from_missouri == 989 or self.miles_from_missouri == 1295 or self.miles_from_missouri == 1648 or self.miles_from_missouri == 1863:
                        buy_items_from_store(self.bank_roll, self.inventory)
                    else:
                        input('\nUnfortunately there are no shops nearby.')

                if response == "10": #exit the game
                    exit() # QUITS THE GAME
                
                response = self.print_menu_and_require_new_input(menu)

            if crossing_a_river: cross(self)
            self.travel_for_one_day() ## only way to break interfacing with menu loop and reach this point is if user chose to travel.
            
        os.system('clear')
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
        input('Return to continue....\n')

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
        self.increment_day()

###########################################################################################################



###########################################################################################################

    def travel_for_one_day(self):
        """ Called if the player chooses to travel.  Checks to make sure travel is possible.  If so, the player moves. """
        if self.inventory["Wagon Wheel"] <1 or self.inventory["Wagon Axle"] <1 or self.inventory["Wagon Tongue"] <1:
            input ("\nYou can't move until you repair your wagon.  Try trading for the part you need or buying one in a store (press enter to continue)")
            return
        if self.inventory["Oxen"]<1:
            input ("\nYou don't have any oxen left to pull your wagon.  You should probably either trade for one or buy one soon!")
            return
        if self.miles_from_missouri == self.location_mileposts_left[-1][0]:  #If we're leaving a landmark, pop it off the list
            self.location_mileposts_left.pop()
        self.increment_day()
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

        next_milepost = self.location_mileposts_left[-1]
        if next_milepost[0] <= self.miles_from_missouri: ###  If you've passed a landmark, be sure to stop at it!
            self.miles_from_missouri = next_milepost[0]
            self.talk_to_strangers()
        else: 
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
        os.system('clear')
        print('\nYou come across a friendly local. Do you want to stop and talk to them?')
        response = input('y/n?  ')
        mile_post = (self.miles_from_missouri)
        if mile_post in  talk_to_people('talking_dictionary') and response == 'y' :
            print(talk_to_people('talking_dictionary')[mile_post])
            input('\nReturn to continue....')
        else:
            input('Alrighty then, safe travels!')
            


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



###########################################################################################################
    def define_the_menu(self):
        def return_health_data_for_menu(party):
            party_health_string = '\n'
            for party_member in party:
                party_health_string += party_member.return_health_status_report()
                party_health_string += '\n'
            return party_health_string[:-1]

        health_string = return_health_data_for_menu(self.party)
        menu = f"\n \n{self.month} {self.day}, {self.year}"
        option1 = "Travel down the trail."
        if self.miles_from_missouri == self.location_mileposts_left[-1][0]:
            menu += f"\nYou have reached {self.location_mileposts_left[-1][1]}\n\n"
            if "crossing" in self.location_mileposts_left[-1][1]:
                option1 = "Cross the river."
        menu += f"""
***Today's Temp ***           Distance traveled: {self.miles_from_missouri} miles
* low : {self.weather[0]}
* hi  : {self.weather[1]}
*******************

Pace: {self.pace}                   Rations: {self.rations}

Health: {health_string}         



You may:
    1. """                                   
        menu += option1
        menu +="""           6. Stop to rest.
    2. Check your supplies.             7. Attempt to trade.
    3. Look at the map.                 8. Go hunting.
    4. Change pace.                     9. Buy supplies.
    5. Change food rations.             10. Quit Game
  
""" 
        return menu
        
        
if __name__ == "__main__":
    Game().play()
