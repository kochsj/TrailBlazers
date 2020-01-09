
from dictionary import talk_to_people   
""" Prompts Strangers to give random location facts at mileposts:
Kansas River Crossing, Big Blue River Crossing, Fort Kearney, Chimney Rock, Fort Laramie, Independence Rock, South Pass, Fort Bridger, Green River Crossing, Soda Springs, Fort Hall, Snake River Crossing, Fort Boise, Blue Mountains, Fort Walla Walla, Oregon City
"""

        
def talk_to_strangers(self):
   print('You come across a friendly local at this stop. Do you want to talk to them?')
   response = input('y/n?  ')
   mile_post = (self.miles_from_missouri)
   if mile_post in  talk_to_people('talking_dictionary')and response == 'y' :
      print(talk_to_people('talking_dictionary')[mile_post])
      input('Return to continue....')
   else:
      print('Alrighty then, safe travels!')


