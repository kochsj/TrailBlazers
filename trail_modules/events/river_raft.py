import random

def cross(game):
	depth=(random.randint(1,6))
	if game.miles_from_missouri == 102:
		width = 620 
	if game.miles_from_missouri == 185:
		width = 30
	if game.miles_from_missouri == 1151:
		width = 450
	if game.miles_from_missouri == 1534:
		width = 158400
	oxen_loss = random.randint(1, 2)
	food_loss = random.randint(1, 3)
	clothing_loss = random.randint(1,3)


	print(f'The river is {depth} feet deep at its deepest point, and {width} feet across.')
	choice = input('''You must choose how to cross:
\n1. Attempt to ford the river.
\n2. Caulk the wagon and float it across. 
\n3. Get a ride across the river (costs 2 clothing)
\n4. Wait to see if conditions improve.
\nWhat is your choice?''')
	if width == 158400:
		if choice =='1':
			print('You attempt to ford the river...')
			print('Your river crossing was not a success.')
			if oxen_loss == 1:
				print(you lost 1 ox)
			if food_loss == 1:
				food_lost = int(game.inventory['Food'] / 5)
				print(f'you lost {food_lost}' pounds of food)
			if clothing_loss == 1:
				clothing_loss == int(game.inventory['Clothing'] / 5)
		elif choice == '2':
			print('You spend a day caulking the wagon and attempt to float across.')
			chance = random.randint(1,8)
			if chance < 7:
				print('Your river crossing was not a success')
			else:
				print('You are able to float across the river safely.')
		elif choice == '3':
			print('You have hired somebody to take you across the river')
			print('You have made it across the river')
			game.inventory['Clothing'] -= 2
		else:
			print('You wait a day to see if conditions improve.')
			return cross(supplies,people)

	else:	
		if choice == '1':
			print('You attempt to ford the river...')
			if depth <= 3:
				print('You have successfully navigated the river without incident!')
				return True
			else:
				print('Your river crossing was not a success.')
				return False
		elif choice == '2':
			print('You spend a day caulking the wagon and attempt to float across.')
			if depth <= 3:
				print('You are able to float across the river safely.')
				return True
			else:
				chance = random.randint(1,2)
				if chance == 1:
					print('You are able to float across the river safely.')
					return True
				else:
					print('Your river crossing was not a success')
					return False

		elif choise == '3':
			print('You have hired somebody to take you across the river')
			print('You have made it across the river')
			game.inventory['Clothing'] -= 2
		else:
			print('You wait a day to see if conditions improve.')
			return cross(supplies,people)

cross(3)

