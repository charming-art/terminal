from contextlib import contextmanager
from . import constants
from .app import renderer
from .core import Point
from .core import Shape
from .common import get_bounding_rect_by_mode
from .common import add_on_return
from .common import params_check


_current_shape = None
is_curve = False
is_bezier = False
is_contour = False
_curve_tightness = 0


#### primitives #####
@add_on_return
@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def line(x1, y1, x2, y2):
    return Shape(points=[Point(x1, y1), Point(x2, y2)], close_mode=constants.OPEN)


@add_on_return
@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    return Shape(points=[Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)])


@add_on_return
@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float)
)
def triangle(x1, y1, x2, y2, x3, y3):
    return Shape(points=[Point(x1, y1), Point(x2, y2), Point(x3, y3)])


@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def rect(a, b, c, d):
    x1, y1, x2, y2, x3, y3, x4, y4 = get_bounding_rect_by_mode(
        a, b, c, d, renderer.rect_mode
    )
    quad(x1, y1, x2, y2, x3, y3, x4, y4)


@params_check(
    (int, float),
    (int, float),
    (int, float),
)
def square(x, y, extend):
    rect(x, y, extend, extend)


@add_on_return
@params_check(
    (int, float),
    (int, float),
)
def point(x, y):
    return Shape(points=[Point(x, y)], primitive_type=constants.POINTS)


@add_on_return
@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    mode=int
)
def arc(a, b, c, d, start, stop, mode=constants.OPEN):
    x1, y1, x2, y2, x3, y3, x4, y4 = get_bounding_rect_by_mode(
        a, b, c, d, renderer.ellipse_mode
    )

    points = [Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)]
    options = {
        'start': start,
        'stop': stop,
        'mode': mode
    }
    return Shape(points=points, options=options, primitive_type=constants.ARC)


@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def ellipse(a, b, c, d):
    arc(a, b, c, d, 0, constants.TAU, constants.CHORD)


@params_check(
    (int, float),
    (int, float),
    (int, float),
)
def circle(x, y, extend):
    ellipse(x, y, extend, extend)

#### vertex ####


@params_check(primitive_type=int)
def begin_shape(primitive_type=constants.POLYGON):
    global _current_shape
    global is_bezier
    global is_contour
    global is_curve
    is_contour = False
    is_bezier = False
    is_curve = False
    _current_shape = Shape(primitive_type=primitive_type)


@add_on_return
@params_check(close_mode=int)
def end_shape(close_mode=constants.OPEN):
    global _current_shape
    _current_shape.close_mode = close_mode
    if is_bezier:
        _current_shape.primitive_type = constants.BEZIER
    elif is_curve:
        _current_shape.primitive_type = constants.CURVE
        _current_shape.options['curve_tightness'] = _curve_tightness
    return _current_shape


@contextmanager
@params_check(
    primitive_type=int,
    close_mode=int
)
def open_shape(primitive_type=constants.POLYGON, close_mode=constants.OPEN):
    begin_shape(primitive_type)
    yield
    end_shape(close_mode)


def begin_contour():
    global is_contour
    is_contour = True


def end_contour():
    global is_contour
    global _current_shape
    is_contour = False
    # close the contour
    contour_points = [p for p in _current_shape.points if p.type == "contour"]
    first_point = contour_points[0]
    last_point = contour_points[-1]
    if first_point.x != last_point.x or first_point.y != last_point.y:
        _current_shape.points.append(
            Point(first_point.x, first_point.y, type="contour")
        )


@contextmanager
def open_contour():
    begin_contour()
    yield
    end_contour()


@params_check(
    (int, float),
    (int, float)
)
def vertex(x, y):
    global _current_shape
    if is_contour:
        p = Point(x, y, type="contour")
    else:
        p = Point(x, y)
    _current_shape.points.append(p)


@params_check(
    (int, float),
    (int, float)
)
def curve_vertex(x, y):
    global _current_shape
    global is_curve
    is_curve = True
    _current_shape.points.append(Point(x, y, type="curve"))


@params_check(
    (int, float)
)
def curve_tightness(v):
    global _curve_tightness
    _curve_tightness = v


@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def bezier_vertex(x2, y2, x3, y3, x4, y4):
    global is_bezier
    is_bezier = True
    global _current_shape
    _current_shape.points.append(Point(x2, y2, type="bezier"))
    _current_shape.points.append(Point(x3, y3, type="bezier"))
    _current_shape.points.append(Point(x4, y4, type="bezier"))


#### curves #####

@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def curve(x1, y1, x2, y2, x3, y3, x4, y4):
    begin_shape()
    curve_vertex(x1, y1)
    curve_vertex(x2, y2)
    curve_vertex(x3, y3)
    curve_vertex(x4, y4)
    end_shape()


@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def curve_point(n1, n2, n3, n4, t):
    s = 1 - _curve_tightness
    t3 = t ** 3
    t2 = t ** 2
    t1 = t
    t0 = 1
    a = -s * t3 + 2 * s * t2 - s * t1
    b = (2 - s) * t3 + (s - 3) * t2 + 1 * t0
    c = (s - 2) * t3 + (3 - 2 * s) * t2 + s * t1
    d = s * t3 - s * t2
    return a * n1 + b * n2 + c * n3 + d * n4


@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def curve_tangent(n1, n2, n3, n4, t):
    s = 1 - _curve_tightness
    t3 = 3 * t ** 2
    t2 = 2 * t
    t1 = 1
    t0 = 0
    a = -s * t3 + 2 * s * t2 - s * t1
    b = (2 - s) * t3 + (s - 3) * t2 + 1 * t0
    c = (s - 2) * t3 + (3 - 2 * s) * t2 + s * t1
    d = s * t3 - s * t2
    return a * n1 + b * n2 + c * n3 + d * n4


@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def bezier(x1, y1, x2, y2, x3, y3, x4, y4):
    begin_shape()
    vertex(x1, y1)
    bezier_vertex(x2, y2, x3, y3, x4, y4)
    end_shape()


@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def bezier_point(n1, n2, n3, n4, t):
    a = (1 - t) ** 3
    b = 3 * t * (1 - t) ** 2
    c = 3 * t ** 2 * (1 - t)
    d = t ** 3
    return a * n1 + b * n2 + c * n3 + d * n4


@params_check(
    (int, float),
    (int, float),
    (int, float),
    (int, float),
    (int, float),
)
def bezier_tangent(n1, n2, n3, n4, t):
    a = -3 * (1 - t) ** 2
    b = 3 * (1 - t) ** 2 - 6 * t * (1 - t)
    c = 6 * t * (1 - t) - 3 * t ** 2
    d = 3 * t ** 2
    return a * n1 + b * n2 + c * n3 + d * n4


#### attributes ####

@params_check(mode=int)
def rect_mode(mode=constants.CORNER):
    renderer.rect_mode = mode


@params_check(mode=int)
def ellipse_mode(mode=constants.CENTER):
    renderer.ellipse_mode = mode


@params_check(
    weight=(int, float)
)
def stroke_weight(weight=0):
    renderer.stroke_weight = int(weight)
