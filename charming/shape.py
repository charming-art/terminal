import functools

from .app import renderer
from .core import Point
from .constants import POLYGON
from .constants import OPEN
from .constants import CLOSE


_current_shape = None


class CShape(object):

    fill_color = None
    stroke_color = None
    stroke_weight = None
    primitive_type = POLYGON
    close_mode = OPEN
    transform_matrix_stack = []
    is_stroke_enabled = True
    is_fill_enabled = True

    def __init__(self, points=[], is_auto=True, primitive_type=POLYGON, close_mode=CLOSE):
        self.points = points
        self.is_auto = is_auto
        self.primitive_type = primitive_type
        self.close_mode = close_mode


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
