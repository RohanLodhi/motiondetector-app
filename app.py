import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera
'''from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Design(Widget):
    pass
    def __init__(self, **kwargs):
        super(Design, self).__init__(**kwargs)
        self.inside = GridLayout()
        self.inside.cols = 2
        self.rows = 2
        self.start = Button(text="Start", font_size=40)
        self.start.bind(on_press=self.toStart)
        self.inside.add_widget(self.start)
        self.stop = Button(text="Stop", font_size=40)
        self.stop.bind(on_press=self.toStop)
        self.inside.add_widget(self.stop)

        self.add_widget(self.inside)

    def toStart(self):
        print("first")

    def toStop(self):
        print("second")'''



class MyApp(App):
    def build(self):
        return FloatLayout(), Camera(play=True, index=1, resolution=(640,480))

if __name__ == "__main__":
    MyApp().run()