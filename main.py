from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import *

import user_infterface as ui
import gamedata as gm


gamecore = gm.MemoryGameSettings(4,4,0,0)

Window.size = (1400, 1000)

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
        self.manager.current = "games"
        print(value)

    def Settings(self, value):
        self.manager.current = "nihappsettings"

    def GotoDictionarySettings(self, value):
        self.manager.current = "dictionarysettings"


class Games(Screen):
    def __init__(self, **kwargs):
        self.name = "games"
        super(Games, self).__init__(**kwargs)


        root = ScrollView(size_hint=(1, None), do_scroll_x=False, size=(Window.height, Window.width))
        layout = GridLayout(cols = 1, minimum_height=40, padding = 10, size_hint=(1, None), spacing = 6)
        b1 = ui.menu_button("go back to menu")
        b1.bind(on_release=self.gotomenu)
        b2 = ui.menu_button("Memory Game")
        b2.bind(on_release=self.gotomemorygame)
        layout.add_widget(b1)
        layout.add_widget(b2)



        l1 = AnchorLayout(anchor_x='center', anchor_y='top')
        root.add_widget(layout)
        l1.add_widget(root)
        self.add_widget(l1)


    def gotomenu(self, value):
        self.manager.current = "main"
        print(value)
    def gotomemorygame(self, value):
        self.manager.current = "memorygame"



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


class NihAppSettings(Screen):
    def __init__(self, **kwargs):
        self.name = "nihappsettings"
        super(NihAppSettings, self).__init__(**kwargs)
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

class MemoryGame(Screen):
    answer_a = ""
    answer_b = ""
    def __init__(self, **kwargs):
        self.name = "memorygame"
        super(MemoryGame, self).__init__(**kwargs)


        root = BoxLayout(orientation = 'vertical', padding = 10, minimum_height = Window.height /15)
        back = ToggleButton(text="Go back to menu", font_size=25, size_hint_max_y=80, outline_width=2)
        back.bind(on_release=self.gotomenu)
        root.add_widget(back)
        layout = GridLayout(cols = 3, minimum_height=40, padding = 10, size_hint=(1, 1), spacing = 6)

        for i in range(12):
            relative = RelativeLayout(size_hint_y=200, size_hint_x = 200)
            #toggle1 = ToggleButton(text="", font_size=25, size_hint_min_y=80, outline_width=2, opacity =1)
            #toggle1.background_down ='appdata/themes/standard/buttonviolet.png'
            #toggle1.background_normal='appdata/themes/standard/buttonalpha.png'
            toggle1 = gm.MemoryToggle(str(i), size_hint_min_y=80)
            label1 = Label(text =str(i))
            relative.add_widget(label1)
            toggle1.state = 'down'
            relative.add_widget(toggle1)

            layout.add_widget(relative)

        root.add_widget(layout)
        self.add_widget(root)
        print(self.answer_a)
    def gotomenu(self, value):
        self.manager.current = "main"
class WindowManager(ScreenManager):
    pass


class StackLayoutExample(StackLayout):
    pass


class MultiScreenApp(App):
    sm = ScreenManager()
    sm.add_widget(Screen(name='main'))
    sm.add_widget(Screen(name='games'))
    sm.add_widget(Screen(name='dictionary'))
    sm.add_widget(Screen(name='nihappsettings'))
    sm.add_widget(Screen(name='memorygame'))
    sm.current_screen = MainScreen

MultiScreenApp().run()