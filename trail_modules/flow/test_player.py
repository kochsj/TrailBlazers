import pytest
from player import Character

def test_character_creation():
    Tom = Character('Tom')
    assert Tom.name == 'Tom'

def test_character_status_report_at_start():
    Tom = Character('Tom')
    assert Tom.return_health_status_report() == "Tom is in perfect health."

def test_every_health_status():
    Tom = Character('Tom')
    Tom_Sick = Character('Tom')
    Tim = Character('Tim')
    Sam = Character('Sam')

    Tom.health = 90
    assert Tom.return_health_status_report() == "Tom is feeling great."

    Tom_Sick.health = 75
    Tom_Sick.sick = True
    assert Tom_Sick.return_health_status_report() == "Tom is feeling good. (SICK)"

    Tim.health = 50
    assert Tim.return_health_status_report() == "Tim is feeling poor."

    Sam.health = 30
    Sam.sick = True
    assert Sam.return_health_status_report() == "Sam is in critical condition. (SICK)"