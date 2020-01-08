    
""" Prompts Strangers to give random location facts at mileposts:
Kansas River Crossing, Big Blue River Crossing, Fort Kearney, Chimney Rock, Fort Laramie, Independence Rock, South Pass, Fort Bridger, Green River Crossing, Soda Springs, Fort Hall, Snake River Crossing, Fort Boise, Blue Mountains, Fort Walla Walla, Oregon City
"""

def talk_to_strangers():
    print('You come across a friendly stranger at this stop. Do you want to talk to them?')
    response = input('y/n?  ')
    mile_post = (miles)
    if mile_post in talking_dictionary and response == 'y' :
       print(talking_dictionary[mile_post])
    
    else:
       print('Alrighty then, safe travels!')


talk_to_strangers()

