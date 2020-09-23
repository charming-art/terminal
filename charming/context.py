from abc import ABCMeta, abstractclassmethod


class Context(metaclass=ABCMeta):
    @abstractclassmethod
    def open(self):
        """ open the drawing context"""


class WindowsContext(Context):
    def open(self):
        print('hello windows context')


class CursesContext(Context):
    def open(self):
        print('hello curses context')


class BrowserContext(Context):
    def open(self):
        print('hello browser context')
