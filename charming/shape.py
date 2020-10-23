import functools
from . import constants
from .app import renderer
from .core import Point
from .core import CShape


_current_shape = None
is_curve = False
is_bezier = False
is_contour = False


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
        a, b, c, d, renderer.rect_mode)
    quad(x1, y1, x2, y2, x3, y3, x4, y4)


def square(x, y, extend):
    rect(x, y, extend, extend)


@_add_on_return
def point(x, y):
    return CShape(points=[Point(x, y)], primitive_type=constants.POINTS)


@_add_on_return
def arc(a, b, c, d, start, stop, mode=constants.OPEN):
    x1, y1, x2, y2, x3, y3, x4, y4 = _get_bounding_rect_by_mode(
        a, b, c, d, renderer.ellipse_mode)

    points = [Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)]
    options = {
        'start': start,
        'stop': stop,
        'mode': mode
    }
    return CShape(points=points, options=options)


def ellipse(a, b, c, d):
    arc(a, b, c, d, 0, constants.TAU, constants.CHORD)


def circle(x, y, extend):
    ellipse(x, y, extend, extend)


def _get_bounding_rect_by_mode(a, b, c, d, mode):
    if mode == constants.RADIUS:
        x1 = a - c
        y1 = b - d
        x2 = a + c
        y2 = b - d
        x3 = a + c
        y3 = b + d
        x4 = a - c
        y4 = b + d
    elif mode == constants.CORNERS:
        x1 = a
        y1 = b
        x2 = c
        y2 = b
        x3 = c
        y3 = d
        x4 = a
        y4 = d
    elif mode == constants.CENTER:
        x1 = a - c / 2
        y1 = b - d / 2
        x2 = a + c / 2
        y2 = b - d / 2
        x3 = a + c / 2
        y3 = b + d / 2
        x4 = a - c / 2
        y4 = b + d / 2
    else:
        x1 = a
        y1 = b
        x2 = a + c
        y2 = b
        x3 = a + c
        y3 = b + d
        x4 = a
        y4 = b + d
    return (x1, y1, x2, y2, x3, y3, x4, y4)

#### vertex ####


def begin_shape(primitive_type=constants.POLYGON):
    global _current_shape
    global is_bezier
    global is_contour
    global is_curve
    is_contour = False
    is_bezier = False
    is_curve = False
    _current_shape = CShape(primitive_type=primitive_type)


@ _add_on_return
def end_shape(close_mode=constants.OPEN):
    global _current_shape
    _current_shape.close_mode = close_mode
    return _current_shape


def begin_contour():
    global is_contour
    is_contour = True


def end_contour():
    pass


def vertex(x, y):
    global _current_shape
    _current_shape.points.append(Point(x, y))


def curve_vertex(x, y):
    global _current_shape
    global is_curve
    is_curve = True
    _current_shape.points.append(Point(x, y, type="curve"))


def curve_tightness(v):
    pass


def bezier_vertex():
    global is_bezier
    is_bezier = True


#### curves #####


def curve():
    pass


def curve_point():
    pass


def curve_tangent():
    pass


def bezier():
    pass


def bezier_point():
    pass


def bezier_tangent():
    pass


#### attributes ####


def rect_mode(mode=constants.CORNER):
    renderer.rect_mode = mode


def ellipse_mode(mode=constants.CENTER):
    renderer.ellipse_mode = mode


def stroke_weight(weight=0):
    renderer.stroke_weight = weight
