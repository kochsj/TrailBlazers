"""
Creating the random events that occur in the game.
"""

import random

def randomize(game):
  """ Determines if random event occurs"""
  random.seed()
  
  # Determine if random event occurs.
  chance = list(range(1,31)) 
  number = random.randint(1,100)
  if not(number in chance):
    return
  # List random event functions.
  misfortunes = [
      illness,
      oxen_dies,
      thief_attacks,
      wagon_breaks,
      bad_weather
      ]
  
  # Randomly pick one event to occur.
  misfortune= random.randint(0,len(misfortunes)-1)
  your_misfortune = misfortunes[misfortune]
  return your_misfortune(game)

def illness(game):
  """
  Causes a random party-member to become ill with a random disease.
  """
  
  # Create names of diseases.
  diseases = [
      'typhoid',
      'cholera',
      'diphtheria',
      'measles',
      'dysentery'
      ]
  
  # Randomly select a party-member.
  choices = []
  for i in range(len(game.party)):
    if game.party[i]:
      choices.append(i)
  name = random.choice(choices)
      
  # Randomly select a disease.
  disease = random.choice(diseases)
  
  # Inform player and make party member sick.
  name = game.party[name].name
  print(f"{name} has {disease}")
  game.party[name].gets_sick(disease)
  
def oxen_dies(game):
  """
  Removes an oxen from the players inventory.
  """

  print("An oxen has died")
  oxen_available = game.inventory('oxen')
  
  # Avoids printing negative numbers to player.
  if oxen_available > 1:
    remaining = game.consume('oxen',1)
    print(f'You have {remaining} oxen remaining')

def thief_attacks(player):
  """
  Theif steals and removes a random amount of food from the player's inventory.
  """


def wagon_breaks(player):
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

  

  
  



        