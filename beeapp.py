# toe-dip from Python 2017 beeware lecture
# Requires Python 3.5-3.5.X.  Do NOT use 3.6

import toga

class Freedom(toga.App):

    def calculate(self, widget):
        try:
            self.c_input.value = (
                float(self.f_input.value) 32.0) * 5.0 / 9.0
        except Exception:
            self.c_input.value = '???'


def startup(self):
    self.main_window = toga.MainWindow(self.name)
    self.main_window.app = self
    box = toga.Box()
    c_box = toga.Box()
    f_box = toga.Box()
    self.c_input = toga.TextInput(readonly=True)
    self.f_input = toga.TextInput()
    # widgets
    c_label = toga.Label('Celcius', alignment=toga.LEFT_ALIGNED)
    f_label = toga.Label('Fahrenheit', alignment=toga.LEFT_ALIGNED)
    join_label = toga.Label('is equivalent to', alignment=toga.RIGHT_ALIGNED)
    button = toga.Button('Calculate', on_press=self.calculate)
    # composition
    f_box.add(self.f_input)
    f_box.add(f_label)
    c_box.add(join_label)
    c_box.add(self.c_input)
    c_box.add(c_label)
    box.add(f_box)
    box.add(c_box)
    box.add(button)
    # style
    box.style.set(flex_direction='column', padding=10)
    f_box.style.set(flex_direction='row', margin=5)
    c_box.style.set(flex_direction='row', margin=5)
    self.c_input.style.set(flex=1)
    self.f_input.style.set(flex=1, margin_left=160)
    c_label.style.set(width=100, margin_left=10)
    f_label.style.set(width=100, margin_left=10)
    join_label.style.set(width=150, margin_right=10)
    button.style.set(margin_top=15)

    self.main_window.content = box
    self.main_window.show()


def main():
    return Freedom('Freedom Units', 'org.pybee')



