from random import randint

def generate_animal():
    """
    
    """
    hunting = input("Something is rustling in the bushes. Would you like to go check it out? (y/n) ")
    if hunting == "y":
        animal = randint(1,8)
        if animal == 1:
            return shooting("squirrel")
        elif animal == 2:
            return shooting("rabbit")
        elif animal == 3:
            return shooting("deer")
        elif animal == 4:
            return shooting("Buffalo")
        elif animal == 5:
            return shooting("Mallard Duck")
        elif animal == 6:
            return shooting("Gazzelle")
        elif animal == 7:
            return shooting("Caribou")
        else:
            return shooting("bear")
    else:
        input("You've decided to continue down the road.")


def shooting(animal):
    decision = input(f"A {animal} jumps out! Would you like to shoot the {animal}? (y/n) ")
    if decision == "y":
        result = randint(1,6)
        if result > 4:
            food(animal)
        elif result == 4:
            input(f"The {animal} ran away.")
            bullets_wasted = randint(1,3)
            # inventory.bullets -= bullets_wasted
            #return bullets
            if bullets_wasted == 1:
                input("You've wasted 1 bullet.")
            else:
                input(f"You've wasted {bullets_wasted} bullets.")
        else:
            attack(animal)
    else:
        input(f"You've decided to spare the {animal}'s life.")


def attack(animal):
    input(f"You have been attacked by the {animal}!")

    if animal == "squirrel":
        input("You've lost 1 point of health!")
        # player.health -= 1
    elif animal == "rabbit":
        input("You've lost 5 points of health!")
        # player.health -= 5
    elif animal == "deer":
        input("You've lost 10 points of health!")
        # player.health -= 10
    elif animal == "Bufallo":
        input("You've lost 5 points of health!")
        # player.health -= 5
    elif animal == "Mallard Duck":
        input("You've lost  points of health!")
        # player.health -= 5
    elif animal == "Gazelle":
        input("You've lost 10 points of health!")
        # player.health -= 10
    elif animal == "Caibou":
        input("You've lost 15 points of health!")
        # player.health -= 15
    else:
        input("You've lost 25 points of health!")
        # player.health -= 25


def food(animal):
    input(f"You have killed the {animal}.")
    if animal == "squirrel":
        input("You've received 1 pound of food!")
        # inventory.food += 1
    elif animal == "rabbit":
        input("You've received 2 pounds of food!")
        # inventory.food += 2
    elif animal == "deer":
        input("You've received 50 pounds of food!")
        # inventory.food += 50
    elif animal == "Bufallo":
        input("You've received 400 pounds of food!")
        # inventory.food += 400
    elif animal == "Mallard Duck":
        input("You've received 1 pounds of food!")
        # inventory.food += 1
    elif animal == "Gazelle":
        input("You've received 35 pounds of food!")
        # inventory.food += 35
    elif animal == "Caribou":
        input("You've received 300 pounds of food!")
        # inventory.food += 300
    else:
        input("You've received 100 pounds of food!")
        # inventory.food += 100
    bullets_used = randint(1,3)
    # inventory.bullets -= bullets_used
    if bullets_used == 1:
        input("You used 1 bullet.")
    else:
        input(f"You used {bullets_used} bullets.")

# generate_animal()


