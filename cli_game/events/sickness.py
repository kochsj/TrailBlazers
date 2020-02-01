import random
from termcolor import colored, cprint

diseases = {'typhoid':60,'cholera':40,'diphtheria':50,'measles':25,'dysentery':60} 

def get_sick (player):
  """ Assigns a randomly selected disease to a player, and decrements the player's health accordingly"""
  disease = random.choice(list(diseases.keys()))
  if disease in player.sick: player.health ==0
  player.health -= diseases[disease]
  player.sick.append(disease)
  print (colored("Health Status Alert!!!", 'red'), colored(f'{player.name} caught {disease}'))
  input ("")

def get_well (player):
  """Player recovers from one of their diseases (chosen at random) and increases in health accordingly"""
  disease = player.sick.pop(random.randrange(len(player.sick)))
  player.health += 0.5 * diseases[disease] 
  if player.health > 100: player.health = 100
  print (colored("Health Status Alert!!!", "red") , colored(f'{player.name} has recovered from {disease}.,  Huzzah', 'white'))
  input ("")