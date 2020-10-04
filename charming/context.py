import sys
from abc import ABCMeta, abstractclassmethod
from .event import MouseEvent
from .event import KeyboardEvent
from .event import WindowEvent


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
    def get_events(self):
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


if sys.platform == "win32":
    class WindowsContext(Context):
        def open(self, size):
            print('hello windows context')

        def close(self):
            pass

        def no_cursor(self):
            pass

        def cursor(self):
            pass

        def get_events(self):
            pass

        def resize(self):
            pass

        def clear(self):
            pass

        def draw(self, buffer, area):
            pass

elif sys.platform == "brython":
    class BrowserContext(Context):

        def open(self, size):
            print('hello browser context')

        def close(self):
            pass

        def no_cursor(self):
            pass

        def cursor(self):
            pass

        def get_events(self):
            pass

        def resize(self):
            pass

        def clear(self):
            pass

        def draw(self, buffer, area):
            pass

else:
    import curses

    class CursesContext(Context):

        _screen = None

        _pad = None

        window_width = 0

        window_height = 0

        has_resized = False

        def __init__(self):
            self._screen = curses.initscr()
            self._screen.keypad(1)
            self._screen.nodelay(1)
            self.window_width = self._screen.getmaxyx()[1]
            self.window_height = self._screen.getmaxyx()[0]
            self._screen.refresh()
            self._screen.leaveok(False)

            curses.noecho()
            curses.cbreak()

            # Enable mouse events
            curses.mousemask(curses.ALL_MOUSE_EVENTS |
                             curses.REPORT_MOUSE_POSITION)

        def open(self, size):
            content_width, content_height = size
            self._pad = curses.newpad(
                content_height + 2,  content_width + 2)
            self._pad.border()

        def close(self):
            self._screen.keypad(0)
            curses.nocbreak()
            curses.echo()
            curses.endwin()

        def no_cursor(self):
            curses.curs_set(0)

        def cursor(self):
            curses.curs_set(1)

        def get_events(self):
            event_queue = []
            key = self._screen.getch()
            while key != -1:
                if key == curses.KEY_RESIZE:
                    event_queue.append(WindowEvent())
                elif key == curses.KEY_MOUSE:
                    _, x, y, _, bstate = curses.getmouse()
                    event_queue.append(MouseEvent(x, y, bstate))
                else:
                    event_queue.append(KeyboardEvent(key))
                key = self._screen.getch()
            return event_queue

        def resize(self):
            curses.update_lines_cols()
            self.window_width = self._screen.getmaxyx()[1]
            self.window_height = self._screen.getmaxyx()[0]
            self.clear()

        def clear(self):
            self._screen.clear()
            self._screen.refresh()

        def draw(self, buffer, area):
            pad_x, pad_y, win_x, win_y, win_width, win_height = area

            content_width = win_width - 2
            x_offset = 1
            y_offset = 1
            for i, color in enumerate(buffer):
                x = i % content_width + x_offset
                y = i // content_width + y_offset
                self._pad.addch(y, x, color.ch)

            self._pad.refresh(pad_y, pad_x, win_y, win_x,
                              win_y + win_height - 1, win_x + win_width - 1)
