from random import randint

def generate_animal(game):
    """
    
    """
    hunting = input("Something is rustling in the bushes. Would you like to go check it out? (y/n) ")
    if hunting == "y":
        animal = randint(1,8)
        if animal == 1:
            return shooting("squirrel", game)
        elif animal == 2:
            return shooting("rabbit", game)
        elif animal == 3:
            return shooting("deer", game)
        elif animal == 4:
            return shooting("Buffalo", game)
        elif animal == 5:
            return shooting("Mallard Duck", game)
        elif animal == 6:
            return shooting("Gazzelle", game)
        elif animal == 7:
            return shooting("Caribou", game)
        else:
            return shooting("bear", game)
    else:
        input("You've decided to continue down the road.")


def shooting(animal, game):
    decision = input(f"A {animal} jumps out! Would you like to shoot the {animal}? (y/n) ")
    if decision == "y":
        result = randint(1,6)
        if result >= 3:
            food(animal, game)
        elif result == 2:
            input(f"The {animal} ran away.")
            random = randint(5,15)
            if random <= game.inventory['Ammunition']:
                bullets_used = random
            else:
                bullets_used = game.inventory['Ammunition']
                game.inventory['Ammunition'] -= bullets_used
                input(f"You've wasted {bullets_used} bullets.")

        else:
            attack(animal, game)
    else:
        input(f"You've decided to spare the {animal}'s life.")


def attack(animal, game):
    input(f"You have been attacked by the {animal}!")

    if animal == "squirrel":
        input("You've lost 1 point of health!")
        game.party[0].health -= 1
    elif animal == "rabbit":
        input("You've lost 5 points of health!")
        game.party[0].health -= 5
    elif animal == "deer":
        input("You've lost 10 points of health!")
        game.party[0].health -= 10
    elif animal == "Bufallo":
        input("You've lost 10 points of health!")
        game.party[0].health -= 10
    elif animal == "Mallard Duck":
        input("You've lost  points of health!")
        game.party[0].health -= 5
    elif animal == "Gazelle":
        input("You've lost 15 points of health!")
        game.party[0].health -= 15
    elif animal == "Caibou":
        input("You've lost 15 points of health!")
        game.party[0].health -= 15
    else:
        input("You've lost 20 points of health!")
        game.party[0].health -= 20


def food(animal, game):
    input(f"You have killed the {animal}.")
    if animal == "squirrel":
        input("You've received 1 pound of food!")
        game.inventory['Food'] += 1
    elif animal == "rabbit":
        input("You've received 2 pounds of food!")
        game.inventory['Food'] += 2
    elif animal == "deer":
        input("You've received 50 pounds of food!")
        game.inventory['Food'] += 50
    elif animal == "Bufallo":
        input("You've received 400 pounds of food!")
        game.inventory['Food'] += 400
    elif animal == "Mallard Duck":
        input("You've received 1 pounds of food!")
        game.inventory['Food'] += 1
    elif animal == "Gazelle":
        input("You've received 35 pounds of food!")
        game.inventory['Food'] += 35
    elif animal == "Caribou":
        input("You've received 300 pounds of food!")
        game.inventory['Food'] += 300
    else:
        input("You've received 100 pounds of food!")
        game.inventory['Food'] += 100    
    random = randint(5,15)
    if random <= game.inventory['Ammunition']:
        bullets_used = random
    else:
        bullets_used = game.inventory['Ammunition']
    game.inventory['Ammunition'] -= bullets_used
    input(f"You used {bullets_used} bullets.")
  



