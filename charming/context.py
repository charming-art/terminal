from abc import ABCMeta, abstractclassmethod
import sys


class Context(metaclass=ABCMeta):
    @abstractclassmethod
    def open(self, size):
        """ open the drawing context"""

    @abstractclassmethod
    def close(self):
        """ close the drawing context and restore state of canvas """

    @abstractclassmethod
    def no_cursor(self):
        """ hide cursor """

    @abstractclassmethod
    def cursor(self):
        """ show cursor """

    @abstractclassmethod
    def get_event(self):
        """ get event: mouse event, keyboard event, cursor event """

    @abstractclassmethod
    def resize(self):
        """ resize the window """

    @abstractclassmethod
    def clear(self):
        """ clear the context """

    @abstractclassmethod
    def draw(self, buffer, area):
        """ draw buffer to screen """


class WindowsContext(Context):
    def open(self, size):
        print('hello windows context')

    def close(self):
        pass

    def no_cursor(self):
        pass

    def cursor(self):
        pass

    def get_event(self):
        pass

    def resize(self):
        pass

    def clear(self):
        pass

    def draw(self, buffer, area):
        pass


class CursesContext(Context):
    import curses

    _screen = None

    _pad = None

    window_width = 0

    window_height = 0

    has_resized = False

    def __init__(self):
        self._screen = self.curses.initscr()
        self._screen.keypad(1)
        self._screen.nodelay(1)
        self.curses.noecho()
        self.curses.cbreak()
        self.window_width = self._screen.getmaxyx()[1]
        self.window_height = self._screen.getmaxyx()[0]
        self._screen.refresh()

    def open(self, size):
        content_width, content_height = size
        self._pad = self.curses.newpad(content_height + 2,  content_width + 2)
        self._pad.border()

    def close(self):
        self._screen.keypad(0)
        self.curses.nocbreak()
        self.curses.echo()
        self.curses.endwin()

    def no_cursor(self):
        self.curses.curs_set(0)

    def cursor(self):
        self.curses.curs_set(1)

    def get_event(self):
        key = 0
        while key != -1:
            key = self._screen.getch()
            if key == self.curses.KEY_RESIZE:
                self.has_resized = True

    def resize(self):
        self.curses.update_lines_cols()
        self.window_width = self._screen.getmaxyx()[1]
        self.window_height = self._screen.getmaxyx()[0]

    def clear(self):
        self._screen.clear()
        self._screen.refresh()

    def draw(self, buffer, area):
        pad_x, pad_y, win_x, win_y, win_width, win_height = area
        self.clear()
        self._pad.refresh(pad_y, pad_x, win_y, win_x,
                          win_y + win_height - 1, win_x + win_width - 1)


class BrowserContext(Context):
    def open(self, size):
        print('hello browser context')

    def close(self):
        pass

    def no_cursor(self):
        pass

    def cursor(self):
        pass

    def get_event(self):
        pass

    def resize(self):
        pass

    def clear(self):
        pass

    def draw(self, buffer, area):
        pass
