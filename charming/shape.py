import functools
import logging
import math
from .app import renderer
from .core import Point
from .constants import POLYGON
from .constants import OPEN
from .constants import CLOSE
from .constants import CORNER
from .constants import CENTER
from .constants import CORNERS
from .constants import RADIUS
from .constants import TAU
from .constants import CHORD
from .constants import PIE
from .constants import PI
from .constants import HALF_PI


_current_shape = None
_rect_mode = CORNER
_ellipse_mode = CENTER


class CShape(object):

    def __init__(self, points=None, is_auto=True, primitive_type=POLYGON, close_mode=CLOSE):
        self.points = [] if points == None else points
        self.is_auto = is_auto
        self.primitive_type = primitive_type
        self.close_mode = close_mode
        self.fill_color = None
        self.stroke_color = None
        self.stroke_weight = None
        self.transform_matrix_stack = []
        self.is_stroke_enabled = True
        self.is_fill_enabled = True

    def __str__(self):
        attrs = {
            'fill_color': self.fill_color,
            'stroke_color': self.stroke_color,
            'primitive_type': self.primitive_type,
            'close_mode': self.close_mode,
            'is_stroke_enabled': self.is_stroke_enabled,
            'is_fill_enabled': self.is_fill_enabled,
            'stroke_weight': self.stroke_weight,
            'points': self.points
        }
        return attrs.__str__()

    __repr__ = __str__


def _add_on_return(foo):
    @functools.wraps(foo)
    def wrapped(*args, **kw):
        shape = foo(*args, **kw)
        renderer.add_shape(shape)
    return wrapped

#### primitives #####


@_add_on_return
def line(x1, y1, x2, y2):
    return CShape(points=[Point(x1, y1), Point(x2, y2)])


@_add_on_return
def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    return CShape(points=[Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)])


@_add_on_return
def triangle(x1, y1, x2, y2, x3, y3):
    return CShape(points=[Point(x1, y1), Point(x2, y2), Point(x3, y3)])


def rect(a, b, c, d):
    x1, y1, x2, y2, x3, y3, x4, y4 = _get_bounding_rect_by_mode(
        a, b, c, d, _rect_mode)
    quad(x1, y1, x2, y2, x3, y3, x4, y4)


def square(x, y, extend):
    rect(x, y, extend, extend)


@_add_on_return
def point(x, y):
    return CShape(points=[Point(x, y)])


@_add_on_return
def arc(a, b, c, d, start, stop, mode=OPEN):
    x1, y1, x2, _, _, _, _, y4 = _get_bounding_rect_by_mode(
        a, b, c, d, _ellipse_mode)
    x0 = int((x1 + x2) / 2)
    y0 = int((y1 + y4) / 2)
    a = int((x2 - x1) / 2)
    b = int((y4 - y1) / 2)
    p1 = []
    p2 = []
    p3 = []
    p4 = []

    def is_in(x, y):
        return (b * x) ** 2 + (a * y) ** 2 - (a * b) ** 2 < 0

    if a >= b:
        y = y0 - b
        for x in range(x0, x0 + a + 1):
            rx = x - x0
            ry = y0 - y
            p1.append(Point(x, y))
            p2.append(Point(x, y + ry * 2))
            p3.append(Point(x - rx * 2, y + ry * 2))
            p4.append(Point(x - rx * 2, y))
            if not is_in(rx + 1, ry - 0.5):
                y += 1
    else:
        x = x0 + a
        for y in range(y0, y0 + b + 1):
            rx = x - x0
            ry = y0 - y
            p1.append(Point(x, y))
            p2.append(Point(x - rx * 2, y))
            p3.append(Point(x - rx * 2, y + ry * 2))
            p4.append(Point(x, y + ry * 2))
            if not is_in(rx - 0.5, ry + 1):
                x -= 1

    points = list(reversed(p2)) + p3 + list(reversed(p4)) + p1
    close_mode = OPEN if mode == OPEN else CLOSE
    if mode == PIE:
        points.insert(0, Point(x0, y0))

    def is_between(x, left,  right):
        return left <= x and x <= right

    def x_range(start, stop, a):
        coss = [math.cos(start), math.cos(stop)]
        cos_max = 1 if is_between(0, start, stop) or is_between(
            TAU, start, stop) else max(coss)
        cos_min = -1 if is_between(PI, start, stop) else min(coss)
        return (a * cos_min, a * cos_max)

    def y_range(start, stop, b):
        sins = [math.sin(start), math.sin(stop)]
        sin_max = 1 if is_between(HALF_PI, start, stop) else max(sins)
        sin_min = -1 if is_between(PI + HALF_PI, start, stop) else min(sins)
        return (b * sin_min, b * sin_max)

    x_min, x_max = x_range(start, stop, a)
    y_min, y_max = y_range(start, stop, b)
    points_filterd = [p for p in points
                      if is_between(p.x - x0, x_min, x_max)
                      and is_between(p.y - y0, y_min, y_max)]

    return CShape(points=points_filterd, close_mode=close_mode)


def ellipse(a, b, c, d):
    arc(a, b, c, d, 0, TAU, CHORD)


def circle(x, y, extend):
    ellipse(x, y, extend, extend)


def _get_bounding_rect_by_mode(a, b, c, d, mode):
    if mode == RADIUS:
        x1 = a - c + 1
        y1 = b - d + 1
        x2 = a + c
        y2 = b - d + 1
        x3 = a + c
        y3 = b + d
        x4 = a - c + 1
        y4 = b + d
    elif mode == CORNERS:
        x1 = a
        y1 = b
        x2 = c
        y2 = b
        x3 = c
        y3 = d
        x4 = a
        y4 = d
    elif mode == CENTER:
        x1 = a - c / 2 + 1
        y1 = b - d / 2 + 1
        x2 = a + c / 2
        y2 = b - d / 2 + 1
        x3 = a + c / 2
        y3 = b + d / 2
        x4 = a - c / 2 + 1
        y4 = b + d / 2
    else:
        x1 = a
        y1 = b
        x2 = a + c - 1
        y2 = b
        x3 = a + c - 1
        y3 = b + d - 1
        x4 = a
        y4 = b + d - 1
    return (x1, y1, x2, y2, x3, y3, x4, y4)

#### vertex ####


def begin_shape(primitive_type=POLYGON):
    global _current_shape
    _current_shape = CShape(primitive_type=primitive_type)


@_add_on_return
def end_shape(close_mode=OPEN):
    global _current_shape
    _current_shape.close_mode = close_mode
    return _current_shape


def vertex(x, y):
    global _current_shape
    _current_shape.points.append(Point(x, y))

#### attributes ####


def rect_mode(mode=CORNER):
    global _rect_mode
    _rect_mode = mode


def ellipse_mode(mode=CENTER):
    global _ellipse_mode
    _ellipse_mode = mode
