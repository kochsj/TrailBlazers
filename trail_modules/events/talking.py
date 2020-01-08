
from dictionary import talk_to_people   
""" Prompts Strangers to give random location facts at mileposts:
Kansas River Crossing, Big Blue River Crossing, Fort Kearney, Chimney Rock, Fort Laramie, Independence Rock, South Pass, Fort Bridger, Green River Crossing, Soda Springs, Fort Hall, Snake River Crossing, Fort Boise, Blue Mountains, Fort Walla Walla, Oregon City
"""
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
         self.miles_from_missouri = 1863
         self.year = 1848
         self.weather = (0,0)
         self.location_mileposts_left=[2040,1863,1808,1648,1543,1359,1259,1151,989,932,830,640,554,304,185,102]
        
      def talk_to_strangers(self):
            print('You come across a friendly stranger at this stop. Do you want to talk to them?')
            response = input('y/n?  ')
            mile_post = (self.miles_from_missouri)
            if mile_post in  talk_to_people('talking_dictionary')and response == 'y' :
                  print(talk_to_people('talking_dictionary')[mile_post])
                  input('Return to continue....')
            else:
                  print('Alrighty then, safe travels!')


game = Game()
game.talk_to_strangers()

