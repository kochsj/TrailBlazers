import random

def trade_resource(inventory):

    resources = [
        "Oxen",
        "Food",
        "Clothing",
        "Ammunition",
        "Wagon Wheel",
        "Wagon Axle",
        "Wagon Tongue",
    ]

    offered_resource = random.choice(resources)
    trading_resource = random.choice(resources)

    while offered_resource == trading_resource:
      trading_resource = random.choice(resources)

    offered_quantity = random.randint(1,6)
    trading_quantity = random.randint(1,6)

    if offered_resource == 'Food':
      offered_quantity *= 40
    if trading_resource == 'Food':
      trading_quantity *= 40
    if offered_resource == 'Ammunition':
      offered_quantity *= 100
    if trading_resource == 'Ammunition':
      trading_quantity *= 100
    if offered_resource == 'Oxen':
      offered_quantity %= 3
      offered_quantity += 1
    if trading_resource == 'Oxen':
      trading_quantity %= 3
      trading_quantity += 1
    
    response = ""
    acceptable_yes = ['yes', 'y', 'yeah', 'sure', 'ok', 'okay', 'ja']
    acceptable_no = ['no', 'n', 'nah', 'naw', 'no way', 'nope', 'x']

    print(f'You meet another emigrant who offers {offered_quantity} {offered_resource} for {trading_quantity} {trading_resource}.')
    while (response.lower() not in acceptable_yes and response.lower() not in acceptable_no):
      response = input('Would you like to trade?')

    if response.lower() in acceptable_yes:
      if inventory[trading_resource] < trading_quantity:
        input(f'You attempted to trade {trading_quantity} {trading_resource} for {offered_quantity} {offered_resource}. Unfortunately, you have no enough {trading_resource}!')

      else:
        input(f'You have successfully traded {trading_quantity} {trading_resource} for {offered_quantity} {offered_resource}.')
        inventory[trading_resource] -= trading_quantity
        inventory[offered_resource] += offered_quantity

    return inventory

if __name__ == "__main__":
    trade_resource({'Oxen': 20, 'Food': 20, 'Clothing': 20, 'Ammunition': 20, 'Wagon Wheel': 20, 'Wagon Axle': 20, 'Wagon Tongue': 20})