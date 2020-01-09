

"""
Buttons with text on them
"""
import arcade
import random
import os
# from game_play import TravelTrail

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "The Oregon Trail"


class TextButton:
    """ Text-based button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_BLUE,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False

def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()

# class ActionButton(TextButton):
#     def __init__(self, center_x, center_y, text, action_function=None, name=None, font_color=None):
#         super().__init__(center_x, center_y, 100, 40, text, 18, "Arial", font_color=arcade.color.ALIZARIN_CRIMSON)
#         self.action_function = action_function
#         self.name = name or text
    
#     def on_press(self):
#         self.action_function(self)




'''
Intro page buttons
'''

class ProfessionButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, "Travel the Trail", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        self.action_function()
        print('hello')
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
        super().__init__(center_x, center_y, 300, 40, 'Billie bob the Banker', 18, 'Arial')
        self.action_function = action_function
        print(self.action_function)

    def on_release(self):
        self.action_function()
        super().on_release()

class CarpenterButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, 'Carl the carpenter', 18, 'Arial')
        self.action_function = action_function
        print(self.action_function)

    def on_release(self):
        self.action_function()
        super().on_release()

class FarmerButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, 'Mac the farmer', 18, 'Arial')
        self.action_function = action_function
        print(self.action_function)

    def on_release(self):
        self.action_function()
        super().on_release()

