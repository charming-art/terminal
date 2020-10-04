import sys
import math
import logging
from collections import namedtuple

logger = logging.getLogger(__name__)

Point = namedtuple('Point', ['x', 'y'])
Color = namedtuple('Color', ['ch', 'fg', 'bg'])


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

    shape_queue = []
    fill_color = Color(' ', 0, 0)
    stroke_color = Color('*', 0, 0)
    stroke_weight = 1
    is_stroke_enabled = True
    is_fill_enabled = True

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
        self.clear_buffer()
        self.context.open(self.size)
        self._update_pad_area()

    def draw(self):
        area = (self.pad_x, self.pad_y, self.win_x,
                self.win_y, self.win_width, self.win_height)
        self.clear_buffer()
        for shape in self.shape_queue:
            self.draw_shape(shape)

        self.shape_queue.clear()
        self.context.draw(self.buffer, area)

    def clear_buffer(self):
        width, height = self.size
        self.buffer = [Color(' ', 0, 0) for _ in range(width * height)]

    def get_events(self):
        def is_valid(e):
            if e.type == "mouse":
                e.x -= (self.win_x + 1)
                e.y -= (self.win_y + 1)
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

    def add_shape(self, shape):
        if shape.is_auto:
            shape.fill_color = self.fill_color
            shape.stroke_color = self.stroke_color
            shape.stroke_weight = self.stroke_weight
        self.shape_queue.append(shape)

    def draw_shape(self, shape):

        vertices = shape.vertices
        # transform

        # generate polygon
        points = None
        for i, _ in enumerate(vertices):
            if i < len(vertices) - 1:
                points = self.draw_line(vertices[i], vertices[i + 1])

        # fill polygon
        # logging.debug(points)
        content_width = self.win_width - 2
        content_height = self.win_height - 2

        # clip
        def is_in_canvas(p):
            return p.x >= 0 and p.x < content_width and p.y >= 0 and p.y < content_height

        points = [p for p in points if is_in_canvas(p)]

        # flush to buffer
        for p in points:
            index = p.x + p.y * content_width
            self.buffer[index] = Color('@', 0, 0)

    def draw_line(self, p1, p2):
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
