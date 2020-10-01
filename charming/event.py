from . import sketch


def get_mouse_x():
    return sketch.mouse_x


def get_mouse_y():
    return sketch.mouse_y


def get_pmouse_y():
    return sketch.pmouse_y


def get_pmouse_x():
    return sketch.pmouse_x


def get_key():
    return sketch.key


def key_typed(hook):
    sketch.add_hook('key_typed', hook)


def mouse_clicked(hook):
    sketch.add_hook('mouse_clicked', hook)


class Event(object):
    type = ""

    def __init__(self, type):
        self.type = type


class WindowEvent(Event):
    def __init__(self):
        super(WindowEvent, self).__init__('window')


class MouseEvent(Event):
    x = 0
    y = 0
    mouse_type = ""

    def __init__(self, x, y, type):
        super(MouseEvent, self).__init__('mouse')
        self.x = x
        self.y = y
        self.mouse_type = type


class KeyboardEvent(Event):
    key = 0

    def __init__(self, key):
        super(KeyboardEvent, self).__init__('keyboard')
        self.key = key

