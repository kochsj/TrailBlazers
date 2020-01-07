"""
Creating the random events that occur in the game.
"""

import random

def randomize(game):
    """ Determines if random event occurs"""
    # List random event functions.
    misfortunes = [
      oxen_dies,
      thief_attacks,
      wagon_breaks,
      bad_weather
      ]
  
  # Randomly pick one event to occur.
    misfortune= random.randint(0,len(misfortunes)-1)
    your_misfortune = misfortunes[misfortune]
    return your_misfortune(game)


  
def oxen_dies(game):
  """
  Removes an oxen from the players inventory.
  """

  print("An oxen has died")
  oxen_available = game.inventory('Oxen')
  
  # Avoids printing negative numbers to player.
  if oxen_available > 1:
    remaining = game.inventory('Oxen') -1
    print(f'You have {remaining} oxen remaining')

def thief_attacks(game):
  """
  Theif steals and removes a random amount of food from the player's inventory.
  """
  amount = random.randint(10,30)
  food_available = game.inventory('Food')
  if food_available >= amount:
    print(f'A thief has stolen {amount} pounds of food')
    remaining_food = (game.inventory('Food')- amount)
    print(f'You have {remaining_food} pounds of food remaining')
  else:
    print('A thief stole all of  your food')


def wagon_breaks(game):
  """
  Random part on wagon breaks and ends game if player cannot fix it.
  """
  wagon_parts = [
      'wheel',
      'axel',
      'tongue'
      ]
  
  part = random.choice(wagon_parts)
  
  print(f'A wagon {part} broke')


def bad_weather(game):
  """
  Player is stuck while a random storm passes.
  """
  
  # (name, days to wait)
  bad_weather= [
      ('heavy rain', 1),
      ('snow storm', 2),
      ('hail', 1),
      ('a blizzard', 3),
      ('strong winds', 1)
      ]
  
  # Determine storm.
  event = random.choice(bad_weather)
  weather = event[0]
  days = event[1]
  
  # Inform player, advance time, and consume food for waiting.
  print(f'You have to halt your journey for {days} days due to {weather}')

  

  
  



        