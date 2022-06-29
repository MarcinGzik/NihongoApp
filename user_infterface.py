from kivy.uix.button import Button


class MenuButton():
    btn = 0

    def __init__(self):
        self.btn = Button(font_size = 14, outline_width = 1, border = 10)





def menu_button(text_value):
    return Button(text = text_value, font_size=30, outline_width=2, size_hint_min_y = 80)