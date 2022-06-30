from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
class game():
    times_played = 0
    current_score = 0
    best_score = 0
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
    def __init__(self, strvalue, **kwargs):
        super(MemoryToggle, self).__init__(**kwargs)
        self.text_value = strvalue
        self.background_down = 'appdata/themes/standard/buttonviolet.png'
        self.background_normal = 'appdata/themes/standard/buttonalpha.png'

    def on_state(self, widget, value):
        if value == 'normal':
            print(self.text_value)
            return self.text_value
        else:
            pass