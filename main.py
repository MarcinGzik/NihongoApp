from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        top_buttons = BoxLayout()
        layout.add_widget(top_buttons)
        b1 = Button(text="Go to second screen")
        b1.bind(on_release=self.GotoWindow)
        b2 = Button(text="Dictionary Settings")
        b2.bind(on_release=self.GotoDictionarySettings)
        b3 = Button(text="third")
        b3.bind(on_release=self.GotoThird)
        self.x = self.x + 1
        top_buttons.add_widget(b1)
        top_buttons.add_widget(b2)
        top_buttons.add_widget(b3)

    def GotoWindow(self, value):
        self.manager.current = "second"
        print(value)
    def GotoThird(self, value):
        self.manager.current = "third"

    def GotoDictionarySettings(self, value):
        self.manager.current = "dictionarysettings"

class SecondScreen(Screen):
    pass

'''
class DictionarySettings(Screen):
    def __init__(self, **kwargs):
        super(DictionarySettings, self).__init__(**kwargs)
        layout = BoxLayout(orientation='horizontal')
        for i in range(20):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
'''


class DictionarySettings(Screen):
    def __init__(self, **kwargs):
        self.name = "dictionarysettings"
        super(DictionarySettings, self).__init__(**kwargs)
        layout = GridLayout(cols = 1, minimum_height=40, padding = 10)
        for i in range(20):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)
        grid = GridLayout(cols = 1, minimum_height=40, padding = 10)
        bu1 = Button(text="button in grid", size_hint_y=None, height=40)
        bu2 = Button(text="Click me to go back", size_hint_y=None, height=40)
        bu2.bind(on_release=self.GotoMenu)

        #root = ScrollView(size_hint=(None, 1), size_hint_max_y = 300, size=(Window.width, Window.height*0.8), disabled= False, do_scroll_y = True, parent = grid)
        root = ScrollView(size_hint=(1, None), size_hint_max_y=300, size=(Window.width, Window.height * 0.8), disabled=False, do_scroll_y=True)
        root.add_widget(layout)
        #grid.add_widget(root)
        self.clear_widgets()


        grid.add_widget(bu1)

        print(root.parent)
        self.add_widget(grid)
        grid.add_widget(bu2)


    def GotoMenu(self, value):
        self.manager.current = "main"

class Third(Screen):
    def __init__(self, **kwargs):
        self.name = "third"
        super(Third, self).__init__(**kwargs)
        '''
        scroll = ScrollView(size_hint=(None, 1), size=(Window.width, Window.height), disabled=False, do_scroll_y=True)


        self.add_widget(scroll)
        scroll.add_widget(layout)
        print(self.children)
        scroll.do_scroll_y = self.top
        '''
        #layout that goes into a scrollview, thats width of a screen
        layout = GridLayout(cols=1, spacing=10, size_hint=(1, None), width=Window.width)
        #make so layout will be scrollable in scrollview
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(40):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)
        layout.height = layout.minimum_height
        #creating y scrollable scrollview
        root = ScrollView(size_hint=(1, None), do_scroll_x= False, size =(Window.width, Window.height))


       #root.always_overscroll = True
        b1 = Button(text = "go Back to menu", size_hint_y = None, height = 40)
        b1.bind(on_release=self.GotoMenu)
        layout.add_widget(b1)
        root.add_widget(layout)
        self.add_widget(root)
        print(layout.parent)


    def GotoMenu(self, value):
        self.manager.current = 'main'

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
    sm.add_widget(Screen(name='third'))
    sm.current_screen = MainScreen







MultiScreenApp().run()