import os
from trail_modules.flow.player import character_creation

###########################################################################################################
def print_the_intro():
    """
    Prints the game intro
    Waits for player reponse
    Starts game, learn more about trail, or quits
    """
    os.system('clear')
    print(' '*4, '*'*62)
    print(' '*4, '*'*62)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*14, '~ THE OREGON TRAIL ~', ' '*14, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*14, '1. Travel the trail. ', ' '*13, '*'*5)
    print(' '*4, '*'*5, ' '*9, '2. Learn more about the trail.', ' '*9, '*'*5)
    print(' '*4, '*'*5, ' '*21, '3. Quit', ' '*20, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*5, ' '*50, '*'*5)
    print(' '*4, '*'*62)
    print(' '*4, '*'*62)
    response = ''
    while response != '1' and response != '2' and response != '3':
        response = input()
    
    if response == '1':
        os.system('clear')
        return character_creation() # in trail_modules/flow/player.py - creates the characters and starts the game
    
    if response == '2':
        learn_more() # in trail_modules/flow/intro_prints.py - prints the rules of the game
        print_the_intro()
    
    if response == '3':
        exit() # QUITS THE GAME
###########################################################################################################




###########################################################################################################
def learn_more(): #TODO: add educational info about what was "The Oregon Trail"
    pass
###########################################################################################################




###########################################################################################################
def choose_month_to_depart():
    """
    Prints the options of months to depart on the trail
    Prompts user to pick a month.
    Returns the chosen month.
    """
    print('It is 1848.... TODO....fill this in....months to leave...')
    print('1. March')
    print('2. April')
    print('3. May')
    print('4. June')
    print('5. July')
    # print('6. Ask for advice') # TODO: do we want this??
    response = ''
    while response != '1' and response != '2' and response != '3' and response != '4' and response != '5':
        response = input('What is your choice?  ')
    if response == '1':
        return 'March'
    if response == '2':
        return 'April'
    if response == '3':
        return 'May'
    if response == '4':
        return 'June'
    if response == '5':
        return 'July'
###########################################################################################################
