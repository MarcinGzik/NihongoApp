from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
import user_infterface as ui


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        #layout of main screen
        layout = BoxLayout(orientation='vertical', padding = 10, spacing = 6)
        #buttons of main screen
        b1 = ui.menu_button("Play Games")
        b1.bind(on_release=self.GotoWindow)
        b2 = ui.menu_button("Dictionary Settings")
        b2.bind(on_release=self.GotoDictionarySettings)
        b3 = ui.menu_button("Settings")
        b3.bind(on_release=self.Settings)

        layout.add_widget(b1)
        layout.add_widget(b2)
        layout.add_widget(b3)
        self.add_widget(layout)


    def GotoWindow(self, value):
        self.manager.current = "second"
        print(value)

    def Settings(self, value):
        self.manager.current = "settings"

    def GotoDictionarySettings(self, value):
        self.manager.current = "dictionarysettings"


class SecondScreen(Screen):
    pass


class DictionarySettings(Screen):
    def __init__(self, **kwargs):
        self.name = "dictionarysettings"
        super(DictionarySettings, self).__init__(**kwargs)

        root = ScrollView(size_hint=(1, None), do_scroll_x=False, size=(Window.height, Window.width))
        layout = GridLayout(cols = 1, minimum_height=40, padding = 10, size_hint=(1, None), spacing = 6)

        b1 = ui.menu_button("go back to menu")
        b1.bind(on_release=self.gotomenu)
        b2 = ui.menu_button("Show dictionaries")
        b3 = ui.menu_button("Add Dictionary")
        layout.add_widget(b1)

        dropdown = DropDown()
        for index in range(10):
            # When adding widgets, we need to specify the height manually
            # (disabling the size_hint_y) so the dropdown can calculate
            # the area it needs.

            btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

            # for each button, attach a callback that will call the select() method
            # on the dropdown. We'll pass the text of the button as the data of the
            # selection.
            #btn.bind(on_release=lambda btn: dropdown.select(btn.text))

            # then add the button inside the dropdown
            dropdown.add_widget(btn)

        # create a big main button
        dropdown.dismiss()
        dropdown.max_height = Window.height/2


        layout.add_widget(dropdown)

        # show the dropdown menu when the main button is released
        # note: all the bind() calls pass the instance of the caller (here, the
        # mainbutton instance) as the first argument of the callback (here,
        # dropdown.open.).
        b2.bind(on_release=dropdown.open)
        layout.add_widget(b3)
        layout.add_widget(b2)
        b1.opacity= 0
        b1.disabled = True
        for i in range(100):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)

        layout.bind(minimum_height=layout.setter('height'))
        root.add_widget(layout)
        l1 = AnchorLayout(anchor_x='center', anchor_y='top')
        l1.add_widget(root)
        b5 = Button(text = "go Back to menu", size_hint_y = None, height = 80, font_size=30, outline_width=2 )
        b5.bind(on_release=self.gotomenu)
        l1.add_widget(b5)
        self.add_widget(l1)

    def gotomenu(self, value):
        self.manager.current = "main"
        print(value)

class Neko(Screen):
    def __init__(self, **kwargs):
        self.name = "settings"
        super(Neko, self).__init__(**kwargs)
        root = ScrollView(size_hint=(1, None), do_scroll_x=False, size=(Window.height, Window.width))
        layout = GridLayout(cols = 1, minimum_height=40, padding = 10, size_hint=(1, None), spacing = 6)

        b1 = ui.menu_button("go back to menu")
        b1.bind(on_release=self.gotomenu)
        b2 = ui.menu_button("Show dictionaries")
        b3 = ui.menu_button("Add Dictionary")
        layout.add_widget(b1)
        self.add_widget(layout)

    def gotomenu(self, value):
        self.manager.current = "main"


'''
class Settings(Screen):
    def __init__(self, **kwargs):
        self.name='settings'
        super(Settings, self).__init__(**kwargs)
        layout = GridLayout(cols= 1)
        b1 = ui.menu_button("go back to menu")
        b1.bind(on_release=self.gotomenu)
        b2 = ui.menu_button("button in settings")

        layout.add_widget(b1)
        layout.add_widget(b2)
        self.add_widget(layout)

    def gotomenu(self, value):
        self.manager.current = "main"
        print(value)

'''
class WindowManager(ScreenManager):
    def PrintGotoWindow(self):
        print("go to window")


class StackLayoutExample(StackLayout):
    pass


class MultiScreenApp(App):
    sm = ScreenManager()
    sm.add_widget(Screen(name='main'))
    sm.add_widget(Screen(name='second'))
    sm.add_widget(Screen(name='dictionary'))
    sm.add_widget(Screen(name='neko'))
    sm.current_screen = MainScreen







MultiScreenApp().run()