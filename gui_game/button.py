import arcade
from arcade.gui import TextButton
    
class ActionButton(TextButton):
    """
    Buttons with text on them
    """
    def __init__(self, action_function, center_x, center_y, width, height, text, font_size=18, font_face='Arial', font_color=arcade.color.BLACK, face_color=arcade.color.BLACK, highlight_color=arcade.color.WHITE, shadow_color=arcade.color.GRAY, button_height=2, name=None):
        super().__init__(center_x, center_y, width, height, text, font_size=font_size, font_face=font_face, font_color=font_color, face_color=face_color, highlight_color=highlight_color, shadow_color=shadow_color, button_height=button_height)
        self.action_function = action_function
        self.name = name

    def on_press(self):
        self.action_function(self)
