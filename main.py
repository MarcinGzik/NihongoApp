from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.stacklayout import StackLayout


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)
        top_buttons = BoxLayout()
        layout.add_widget(top_buttons)
        layout.add_widget(Button(text='A'))
        layout.add_widget(Button(text='B'))
        layout.add_widget(Button(text='C'))
        b1 = Button(text="Go to second screen")
        b1.bind(on_release=self.GotoWindow)

        top_buttons.add_widget(b1)

    def GotoWindow(self, value):
        self.manager.current = "second"
        print(value)


class SecondScreen(Screen):
    pass


class WindowManager(ScreenManager):
    def PrintGotoWindow(self):
        print("go to window")


class StackLayoutExample(StackLayout):
    pass


class MultiScreenApp(App):
    pass






MultiScreenApp().run()