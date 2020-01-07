import pytest
from weather import get_weather, test_data, _distances



def test_barlow():
  for _ in range (300):
    weather = get_weather (2010,12)
    assert weather[0] >= 29
    assert weather[1] <= 63

# @pytest.mark.skip()
def test_every_damned_thing():
  for distance in _distances:
    landmark, miles = distance[0], distance[1]+1
    low = test_data[landmark][44]
    high = test_data[landmark][47]
    for _ in range (300):
      weather = get_weather(miles,12)
      assert weather [0] >= low
      assert weather [1] < high