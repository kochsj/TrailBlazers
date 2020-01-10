import os
from termcolor import colored, cprint
from trail_modules.flow.player import character_creation
from pyfiglet import Figlet
f = Figlet(font='small')
red_star = lambda x: cprint(x, 'red')
blue_star = lambda x: cprint(x, 'blue')

###########################################################################################################

def print_the_intro():
    """
    Prints the game intro
    Waits for player reponse
    Starts game, learn more about trail, or quits
    """
    os.system('clear')
    cprint('*'*75, 'red')
    cprint('*'*75, 'blue')
    red_star('*********                                                         *********')
    cprint(f.renderText('THE OREGON TRAIL'), 'green', attrs=['blink', 'bold'])
    red_star('*********                                                         *********')
    red_star('*********                                                         *********')
    red_star('*********                1. Travel the trail.                     *********')
    blue_star('*********           2. Learn more about the trail.                *********')
    red_star('*********                       3. Quit                           *********')
    blue_star('*********                                                         *********')
    red_star('*********                                                         *********')
    cprint('*'*75, 'blue')
    cprint('*'*75, 'red')
    response = ''
    while response != '1' and response != '2' and response != '3':
        response = input()
    
    if response == '1':
        os.system('clear')
        return character_creation() # in trail_modules/flow/player.py - creates the characters and starts the game
    
    if response == '2':
        os.system('clear')
        learn_more() 
        print_the_intro()
    
    if response == '3':
        exit() # QUITS THE GAME
###########################################################################################################




###########################################################################################################
def learn_more(): 
    input(' You\'re about to begin a great adventure, traveling the Oregon Trail.\n Your party of 5, in a covered wagon pulled by a team of oxen, will\n travel from Independence, Missouri, to Oregon City, Oregon -- a\n journey of approximately 2,040 miles, across plains, rivers, and \n mountains. Along the way you will face obstacles, like crossing rivers, \n bad weather, lack of food, illnesses.  How you over come these challenges \n are based on the decisions you make, if you choose wisely you will make \n it all the way to Oregon'


    '\n \n This trail was used by hundreds of thousands of American pioneers\n in the mid-1800s to emigrate west. It was a long and dangerous\n journey that went through Missouri, Kansas, Nebraska, Wyoming, Idaho \n and finally into Oregon. Without the Oregon Trail and the passing of \n the Oregon Donation Land Act in 1850, which encouraged settlement in \n the Oregon Territory, American pioneers would have been slower to settle\n the American West in the 19th century.')
    input('Return to continue...')


###########################################################################################################




###########################################################################################################
def choose_month_to_depart():
    """
    Prints the options of months to depart on the trail
    Prompts user to pick a month.
    Returns the chosen month.
    """
    print('The year is 1848. Select a month to begin your journey.')
    print('1. March')
    print('2. April')
    print('3. May')
    print('4. June')
    # print('5. July')
    
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
    # if response == '5':
    #     return 'July'
###########################################################################################################

def explain_starting_inventory_and_shopping():
    os.system('clear')
    input('You start your journey with a wagon, a wagon wheel, wagon axle, and a wagon tongue for attaching the oxen to the wagon.\n\nIt is advisable to pick up spare parts, food, ammunition, and other necessiary supplies for your journey.\n\nLet\'s head to the store to begin.')