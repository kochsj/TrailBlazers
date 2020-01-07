import os

###########################################################################################################
def buy_items_from_store(partys_bank_roll, starting_inventory):
    """
    Function for handling a trip to the General Store (in populated locations like forts)
    Requires the current parties_bank_roll and the starting_inventory as arguements
    Prompts user to select items to buy.
    Calls helper functions to handle purchasing the chosen items.
    Returns the shopping_result, a list of [the inventory after shopping, and the remaining bank_roll]
    """
    os.system('clear')
    shopping_inventory = starting_inventory
    response = ""
    bank_roll = partys_bank_roll
    can_shop = True
    menu = """General Store
1. Oxen
2. Food
3. Clothing
4. Ammunition
5. Wagon Wheel
6. Wagon Axle
7. Wagon Tongue
8. Done Shopping"""
    
    while can_shop:
        print(menu)
        print(f'Current funds: {bank_roll}')
        while (
            response != "1"
            and response != "2"
            and response != "3"
            and response != "4"
            and response != "5"
            and response != "6"
            and response != "7"
            and response != "8"
        ):
            response = input("Which item would you like to buy? ")

        os.system('clear')

        if response == "1":
            print("You will need a team of oxen to pull your wagon. I charge $40 an ox.")
            num_chosen, remaining_funds = process_trade_transaction(bank_roll, cost=40)
            shopping_inventory, bank_roll, response = update_inventory_and_bank_roll('Oxen', num_chosen, remaining_funds, shopping_inventory, menu)

        if response == "2":
            print("You will need plenty of food for your party during the trip. I charge $0.25 per pound.")
            num_chosen, remaining_funds = process_trade_transaction(bank_roll, cost=0.25)
            shopping_inventory, bank_roll, response = update_inventory_and_bank_roll('Food', num_chosen, remaining_funds, shopping_inventory, menu)

        if response == "3":
            print("You will need clothing for both summer and winter. I charge $15 per set.")
            num_chosen, remaining_funds = process_trade_transaction(bank_roll, cost=15)
            shopping_inventory, bank_roll, response = update_inventory_and_bank_roll('Clothing', num_chosen, remaining_funds, shopping_inventory, menu)

        if response == "4":
            print("You will need ammunition for your rifles to hunt. I charge $2 per box of bullets.")
            num_chosen, remaining_funds = process_trade_transaction(bank_roll, cost=2)
            shopping_inventory, bank_roll, response = update_inventory_and_bank_roll('Ammunition', num_chosen, remaining_funds, shopping_inventory, menu)

        if response == "5":
            print("You will need spare parts for your wagon. Wagon wheel is one of three types of spare parts. I charge $10 per piece.")
            num_chosen, remaining_funds = process_trade_transaction(bank_roll, cost=10)
            shopping_inventory, bank_roll, response = update_inventory_and_bank_roll('Wagon Wheel', num_chosen, remaining_funds, shopping_inventory, menu)

        if response == "6":
            print("You will need spare parts for your wagon. Wagon axle is one of three types of spare parts. I charge $10 per piece.")
            num_chosen, remaining_funds = process_trade_transaction(bank_roll, cost=10)
            shopping_inventory, bank_roll, response = update_inventory_and_bank_roll('Wagon Axle', num_chosen, remaining_funds, shopping_inventory, menu)

        if response == "7":
            print("You will need spare parts for your wagon. Wagon tongue is one of three types of spare parts. I charge $10 per piece.")
            num_chosen, remaining_funds = process_trade_transaction(bank_roll, cost=10)
            shopping_inventory, bank_roll, response = update_inventory_and_bank_roll('Wagon Tongue', num_chosen, remaining_funds, shopping_inventory, menu)
            
        if response == "8":
            shopping_result = [shopping_inventory, bank_roll]
            can_shop = False
          
    return shopping_result
###########################################################################################################



###########################################################################################################
def process_trade_transaction(bank_roll, cost):
    """
    Requires the current bank_roll and the item's cost as arguements
    determines if the player can afford to purchase
    returns a tuple of the number purchased and the remaining funds
    """
    response = ''
    while not response.isnumeric():
        response = input("How many would you like? ")
    total_cost = int(response) * cost
    money = bank_roll
    if bank_roll < total_cost:
        input("You have no enough money to finish this transaction.")
        return (0, money)
    else:
        money -= total_cost
        return (int(response), money)
###########################################################################################################



###########################################################################################################
def update_inventory_and_bank_roll(inv_item, num_chosen, remaining_funds, shopping_inventory, menu):
    """
    Helper function that handles updating the inventory and updating the game_roll
    Adds the number of chosen items to the dictionary at that item key
    Sets the bank_roll equal to the remaining funds
    Resets the response to a null string, so that the shopping loop will continue on
    Returns a list of the current shopping_inventory, bank_roll, and null response
    """
    shopping_inventory[inv_item] += num_chosen #the number chosen from process_trade_transaction
    bank_roll = remaining_funds #the remaining funds from process_trade_transaction
    response = '' #reset response so that the player is asked what item to buy
    os.system('clear') # clear screen for fresh menu
    return [shopping_inventory, bank_roll, response]
###########################################################################################################

