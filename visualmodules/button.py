"""
Buttons with text on them
"""
import arcade
import random
import os

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

        # if not self.pressed:
        #     color = self.shadow_color
        # else:
        #     color = self.highlight_color

        # # Bottom horizontal
        # arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
        #                  self.center_x + self.width / 2, self.center_y - self.height / 2,
        #                  color, self.button_height)

        # # Right vertical
        # arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
        #                  self.center_x + self.width / 2, self.center_y + self.height / 2,
        #                  color, self.button_height)

        # if not self.pressed:
        #     color = self.highlight_color
        # else:
        #     color = self.shadow_color

        # # Top horizontal
        # arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
        #                  self.center_x + self.width / 2, self.center_y + self.height / 2,
        #                  color, self.button_height)

        # # Left vertical
        # arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
        #                  self.center_x - self.width / 2, self.center_y + self.height / 2,
        #                  color, self.button_height)

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


class TravelTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, "Travel the Trail", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class LearnTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 300, 40, "Learn more about the trail", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class QuitTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Quit", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


# class MyGame(arcade.Window):
#     """
#     Main application class.

#     NOTE: Go ahead and delete the methods you don't need.
#     If you do need a method, delete the 'pass' and replace it
#     with your own code. Don't leave 'pass' in this program.
#     """

#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)

#         # Set the working directory (where we expect to find files) to the same
#         # directory this .py file is in. You can leave this out of your own
#         # code, but it is needed to easily run the examples using "python -m"
#         # as mentioned at the top of this program.
#         file_path = os.path.dirname(os.path.abspath(__file__))
#         os.chdir(file_path)



#         # arcade.set_background_color(arcade.color.AMAZON)


    
#         # Create our on-screen GUI buttons
#         self.button_list = []

#         travel_button = TravelTextButton(400, 300, self.resume_program)
#         self.button_list.append(travel_button)

#         learn_button = LearnTextButton(400, 245, self.pause_program)
#         self.button_list.append(learn_button)

#         quit_button = QuitTextButton(400, 190, self.pause_program)
#         self.button_list.append(quit_button)







#     def on_draw(self):
#         """
#         Render the screen.
#         """

#         arcade.start_render()

#         # Draw the coins
       

#         # Draw the buttons
#         for button in self.button_list:
#             button.draw()


#     def on_mouse_press(self, x, y, button, key_modifiers):
#         """
#         Called when the user presses a mouse button.
#         """
#         check_mouse_press_for_buttons(x, y, self.button_list)

#     def on_mouse_release(self, x, y, button, key_modifiers):
#         """
#         Called when a user releases a mouse button.
#         """
#         check_mouse_release_for_buttons(x, y, self.button_list)

#     def pause_program(self):
#         self.pause = True

#     def resume_program(self):
#         self.pause = False


# def main():
#     """ Main method """
#     game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#     arcade.run()


# if __name__ == "__main__":
#     main()