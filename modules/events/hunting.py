from random import randint

def generate_animal():
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
        print("You've decided to continue down the road.")


def shooting(animal):
    decision = input(f"A {animal} jumps out! Would you like to shoot the {animal}? (y/n) ")
    if decision == "y":
        result = randint(1,6)
        if result > 4:
            food(animal)
        elif 4 < result > 5:
            print(f"The {animal} ran away.")
            bullets_wasted = randint(1,3)
            # inventory.bullets -= bullets_wasted
            if bullets_wasted == 1:
                print("You've wasted 1 bullet.")
            else:
                print(f"You've wasted {bullets_wasted} bullets.")
        else:
            attack(animal)
    else:
        print(f"You've decided to spare the {animal}'s life.")


def attack(animal):
    print(f"You have been attacked by the {animal}!")

    if animal == "squirrel":
        print("You've lost 1 point of health!")
        # player.health -= 1
    elif animal == "rabbit":
        print("You've lost 5 points of health!")
        # player.health -= 5
    elif animal == "deer":
        print("You've lost 10 points of health!")
        # player.health -= 10
    elif animal == "Bufallo":
        print("You've lost 5 points of health!")
        # player.health -= 5
    elif animal == "Mallard Duck":
        print("You've lost  points of health!")
        # player.health -= 5
    elif animal == "Gazelle":
        print("You've lost 10 points of health!")
        # player.health -= 10
    elif animal == "Caibou":
        print("You've lost 15 points of health!")
        # player.health -= 15
    else:
        print("You've lost 25 points of health!")
        # player.health -= 25


def food(animal):
    print(f"You have killed the {animal}.")
    if animal == "squirrel":
        print("You've received 1 pound of food!")
        # inventory.food += 1
    elif animal == "rabbit":
        print("You've received 2 pounds of food!")
        # inventory.food += 2
    elif animal == "deer":
        print("You've received 50 pounds of food!")
        # inventory.food += 50
    elif animal == "Bufallo":
        print("You've received 400 pounds of food!")
        # inventory.food += 400
    elif animal == "Mallard Duck":
        print("You've received 1 pounds of food!")
        # inventory.food += 1
    elif animal == "Gazelle":
        print("You've received 35 pounds of food!")
        # inventory.food += 35
    elif animal == "Caribou":
        print("You've received 300 pounds of food!")
        # inventory.food += 300
    else:
        print("You've received 100 pounds of food!")
        # inventory.food += 100
    bullets_used = randint(1,3)
    # inventory.bullets -= bullets_used
    if bullets_used == 1:
        print("You used 1 bullet.")
    else:
        print(f"You used {bullets_used} bullets.")

generate_animal()


