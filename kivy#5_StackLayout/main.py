from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(0,10):
            b = Button(text=str(i+1), size_hint=(.2,.2))
            self.add_widget(b)


class BoxLayoutExample(BoxLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
