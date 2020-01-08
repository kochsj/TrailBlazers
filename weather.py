"""   

Module uses real historical weather data from NWS, Weather Underground and NOOA to create accurate in-game weather at various points along the trail.  Exists solely for the get_weather function.

"""

import random
import copy
_landmarks = []
_distances = [["independence",-1],["kansas river",102],["blue river", 185],["fort kearny",304],["chimney rock",554],["fort laramie",640],["independence rock",830],["south pass",932],["fort bridger",989],["green river",1151],["soda springs",1295],["fort hall",1395],["snake river",1534],["fort boise",1648],["grande ronde valley",1808],["fort walla walla",1863],["the dalles",1920],["barlow road",2000]]


data = {
"independence": [-4,35,8,51, 5,31,25,50,6,50,27,76,20,51,29,78,34,70,60,88,54,73,75,93,79,100,66,80,61,79,72,107,32,77,69,100,32,78,55,85,35,77,21,53,13,39,29,60],"kansas river" : [-4,40,5,54,1,34,23,50,21,62,31,81,38,66,57,80,42,73,54,88,60,78,78,93,65,81,79,94,0,81,79,103,44,69,64,91,31,62,55,85,0,53,33,73,3,33,18,67],"blue river" : [-6,33,13,64,-7,34,9,71,-2,47,8,78,23,62,46,88,32,70,56,94,50,77,69,96,48,78,75,106,55,79,77,104,35,78,55,97,0,66,48,89,3,48,26,72,4,51,18,60],"fort kearny" : [-2,30,12,52,1,30,14,61,0,36,19,72,25,46,39,81,32,61,48,86,52,64,72,91,55,72,73,95,52,72,72,99,0,70,57,90,25,63,39,79,10,46,19,75,-9,30,3,63],"chimney rock" : [-10,33,6,53,-9,30,10,55,-9,49,14,82,0,49,48,79,0,60,42,93,11,59,60,98,21,68,71,100,18,63,62,97,16,64,56,100,6,47,31,78,-9,37,7,72,-21,25,-1,44],
"fort laramie" : [-21,27,0,43,-13,28,17,50,0,35,16,51,0,36,23,63,20,52,46,84,24,49,55,86,33,58,70,91,44,55,66,84,25,49,33,83,9,38,26,66,2,38,17,61,-9,28,12,52],"independence rock" : [-19,38,8,50,-20,29,0,51,0,37,34,66,6,47,27,78,30,51,47,87,38,57,60,97,45,65,77,99,39,60,67,100,33,57,50,91,17,57,30,79,7,35,21,61,-8,36,14,51],"south pass" : [-14,23,0,50,-11,21,7,51,-8,35,9,64,21,48,39,73,21,51,38,77,35,64,61,92,45,67,75,96,45,65,72,95,40,62,50,96,-9,41,13,71,-1,35,19,67,-11,20,7,37],"fort bridger" : [-11,24,6,35,-8,29,10,39,-6,33,13,58,19,42,32,69,20,49,37,74,30,59,54,85,45,63,75,91,35,59,75,89,33,59,55,90,-6,44,17,67,3,35,21,59,-6,28,11,37],"green river" : [-13,33,5,40,-16,35,6,51,-3,40,27,64,11,40,30,68,33,40,48,79,38,57,63,85,37,61,70,88,42,63,63,90,36,53,50,79,4,49,18,73,0,30,24,47,-24,30,-3,50],"soda springs" : [-5,40,11,53,12,41,35,62,10,51,34,73,18,46,44,77,31,53,53,85,43,65,69,101,39,69,69,97,38,68,70,96,33,62,60,93,25,55,48,83,-3,43,19,59,-13,42,7,58],"fort hall" : [-14,32,14,41,4,41,22,57,20,44,40,66,29,49,49,78,29,49,54,83,37,61,67,96,41,69,66,98,41,62,77,96,31,60,52,90,26,52,46,75,16,40,33,68,-11,34,10,45],"snake river" : [-14,32,14,41,4,41,22,57,20,44,40,66,29,49,49,78,29,49,54,83,37,61,67,96,41,69,66,98,41,62,77,96,31,60,52,90,26,52,46,75,16,40,33,68,-11,34,10,45],"fort boise" : [8,32,20,33,12,38,31,52,24,50,37,70,25,56,39,80,31,64,54,97,41,64,60,98,49,73,68,104,53,74,82,102,45,72,71,91,30,53,49,86,20,46,34,68,11,35,21,46],"grande ronde valley" : [12,44,20,66,13,51,31,65,22,49,51,72,30,56,42,87,35,62,54,87,44,68,62,98,50,80,75,106,52,73,64,96,41,65,59,93,35,50,51,70,26,47,37,60,-11,46,-7,62],"fort walla walla" : [27,45,29,66,19,52,27,61,30,46,47,68,34,53,49,80,39,67,62,88,44,68,60,92,66,77,74,106,53,76,70,107,48,61,62,92,37,53,52,73,22,57,30,66,21,47,29,62],"the dalles" : [30,46,42,56,24,41,36,50,25,49,37,72,38,54,52,75,43,59,57,89,50,69,60,98,55,65,67,91,56,66,71,97,42,66,52,88,30,53,47,71,27,52,44,66,28,50,40,58],"barlow road" : [24,48,39,60,34,50,44,63,31,52,55,73,36,51,51,81,46,59,57,84,51,71,61,94,55,67,68,103,55,67,73,97,46,65,60,94,43,60,59,85,24,55,37,64,29,57,39,63]
}  ### raw weather data for each location

test_data = copy.deepcopy(data)

class month:
  """weather is stored in month objects"""
  def __init__(self, lowest_low, highest_low, lowest_high, highest_high):
    self.ll = lowest_low
    self.hl = highest_low
    self.lh = lowest_high
    self.hh = highest_high

class landmark:
  """landmark objects.  Each landmark has a dictionary of months"""
  def __init__ (self, name, data):
    self.name = name
    self.weather_data = {}
    mo = 0
    
    while data:
      mo += 1
      self.weather_data[mo] = month (data.pop(0), data.pop(0),data.pop(0),data.pop(0))      

for location in data:
  #build the array landmark objects
  _landmarks.append (landmark(location, data[location]))



def get_weather (milage, month):
  """ Milage is an int, and month is a string.  The former being total miles travelled.  Returns a tuple (todays low temp, todays high temp)"""
  month_dict = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}
  month = month_dict[month]
  location = ""
  for distance in _distances:
    if distance[1] < milage : location = distance[0]  #finds the string corresponding to last landmark passed (function was originally written to require strings).
  low = 0
  high = 0
  for place in _landmarks:
    if place.name == location:
      while high - low < 10:
        low = _values(place.weather_data[month].ll,place.weather_data[month].hl)
        high = _values(place.weather_data[month].lh,place.weather_data[month].hh)
  return low, high


def _values (low, high):
  """returns a low beween low and high, weighted towards the center)"""
  range = (high - low)/2
  center = low + range
  rand = random.uniform(-1, 1) **3
  results = int(center + range * rand)
  return results