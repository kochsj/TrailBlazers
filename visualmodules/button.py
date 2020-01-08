

"""
Buttons with text on them
"""

import arcade
from arcade.gui import TextButton
import random
import os
# from game_play import TravelTrail

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "The Oregon Trail"

# class TextButton:
#     """ Text-based button """

#     def __init__(self,
                 
#                  center_x, center_y,
#                  width, height,
#                  text,
#                  font_size=18,
#                  font_face="Arial",
#                  face_color=arcade.color.LIGHT_BLUE,
#                  highlight_color=arcade.color.WHITE,
#                  shadow_color=arcade.color.GRAY,
#                  button_height=2):
#         self.center_x = center_x
#         self.center_y = center_y
#         self.width = width
#         self.height = height
#         self.text = text
#         self.font_size = font_size
#         self.font_face = font_face
#         self.pressed = False
#         self.face_color = face_color
#         self.highlight_color = highlight_color
#         self.shadow_color = shadow_color
#         self.button_height = button_height
    
class ActionButton (TextButton):
    def __init__(self, action_function, center_x, center_y, width, height, text, font_size=18, font_face='Arial', font_color=arcade.color.BLACK, face_color=arcade.color.BLACK, highlight_color=arcade.color.WHITE, shadow_color=arcade.color.GRAY, button_height=2):
        super().__init__(center_x, center_y, width, height, text, font_size=font_size, font_face=font_face, font_color=font_color, face_color=face_color, highlight_color=highlight_color, shadow_color=shadow_color, button_height=button_height)
        self.action_function = action_function

    
    def on_press(self):
        self.action_function()


'''
Intro page buttons
'''

class ProfessionButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, "Travel the Trail", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        self.action_function()
        super().on_release()

class LearnTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, "Learn more about the trail", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        self.action_function()
        super().on_release()

class QuitTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Quit", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        self.action_function()
        super().on_release()

"""
Charater buttons
"""

class BankerButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        print(center_x, center_y, 'this is the')
        super().__init__(center_x, center_y, 300, 40, 'Billie bob the Banker', 18, 'Arial')
        self.action_function = action_function

    def on_release(self):
        self.action_function()
        super().on_release()

class CarpenterButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, 'Carpenter', 18, 'Arial')
        self.action_function = action_function

    def on_release(self):
        self.action_function()
        super().on_release()

class FarmerButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, 'Farmer', 18, 'Arial')
        self.action_function = action_function

    def on_release(self):
        self.action_function()
        super().on_release()

