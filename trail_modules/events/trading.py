def buy_items_from_store(bank_roll):
    print('General Store')
    print('1. Oxen')
    print('2. Food')
    print('3. Clothing')
    print('4. Ammunition')
    print('5. Spare parts')

    response = ''
    shopping_spree_for_inventory = {}
    while response != '1' and response != '2' and response != '3' and response != '4' and response != '5':
        response = input('Which item would you like to buy? ')
    if response == '1':
        print ('talk about oxen')
        cattle_cost = process_trade_transaction(bank_roll, cost=40)
        shopping_spree_for_inventory['Oxen'] = cattle_cost[0]
    if response == '2':
        return 'April'
    if response == '3':
        return 'May'
    if response == '4':
        return 'June'
    if response == '5':
        return 'July'

def process_trade_transaction(bank_roll, cost):
  response = input('How many would you like? ')
  total_cost = int(response) * cost
  if bank_roll < total_cost:
    print('no money')
  else:
    return (response, total_cost)
