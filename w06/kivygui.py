from kivy.app import App
from kivy.uix.widget import Widget

# Write a kivy app that gets the radius from user and outputs the area of a circle
# Area of a circle = pi * r^2
# Use the following code to get the value of pi
# from math import pi
class CircleArea(Widget):
    def __init__(self):
        super(CircleArea, self).__init__()
        self.radius = 0
        self.area = 0
        self.pi = 3.14159

    def calculate_area(self):
        if self.ids.radius.text == "":
            self.ids.radius.background_color = (1, 1, 1, 1)
            self.ids.area.text = ""
        elif not self.ids.radius.text.isnumeric():
            self.ids.radius.background_color = (1, 0, 0, 1)
            self.ids.area.text = "Invalid input"
        elif int(self.ids.radius.text) > 1000 or int(self.ids.radius.text) < 1:
            self.ids.radius.background_color = (1, 0, 0, 1)
            self.ids.area.text = "Radius out of range"
        else:
            self.radius = float(self.ids.radius.text)
            self.area = self.pi * self.radius ** 2
            self.ids.area.text = f"{self.area:.2f} cm²"
            self.ids.radius.background_color = (1, 1, 1, 1)

class CircleAreaApp(App):
    def build(self):
        return CircleArea()


if __name__ == '__main__':
    CircleAreaApp().run()
