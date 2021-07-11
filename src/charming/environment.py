import types
from . import constants
from .app import sketch
from .app import renderer
from .common import params_check


@params_check(int)
def frame_rate(frame_rate):
    sketch.frame_rate = frame_rate


@params_check(
    (int, float),
    (int, float),
    mode=int
)
def size(width, height, mode=constants.SINGLE):
    scale = 2 if mode == constants.DOUBLE else 1
    sketch.context.open(int(width) * scale, int(height))
    sketch.renderer.init(mode)


@params_check(
    mode=int
)
def full_screen(mode=constants.SINGLE):
    sketch.context.open(is_full_screen=True)
    sketch.renderer.init(mode)


def get_window_size():
    return sketch.context.get_window_size()


def get_width():
    scale = 2 if renderer.mode == constants.DOUBLE else 1
    return int(sketch.context.width / scale)


def get_height():
    return sketch.context.height


def get_frame_count():
    return sketch.frame_count


def no_cursor():
    sketch.context.no_cursor()


def cursor():
    sketch.context.cursor()


@params_check(
    x=(int, float),
    y=(int, float)
)
def set_cursor(x=0, y=0):
    sketch.context.cursor_x = int(x)
    sketch.context.cursor_y = int(y)


@params_check(
    types.FunctionType
)
def window_resized(hook):
    sketch.add_hook('window_resized', hook)
