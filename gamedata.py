from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image


class game():
    times_played = 0
    current_score = 0
    best_score = 0
    answer1 =""
    answer2 =""
    in_game = True
    def __init__(self, times_played, best_score):
        self.times_played = times_played
        self.best_score = best_score


class MemoryGameSettings(game):
    rows = 0
    cols = 0

    def __init__(self, rows, cols, times_played, best_score):
        super(MemoryGameSettings, self).__init__(times_played, best_score)
        self.rows = rows
        self.cols = cols

    def button(self, text_value):
        tgl = ToggleButton(text="", font_size=25, size_hint_min_y=80, outline_width=2)
        tgl.background_down ='appdata/themes/standard/button.png'
        return tgl


class MemoryToggle(ToggleButton):
    text_value = ""
    value_id = None
    gamecore= None
    def __init__(self, strvalue, value_id, gc, **kwargs):
        super(MemoryToggle, self).__init__(**kwargs)
        self.text_value = strvalue
        self.value_id = value_id
        self.gamecore = gc

        #self.background_down = 'appdata/themes/standard/buttonviolet.png'

        #self.background_normal = 'appdata/themes/standard/buttonalpha.png'



        self.background_down = 'appdata/themes/standard/buttonalpha.png'
        self.background_normal = 'appdata/themes/standard/buttonviolet.png'

    def on_state(self, widget, value):
        pass
        #if value == 'normal':
         #   self.disabled = True
