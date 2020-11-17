from .app import sketch
from .app import renderer
from . import constants


def frame_rate(frame_rate):
    sketch.frame_rate = frame_rate


def size(width, height, mode=constants.SINGLE):
    scale = 2 if mode == constants.DOUBLIE else 1
    sketch.context.open(int(width) * scale, int(height))
    sketch.renderer.init(mode)


def terminal_size(width, height, options=None):
    sketch.context.terminal_width = width
    sketch.context.terminal_height = height
    sketch.context.options = options


def full_terminal(options=None):
    terminal_size(
        sketch.context.inner_width,
        sketch.context.inner_height,
        options
    )


def full_screen(mode=constants.SINGLE):
    sketch.context.open(is_full_screen=True)
    sketch.renderer.init(mode)


def get_window_width():
    return sketch.context.window_width


def get_window_height():
    return sketch.context.window_height


def get_width():
    scale = 2 if renderer.mode == constants.DOUBLIE else 1
    return int(sketch.context.width / scale)


def get_height():
    return sketch.context.height


def get_frame_rate():
    return sketch.frame_rate


def get_frame_count():
    return sketch.frame_count


def no_cursor():
    sketch.context.no_cursor()


def cursor(x=0, y=0):
    sketch.context.cursor()
    sketch.context.cursor_x = x
    sketch.context.cursor_y = y


def window_resized(hook):
    sketch.add_hook('window_resized', hook)