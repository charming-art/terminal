from abc import ABCMeta, abstractclassmethod
import sys


class Context(metaclass=ABCMeta):
    @abstractclassmethod
    def open(self, size):
        """ open the drawing context"""

    @abstractclassmethod
    def close(self):
        """ close the drawing context and restore state of canvas """


class WindowsContext(Context):
    def open(self, size):
        print('hello windows context')

    def close(self):
        pass


class CursesContext(Context):
    import curses

    _screen = None

    _pad = None

    windowWidth = 0

    windowHeight = 0

    def __init__(self):
        self._screen = self.curses.initscr()
        self._screen.keypad(1)
        self.curses.noecho()
        self.curses.cbreak()
        self.window_width = self.curses.COLS  # pylint: disable=no-member
        self.window_height = self.curses.LINES  # pylint: disable=no-member

    def open(self, size):
        content_width, content_height = size
        box_width = content_width + 2
        box_height = content_height + 2

        self._pad = self.curses.newpad(box_height,  box_width)
        self._pad.border()

        x = int((self.window_width - box_width) / 2)
        y = int((self.window_height - box_height) / 2)

        pad_x = -x if x < 0 else 0
        pad_y = -y if y < 0 else 0
        win_x = 0 if x < 0 else x
        win_y = 0 if y < 0 else y
        win_width = self.window_width if x < 0 else box_width
        win_height = self.window_height if y < 0 else box_height

        self._pad.refresh(pad_y, pad_x, win_y, win_x,
                          win_y + win_height - 1, win_x + win_width - 1)

    def close(self):
        self.curses.nocbreak()
        self._screen.keypad(0)
        self.curses.echo()
        self.curses.endwin()


class BrowserContext(Context):
    def open(self, size):
        print('hello browser context')

    def close(self):
        pass
