import sys


class Renderer(object):

    context = None
    size = (10, 10)
    buffer = []
    pad_x = 0
    pax_y = 0
    win_x = 0
    win_y = 0
    win_width = 0
    win_height = 0

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
        self._update_pad_area()

    def draw(self):
        area = (self.pad_x, self.pad_y, self.win_x,
                self.win_y, self.win_width, self.win_height)
        self.context.draw(self.buffer, area)

    def get_events(self):
        def is_valid(e):
            if e.type == "mouse":
                e.x -= self.win_x
                e.y -= self.win_y
                x_in = e.x >= 0 and e.x < self.win_width
                y_in = e.y >= 0 and e.y < self.win_height
                return x_in and y_in
            else:
                return True
        events = [e for e in self.context.get_events() if is_valid(e)]
        return events

    def close(self):
        self.context.close()

    def no_cursor(self):
        self.context.no_cursor()

    def cursor(self):
        self.context.cursor()

    def resize(self):
        self.context.resize()
        self._update_pad_area()

    @property
    def window_width(self):
        return self.context.window_width

    @property
    def window_height(self):
        return self.context.window_height

    def _update_pad_area(self):
        box_width = self.size[0] + 2
        box_height = self.size[1] + 2
        x = (self.window_width - box_width) // 2
        y = (self.window_height - box_height) // 2

        self.pad_x = -x if x < 0 else 0
        self.pad_y = -y if y < 0 else 0
        self.win_x = 0 if x < 0 else x
        self.win_y = 0 if y < 0 else y
        self.win_width = self.window_width if x <= 0 else box_width
        self.win_height = self.window_height if y <= 0 else box_height
