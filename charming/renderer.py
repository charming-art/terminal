import sys


class Renderer(object):

    context = None
    size = (10, 10)

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
        self.context.open(self.size)

    def draw(self):
        pass

    def listen(self):
        pass

    def close(self):
        self.context.close()

    @property
    def window_width(self):
        return self.context.window_width

    @property
    def window_height(self):
        return self.context.window_height
