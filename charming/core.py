import time
import logging
import math
import sys
from collections import namedtuple
from abc import ABCMeta, abstractclassmethod
from .constants import POINTS
from .constants import POLYGON
from .constants import CLOSE
from .constants import CORNER
from .constants import CENTER
from .constants import LEFT
from .constants import TOP
from .cmath import map
from .cmath import Matrix


logger = logging.getLogger(__name__)

Point = namedtuple('Point', ['x', 'y'])
Color = namedtuple('Color', ['ch', 'fg', 'bg'])
Vertex = namedtuple('Vertex', ['x', 'y', 'color'])


class Sketch(object):

    def __init__(self, renderer, context):
        self.renderer = renderer
        self.context = context

        self.frame_rate = 30
        self.is_loop = True
        self.frame_count = 0
        self.size = (10, 10)
        self.key = 0
        self.key_code = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.pmouse_x = 0
        self.pmouse_y = 0
        self.hooks_map = {
            'setup': lambda: None,
            'draw': lambda: None,
            'mouse_clicked': lambda: None,
            'key_typed': lambda: None,
            'window_resized': lambda: None,
        }

    def run(self):
        error = None
        try:
            setup_hook = self.hooks_map['setup']
            draw_hook = self.hooks_map['draw']

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
            error = e
        finally:
            self.context.close()
            print(error)

    def add_hook(self, name, hook):
        self.hooks_map[name] = hook

    def _handle_event(self, e):
        if e.type == 'mouse':
            self.pmouse_x = self.mouse_x
            self.pmouse_y = self.mouse_y
            self.mouse_x = e.x
            self.mouse_y = e.y
            mouse_hook = self.hooks_map['mouse_clicked']
            mouse_hook()
        elif e.type == "window":
            window_hook = self.hooks_map['window_resized']
            window_hook()
        elif e.type == "keyboard":
            self.key = e.key
            keyTyped_hook = self.hooks_map['key_typed']
            keyTyped_hook()


class Renderer(object):

    def __init__(self):
        self.frame_buffer = []
        self.shape_queue = []

        # styles
        self.fill_color = Color(' ', None, None)
        self.stroke_color = Color('*', None, None)
        self.stroke_weight = 1
        self.is_stroke_enabled = True
        self.is_fill_enabled = True
        self.rect_mode = CORNER
        self.ellipse_mode = CENTER
        self.text_align_x = LEFT
        self.text_aligh_y = TOP
        self.text_leading = 1
        self.text_size = 1
        self.transform_matrix_stack = []

        self.size = (10, 10)

    def setup(self, size):
        self.size = size
        self._reset_frame_buffer()

    def render(self):
        while len(self.shape_queue) > 0:
            shape = self.shape_queue.pop(0)
            self._render_shape(shape)
        self.transform_matrix_stack.clear()

    def add_shape(self, shape):
        if shape.is_auto:
            shape.fill_color = self.fill_color
            shape.stroke_color = self.stroke_color
            shape.stroke_weight = self.stroke_weight
            shape.is_fill_enabled = self.is_fill_enabled
            shape.is_stroke_enabled = self.is_stroke_enabled
            shape.transform_matrix_stack = [
                m for m in self.transform_matrix_stack]
        self.shape_queue.append(shape)

    def set_frame_buffer(self, color):
        for i, _ in enumerate(self.frame_buffer):
            self.frame_buffer[i] = color

    def _reset_frame_buffer(self):
        width, height = self.size
        self.frame_buffer = [Color(' ', None, None)
                             for _ in range(width * height)]

    def _render_shape(self, shape):

        vertices = self._vertex_processing(
            shape.points,
            shape.stroke_color,
            shape.transform_matrix_stack)

        primitives = self._primitive_assembly(
            vertices,
            shape.primitive_type,
            shape.close_mode)

        fragments = self._rasterization(
            primitives,
            shape.fill_color,
            shape.is_stroke_enabled,
            shape.is_fill_enabled)

        fragments_clipped = self._clipping(fragments)

        self._fragment_processing(fragments_clipped)

    def _vertex_processing(self, points, stroke_color, transform_matrix_stack):
        # transform
        matrix_points = [Matrix([[p.x], [p.y], [1]]) for p in points]
        while len(transform_matrix_stack) > 0:
            matrix = transform_matrix_stack.pop()
            matrix_points = [matrix * p for p in matrix_points]
        transformed_points = [Point(p[0][0], p[1][0]) for p in matrix_points]

        # screen map && color
        vertices = [Vertex(int(p.x), int(p.y), stroke_color)
                    for p in transformed_points]
        return vertices

    def _primitive_assembly(self, vertices, primitive_type, close_mode):
        if primitive_type == POLYGON:
            if close_mode == CLOSE:
                vertices.append(vertices[0])
            primitives = [vertices]
        elif primitive_type == POINTS:
            primitives = [[v] for v in vertices]
        return primitives

    def _rasterization(self, primitives, fill_color, is_stroke_enabled, is_fill_enabled):
        fragments = []

        for vertices in primitives:
            pixels = []
            # fill polygon
            if is_fill_enabled and len(vertices) > 2:
                pixels += self._scan_line_filling(vertices, fill_color)

            # stroke polygon
            if is_stroke_enabled:
                if len(vertices) == 1:
                    pixels += vertices
                else:
                    for i, _ in enumerate(vertices):
                        if i < len(vertices) - 1:
                            pixels += self._draw_line(
                                vertices[i],
                                vertices[i + 1])
            fragments.append(pixels)

        return fragments

    def _clipping(self, fragments):
        fragments_clipped = []

        def is_in(p):
            content_width, content_height = self.size
            return p.x >= 0 and p.x < content_width and p.y >= 0 and p.y < content_height

        for pixels in fragments:
            pixels_clipped = [p for p in pixels if is_in(p)]
            fragments_clipped.append(pixels_clipped)

        return fragments_clipped

    def _fragment_processing(self, fragemnts):
        for pixels in fragemnts:
            for p in pixels:
                index = p.x + p.y * self.size[0]
                self.frame_buffer[index] = p.color

    def _scan_line_filling(self, polygon, fill_color):
        '''
        https://www.cs.uic.edu/~jbell/CourseNotes/ComputerGraphics/PolygonFilling.html
        '''

        # close the polygon
        polygon = polygon.copy()
        first = polygon[0]
        last = polygon[-1]
        if first.x != last.x or first.y != last.y:
            polygon.append(Vertex(first.x, first.y, first.color))

        pixels = []
        edges_horizontal = [(v, polygon[i + 1]) for i, v in enumerate(polygon)
                            if i < len(polygon) - 1 and v.y == polygon[i + 1].y]
        edges = [(v, polygon[i + 1])
                 for i, v in enumerate(polygon)
                 if i < len(polygon) - 1 and v.y != polygon[i + 1].y]
        ymin = min(polygon, key=lambda p: p.y).y
        ymax = max(polygon, key=lambda p: p.y).y

        def has_intersect(e, y):
            v1, v2 = e
            if v1.y > v2.y:
                return y <= v1.y and y > v2.y
            else:
                return y >= v1.y and y < v2.y

        for e in edges_horizontal:
            y = e[0].y
            pixels += self._draw_line(
                Vertex(e[0].x, y, fill_color),
                Vertex(e[1].x, y, fill_color))

        for y in range(ymin, ymax + 1):
            intersections = [round(map(y, e[0].y, e[1].y, e[0].x, e[1].x))
                             for e in edges if has_intersect(e, y)]
            if len(intersections) == 1:
                pixels += [Vertex(intersections[0], y, fill_color)]
            else:
                intersections_sorted = sorted(intersections)
                is_draw = True
                for i, x0 in enumerate(intersections_sorted):
                    if is_draw and i < len(intersections_sorted) - 1:
                        x1 = intersections_sorted[i + 1]
                        pixels += self._draw_line(
                            Vertex(x0, y, fill_color),
                            Vertex(x1, y, fill_color))
                    is_draw = not is_draw
        return pixels

    def _draw_line(self, v1, v2):
        pixels = []

        dx = abs(v1.x - v2.x)
        dy = abs(v1.y - v2.y)

        if dx >= dy:
            start_x = min(v1.x, v2.x)
            end_x = max(v1.x, v2.x)
            for x in range(start_x, end_x + 1):
                y = map(x, v1.x, v2.x, v1.y, v2.y)
                pixels.append(Vertex(x, round(y), v1.color))
        else:
            start_y = min(v1.y, v2.y)
            end_y = max(v1.y, v2.y)
            for y in range(start_y, end_y + 1):
                x = map(y, v1.y, v2.y, v1.x, v2.x)
                pixels.append(Vertex(round(x), y, v1.color))

        return pixels


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

        window_height = 0

        def __init__(self):
            self._screen = curses.initscr()
            self._screen.keypad(1)
            self._screen.nodelay(1)
            self.window_width = self._screen.getmaxyx()[1]
            self.window_height = self._screen.getmaxyx()[0]
            self._screen.refresh()
            self._screen.leaveok(False)
            self._buffer = []
            self.color_pair = []

            curses.noecho()
            curses.cbreak()

            # Enable mouse events
            curses.mousemask(curses.ALL_MOUSE_EVENTS |
                             curses.REPORT_MOUSE_POSITION)

        def open(self, size):
            curses.start_color()  # Enables colors

            # for i, c in enumerate(self.color_pair):
            #     curses.init_pair(i, c.fg, c.bg)

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
                    x -= (self._canvas_x - self._pad_x + 1)
                    y -= (self._canvas_y - self._pad_y + 1)
                    x_in = x >= 0 and x < self._canvas_width - 1
                    y_in = y >= 0 and y < self._canvas_height - 1
                    if x_in and y_in:
                        event_queue.append(MouseEvent(x, y, bstate))
                else:
                    event_queue.append(KeyboardEvent(key))
                key = self._screen.getch()
            return event_queue

        def draw(self, buffer=None):
            if buffer == None:
                buffer = self._buffer
            else:
                self._buffer = buffer
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
            self.draw()


class Event(object):
    type = ""

    def __init__(self, type):
        self.type = type


class WindowEvent(Event):
    def __init__(self):
        super(WindowEvent, self).__init__('window')


class MouseEvent(Event):
    mouse_type = ""

    def __init__(self, x, y, type):
        super(MouseEvent, self).__init__('mouse')
        self.x = x
        self.y = y
        self.mouse_type = type


class KeyboardEvent(Event):

    def __init__(self, key):
        super(KeyboardEvent, self).__init__('keyboard')
        self.key = key
