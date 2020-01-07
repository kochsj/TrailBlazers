import random

diseases = {'typhoid':60,'cholera':40,'diphtheria':50,'measles':25,'dysentery':60} 

def get_sick (player):
  """ Assigns a randomly selected disease to a player, and decrements the player's health accordingly"""
  disease = random.choice(list(diseases.keys()))
  if disease in player.sick: player.health ==0
  player.health -= diseases[disease]
  player.sick.append(disease)

def get_well (player):
  """Player recovers from one of their diseases (chosen at random) and increases in health accordingly"""
  disease = player.sick.pop(random.randrange(len(player.sick)))
  player.health += diseases[disease]
