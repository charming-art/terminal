import functools

from .app import renderer
from .core import Point


class CShape(object):

    fill_color = None
    stroke_color = None
    stroke_weight = None

    def __init__(self, vertices=[], is_auto=True):
        self.vertices = vertices
        self.is_auto = is_auto


def set_render_parameters(foo):
    @functools.wraps(foo)
    def wrapped(*args, **kw):
        shape = foo(*args, **kw)
        renderer.add_shape(shape)
    return wrapped


@set_render_parameters
def line(x1, y1, x2, y2):
    return CShape(vertices=[Point(x1, y1), Point(x2, y2)])
