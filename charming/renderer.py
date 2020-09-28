import sys


class Renderer(object):

    context = None
    size = (10, 10)
    buffer = []

    def __init__(self):
        if sys.platform == 'win32':
            from .context import WindowsContext
            self.context = WindowsContext()
        elif sys.platform == 'brython':
            from .context import BrowserContext
            self.context = BrowserContext()
        else:
            from .context import CursesContext
            self.context = CursesContext()

    def setup(self):
        width, height = self.size
        self.context.open(self.size)
        self.buffer = ['' for _ in range(width * height)]

    def draw(self):
        area = self._get_pad_area()
        self.context.draw(self.buffer, area)

    def listen(self):
        self.context.get_event()
        if self.context.has_resized:
            self.context.resize()

    def close(self):
        self.context.close()

    def no_cursor(self):
        self.context.no_cursor()

    def cursor(self):
        self.context.cursor()

    @property
    def window_width(self):
        return self.context.window_width

    @property
    def window_height(self):
        return self.context.window_height

    def _get_pad_area(self):
        box_width = self.size[0] + 2
        box_height = self.size[1] + 2
        x = (self.window_width - box_width) // 2
        y = (self.window_height - box_height) // 2

        pad_x = -x if x < 0 else 0
        pad_y = -y if y < 0 else 0
        win_x = 0 if x < 0 else x
        win_y = 0 if y < 0 else y
        win_width = self.window_width if x <= 0 else box_width
        win_height = self.window_height if y <= 0 else box_height

        return (pad_x, pad_y, win_x, win_y, win_width, win_height)
