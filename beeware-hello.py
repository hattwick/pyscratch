# toe-dip from Python 2017 beeware lecture
# Requires Python 3.5-3.5.X.  Do NOT use 3.6

import toga

def handler(widget):
    widget.window.info_dialog("Say hello",                              "Hello, world")

def build(app):
    box = toga.Box()
    button = toga.Button('Say hello',                         on_press=handler)
    button.style.set(margin=50)
    box.add(button)
    return box


if __name__ == '__main__':
    app = toga.App('Hello', 'org.pybee.hello',                   startup=build)
    app.main_loop()


