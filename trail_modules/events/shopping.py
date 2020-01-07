def buy_items_from_store(partys_bank_roll, shopping_inventory):
    shopping_inventory = shopping_inventory or {}
    response = ""
    bank_roll = partys_bank_roll
    can_shop = True
    menu = """
General Store
1. Oxen
2. Food
3. Clothing
4. Ammunition
5. Wagon Wheel
6. Wagon Axle
7. Wagon Tongue
8. Done Shopping
"""
    print(menu)
    
    while can_shop:
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

      if response == "1":
          print("talk about oxen")
          num_chosen, purchase_cost = process_trade_transaction(bank_roll, cost=40)
          if 'Oxen' in shopping_inventory:
            shopping_inventory['Oxen'] += num_chosen
          else:
            shopping_inventory['Oxen'] = num_chosen
          bank_roll = purchase_cost
          response = ''
          print(menu)
          print(f'Current funds: {bank_roll}')
      if response == "2":
          print("talk about food")
          num_chosen, purchase_cost = process_trade_transaction(bank_roll, cost=0.25)
          if 'Food' in shopping_inventory:
            shopping_inventory['Food'] += num_chosen
          else:
            shopping_inventory['Food'] = num_chosen
          bank_roll = purchase_cost
          response = ''
          print(menu)
          print(f'Current funds: {bank_roll}')
      if response == "3":
          print("talk about clothing")
          num_chosen, purchase_cost = process_trade_transaction(bank_roll, cost=15)
          if 'Clothing' in shopping_inventory:
            shopping_inventory['Clothing'] += num_chosen
          else:
            shopping_inventory['Clothing'] = num_chosen
          bank_roll = purchase_cost
          response = ''
          print(menu)
          print(f'Current funds: {bank_roll}')
      if response == "4":
          print("talk about Ammunition")
          num_chosen, purchase_cost = process_trade_transaction(bank_roll, cost=2)
          if 'Ammunition' in shopping_inventory:
            shopping_inventory['Ammunition'] += num_chosen
          else:
            shopping_inventory['Ammunition'] = num_chosen
          bank_roll = purchase_cost
          response = ''
          print(menu)
          print(f'Current funds: {bank_roll}')
      if response == "5":
          print("talk about Wagon Wheel")
          num_chosen, purchase_cost = process_trade_transaction(bank_roll, cost=10)
          if 'Wagon Wheel' in shopping_inventory:
            shopping_inventory['Wagon Wheel'] += num_chosen
          else:
            shopping_inventory['Wagon Wheel'] = num_chosen
          bank_roll = purchase_cost
          response = ''
          print(menu)
          print(f'Current funds: {bank_roll}')
      if response == "6":
          print("talk about Wagon Axle")
          num_chosen, purchase_cost = process_trade_transaction(bank_roll, cost=10)
          if 'Wagon Axle' in shopping_inventory:
            shopping_inventory['Wagon Axle'] += num_chosen
          else:
            shopping_inventory['Wagon Axle'] = num_chosen
          bank_roll = purchase_cost
          response = ''
          print(menu)
          print(f'Current funds: {bank_roll}')
      if response == "7":
          print("talk about Wagon Tongue")
          num_chosen, purchase_cost = process_trade_transaction(bank_roll, cost=10)
          if 'Wagon Tongue' in shopping_inventory:
            shopping_inventory['Wagon Tongue'] += num_chosen
          else:
            shopping_inventory['Wagon Tongue'] = num_chosen
          bank_roll = purchase_cost
          response = ''
          print(menu)
          print(f'Current funds: {bank_roll}')
      if response == "8":
          shopping_result = [shopping_inventory, bank_roll]
          can_shop = False
          
    return shopping_result


def process_trade_transaction(bank_roll, cost):
    response = input("How many would you like? ")
    total_cost = int(response) * cost
    money = bank_roll
    if bank_roll < total_cost:
        print("no money")
        return (0, money)
    else:
        money -= total_cost
        return (int(response), money)


if __name__ == "__main__":
    a = buy_items_from_store(1600, {})
    print(a)