class Event(object):
    pass


class WindowEvent(Event):
    def __init__(self):
        pass


class MouseEvent(Event):
    def __init__(self, x, y, type):
        pass


class KeyboardEvent(Event):
    def __init__(self, key):
        pass


class CursorEvent(KeyboardEvent):
    def __init(self, key):
        pass
