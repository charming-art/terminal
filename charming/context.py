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

    def open(self, size):
        self._screen = self.curses.initscr()
        self._screen.keypad(1)
        self.curses.noecho()
        self.curses.cbreak()

    def close(self):
        self._screen.keypad(0)
        self.curses.echo()
        self.curses.nocbreak()
        self.curses.endwin()


class BrowserContext(Context):
    def open(self, size):
        print('hello browser context')

    def close(self):
        pass
