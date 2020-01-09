import random
import os

def cross(game):
	"""handles if a player gets to a river, and has to make a choice of how they want to cross it"""
	depth=(random.randint(1,6))
	width=0
	if game.miles_from_missouri == 102:
		width = 620 
	if game.miles_from_missouri == 185:
		width = 30
	if game.miles_from_missouri == 1151:
		width = 450
	if game.miles_from_missouri == 1543:
		width = 608
	oxen_loss = random.randint(1, 2)
	food_loss = random.randint(1, 3)
	clothing_loss = random.randint(1,3)

	valid_choice = False
	while not valid_choice:
		os.system('clear')
		input(f'The river is {depth} feet deep at its deepest point, and {width} feet across.')
		choice = input('''You must choose how to cross:
		\n1. Attempt to ford the river.
		\n2. Caulk the wagon and float it across. 
		\n3. Get a ride across the river (costs 2 clothing)
		\nWhat is your choice?''')

		if choice == '3':
			if game.inventory['Clothing'] > 1:
				valid_choice = True
			else:
				input('You do not have enough clothing!')

		elif choice != '1' and choice != '2':
			input('That is not a valid input!')

		else:
			valid_choice = True

	if width == 158400:
		if choice =='1':
			input('You attempt to ford the river...')
			input('Your river crossing was not a success.')
			if oxen_loss == 1:
				input('You lost 1 ox')
				game.inventory['Oxen'] -= 1
			if food_loss == 1:
				food_lost = int(game.inventory['Food'] / 5)
				input(f'You lost {food_lost} pounds of food')
				game.inventory['Food'] -= food_lost

			if clothing_loss == 1:
				clothing_lost = int(game.inventory['Clothing'] / 5)
				input(f'You lost {clothing_lost} clothing')
				game.inventory['Clothing'] -= clothing_lost
			i = 0
			for player in game.party:
				death_chance = random.randint(1,4)
				if death_chance == 1:
					print(f'{game.party[i].name} has drowned!')
					game.party.pop(i)
				i += 1

		elif choice == '2':
			input('You spend a day caulking the wagon and attempt to float across.')
			chance = random.randint(1,8)
			if chance < 7:
				input('Your river crossing was not a success')
				if oxen_loss == 1:
					input('You lost 1 ox')
					game.inventory['Oxen'] -= 1
				if food_loss == 1:
					food_lost = int(game.inventory['Food'] / 5)
					input(f'You lost {food_lost} pounds of food')
					game.inventory['Food'] -= food_lost
				if clothing_loss == 1:
					clothing_lost = int(game.inventory['Clothing'] / 5)
					input(f'You lost {clothing_lost} clothing')
					game.inventory['Clothing'] -= clothing_lost
				i = 0
				for player in game.party:
					death_chance = random.randint(1,4)
					if death_chance == 1:
						print(f'{game.party[i].name} has drowned!')
						game.party.pop(i)
					i += 1		
			else:
				input('You are able to float across the river safely.')
		else:
			input('You have hired somebody to take you across the river')
			input('You have made it across the river')
			game.inventory['Clothing'] -= 2

	else:	
		if choice == '1':
			input('You attempt to ford the river...')
			if depth <= 3:
				input('You have successfully navigated the river without incident!')
			else:
				input('Your river crossing was not a success.')
				if oxen_loss == 1:
					input('You lost 1 ox')
					game.inventory['Oxen'] -= 1
				if food_loss == 1:
					food_lost = int(game.inventory['Food'] / 5)
					input(f'You lost {food_lost} pounds of food')
					game.inventory['Food'] -= food_lost
				if clothing_loss == 1:
					clothing_lost = int(game.inventory['Clothing'] / 5)
					input(f'You lost {clothing_lost} clothing')
					game.inventory['Clothing'] -= clothing_lost
				i = 0
				for player in game.party:
					death_chance = random.randint(1,4)
					if death_chance == 1:
						print(f'{game.party[i].name} has drowned!')
						game.party.pop(i)
					i += 1
		elif choice == '2':
			input('You spend a day caulking the wagon and attempt to float across.')
			if depth <= 3:
				input('You are able to float across the river safely.')

			else:
				chance = random.randint(1,2)
				if chance == 1:
					input('You are able to float across the river safely.')
				else:
					input('Your river crossing was not a success')
					if oxen_loss == 1:
						input('You lost 1 ox')
						game.inventory['Oxen'] -= 1
					if food_loss == 1:
						food_lost = int(game.inventory['Food'] / 5)
						input(f'You lost {food_lost} pounds of food')
						game.inventory['Food'] -= food_lost
					if clothing_loss == 1:
						clothing_lost = int(game.inventory['Clothing'] / 5)
						input(f'You lost {clothing_lost} clothing')
						game.inventory['Clothing'] -= clothing_lost
					i = 0
					for player in game.party:
						death_chance = random.randint(1,4)
						if death_chance == 1:
							print(f'{game.party[i].name} has drowned!')
							game.party.pop(i)
						i += 1
		elif choice == '3':
			if game.inventory['Clothing'] >= 2:
				input('You have hired somebody to take you across the river')
				input('You have made it across the river')
				game.inventory['Clothing'] -= 2


