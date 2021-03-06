from cli_game.events.random_events import illness
from termcolor import colored

class person():
  """class to deal with individual member in the party """
 
  def __init__(self, name):
    self.name = name
    self.alive = True
    self.sick = False
    self.status = "Healthy"
    self.disease = disease

    
  def gets_sick(self,illness):
    """
    Keeps track of persons health and if they die """

    if self.sick:
        self.dies(illness)
    else:
        self.sick = True
        # self.status = (f'Has {disease}')
    
  def dies(self, illlness):
    """
    Party memeber has died.
    """

    print(f'Obituary Alert!!! {self.name} died from {self.disease}')
    self.status = "Deceased"
    self.alive = False