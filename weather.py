"""   Module uses real historical weather data from NWS and NOOA to create accurate in-game weather at various points along the trail"""

import random
landmarks = []

ind_data = [-4,35,8,51, 5,31,25,50,6,50,27,76,20,51,29,78,34,70,60,88,54,73,75,93,79,100,66,80,61,79,72,107,32,77,69,100,32,78,55,85,35,77,21,53,13,39,29,60]

class month:
  """Month objects to be stored as values in a dictionary"""
  def __init__(self, lowest_low, highest_low, lowest_high, highest_high):
    self.ll = lowest_low
    self.hl = highest_low
    self.lh = lowest_high
    self.hh = highest_high

class landmark:
  """locations along the trail"""
  def __init__ (self, name, data):
    self.name = name
    self.weather_data = {}
    mo = 0
    while data:
      mo += 1
      self.weather_data[mo] = month (data.pop(0), data.pop(0),data.pop(0),data.pop(0))      

landmarks.append (landmark("independence", ind_data))
landmarks.append (landmark("independence", ind_data))


def get_weather (location, month):
  """ Location should be a string (ie "Independence", not case sensitive).  Month should be int.   Returns a tuple (Low Temp, High Temp)"""
  low = 0
  high = 0
  for place in landmarks:
    if place.name == location:
      low = _values(place.weather_data[month].ll,place.weather_data[month].hl)
      high = _values(place.weather_data[month].lh,place.weather_data[month].hh)
  if low > high:
    #Most months have freaky weather data where the record highest low temp is greater than the record lowest high.  Theoretically, this makes it possible to return a daily high that's lower than the daily low.
    high = low + 20
  return low, high


def _values (low, high):
  """returns a low beween low and high, weighted towards the center)"""
  range = (high - low)/2
  center = low + range
  rand = random.uniform(-1, 1)
  rand = rand ** 3
  results = int(center + range * rand)
  return results

