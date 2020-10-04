import time
import logging
import math
import sys
from collections import namedtuple
from abc import ABCMeta, abstractclassmethod


logger = logging.getLogger(__name__)


class Sketch(object):
    renderer = None
    context = None

    frame_rate = 30
    is_loop = True
    frame_count = 0
    size = (0, 0)

    key = 0
    key_code = 0
    mouse_x = 0
    mouse_y = 0
    pmouse_x = 0
    pmouse_y = 0

    _hooks_map = {
        'setup': lambda: None,
        'draw': lambda: None,
        'mouse_clicked': lambda: None,
        'key_typed': lambda: None,
        'window_resized': lambda: None,
    }

    def __init__(self, renderer, context):
        self.renderer = renderer
        self.context = context

    def run(self):
        try:
            setup_hook = self._hooks_map['setup']
            draw_hook = self._hooks_map['draw']

            if not setup_hook or not draw_hook:
                return

            setup_hook()
            self.context.open(self.size)
            self.renderer.setup(self.size)

            while True:
                events = self.context.get_events()
                for e in events:
                    self._handle_event(e)

                if self.is_loop:
                    draw_hook()
                    self.renderer.render()
                    self.context.draw(self.renderer.frame_buffer)

                self.frame_count += 1
                time.sleep(1 / self.frame_rate)
        except Exception as e:
            logger.debug(e)
        finally:
            self.context.close()

    def add_hook(self, name, hook):
        self._hooks_map[name] = hook

    def _handle_event(self, e):
        if e.type == 'mouse':
            self.pmouse_x = self.mouse_x
            self.pmouse_y = self.mouse_y
            self.mouse_x = e.x
            self.mouse_y = e.y
            mouse_hook = self._hooks_map['mouse_clicked']
            mouse_hook()
        elif e.type == "window":
            window_hook = self._hooks_map['window_resized']
            window_hook()
        elif e.type == "keyboard":
            self.key = e.key
            keyTyped_hook = self._hooks_map['key_typed']
            keyTyped_hook()


Point = namedtuple('Point', ['x', 'y'])
Color = namedtuple('Color', ['ch', 'fg', 'bg'])


class Renderer(object):

    size = (10, 10)
    frame_buffer = []
    shape_queue = []
    fill_color = Color(' ', 0, 0)
    stroke_color = Color('*', 0, 0)
    stroke_weight = 1
    is_stroke_enabled = True
    is_fill_enabled = True

    def __init__(self):
        pass

    def setup(self, size):
        self.size = size

    def render(self):
        self._reset_frame_buffer()
        while len(self.shape_queue) > 0:
            shape = self.shape_queue.pop(0)
            vertices = self._vertex_processing(shape)
            primitives = self._primitive_assembly(vertices)
            fragments = self._rasterization(primitives)
            fragments_clipped = self._clipping(fragments)
            self._fragment_processing(fragments_clipped)

    def add_shape(self, shape):
        if shape.is_auto:
            shape.fill_color = self.fill_color
            shape.stroke_color = self.stroke_color
            shape.stroke_weight = self.stroke_weight
        self.shape_queue.append(shape)

    def _reset_frame_buffer(self):
        width, height = self.size
        self.frame_buffer = [Color(' ', 0, 0) for _ in range(width * height)]

    def _vertex_processing(self, shape):
        return shape.vertices

    def _primitive_assembly(self, vertices):
        primitives = [vertices]
        return primitives

    def _rasterization(self, primitives):
        fragments = []
        for vertices in primitives:
            points = None
            for i, _ in enumerate(vertices):
                if i < len(vertices) - 1:
                    points = self._draw_line(vertices[i], vertices[i + 1])
            fragments.append(points)
        return fragments

    def _clipping(self, fragments):
        fragments_clipped = []
        for points in fragments:
            content_width, content_height = self.size

            def is_in(p):
                return p.x >= 0 and p.x < content_width and p.y >= 0 and p.y < content_height

            points_clipped = [p for p in points if is_in(p)]
            fragments_clipped.append(points_clipped)
        return fragments_clipped

    def _fragment_processing(self, fragemnts):
        for points in fragemnts:
            for p in points:
                index = p.x + p.y * self.size[0]
                self.frame_buffer[index] = Color('@', 0, 0)

    def _draw_line(self, p1, p2):
        points = []

        def map(value, start1, stop1, start2, stop2):
            if start1 == stop1:
                return value
            t = (value - start1) / (stop1 - start1)
            return start2 * (1 - t) + stop2 * t

        def round(value):
            return math.floor(value) if value - math.floor(value) < 0.5 else math.ceil(value)

        dx = abs(p1.x - p2.x)
        dy = abs(p1.y - p2.y)

        if dx >= dy:
            start_x = min(p1.x, p2.x)
            end_x = max(p1.x, p2.x)
            for x in range(start_x, end_x + 1):
                y = map(x, p1.x, p2.x, p1.y, p2.y)
                points.append(Point(x, round(y)))
        else:
            start_y = min(p1.y, p2.y)
            end_y = max(p1.y, p2.y)
            for y in range(start_y, end_y + 1):
                x = map(y, p1.y, p2.y, p1.x, p2.x)
                points.append(Point(round(x), y))

        return points


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
    def draw(self, buffer):
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

        def draw(self, buffer):
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

        def draw(self, buffer):
            pass

else:
    import curses

    class CursesContext(Context):

        _screen = None

        _pad = None

        _pad_x = 0

        _pad_y = 0

        _pad_width = 0

        _pad_height = 0

        _canvas_x = 0

        _canvas_y = 0

        _canvas_width = 0

        _canvas_height = 0

        window_width = 0

        window_height = 0

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
            self._pad_width = size[0] + 2
            self._pad_height = size[1] + 2
            self._pad = curses.newpad(
                self._pad_height, self._pad_width)
            self._pad.border()
            self._update_canvas()

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
                    self._resize()
                    event_queue.append(WindowEvent())
                elif key == curses.KEY_MOUSE:
                    _, x, y, _, bstate = curses.getmouse()
                    x -= (-self._pad_x + 1)
                    y -= (-self._pad_y + 1)
                    x_in = x >= 0 and x < self._canvas_width - 1
                    y_in = y >= 0 and y < self._canvas_height - 1
                    if x_in and y_in:
                        event_queue.append(MouseEvent(x, y, bstate))
                else:
                    event_queue.append(KeyboardEvent(key))
                key = self._screen.getch()
            return event_queue

        def draw(self, buffer):
            content_width = self._pad_width - 2
            x_offset = 1
            y_offset = 1

            for i, color in enumerate(buffer):
                x = i % content_width + x_offset
                y = i // content_width + y_offset
                self._pad.addch(y, x, color.ch)

            self._pad.refresh(self._pad_y, self._pad_x, self._canvas_y, self._canvas_x,
                              self._canvas_y + self._canvas_height - 1, self._canvas_x + self._canvas_width - 1)

        def _update_canvas(self):
            x = (self.window_width - self._pad_width) // 2
            y = (self.window_height - self._pad_height) // 2

            self._pad_x = -x if x < 0 else 0
            self._pad_y = -y if y < 0 else 0
            self._canvas_x = 0 if x < 0 else x
            self._canvas_y = 0 if y < 0 else y
            self._canvas_width = self.window_width if x <= 0 else self._pad_width
            self._canvas_height = self.window_height if y <= 0 else self._pad_height

        def _resize(self):
            curses.update_lines_cols()
            self.window_width = self._screen.getmaxyx()[1]
            self.window_height = self._screen.getmaxyx()[0]
            self._update_canvas()
            self._screen.clear()
            self._screen.refresh()


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
