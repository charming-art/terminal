from .app import renderer
from .app import context
from .core import Color
from functools import wraps


def _add_on_return(func):

    @wraps(func)
    def wrapped(*args, **kw):
        c = func(*args, **kw)

        def has_color(color_pair):
            _, fg, bg = c
            equal_colors = [
                color for color, enable in color_pair if color.fg == fg and color.bg == bg]
            return len(equal_colors) > 0

        if hasattr(context, 'color_pair'):
            if not has_color(context.color_pair):
                context.color_pair.append([c, False])
        return c

    return wrapped


@_add_on_return
def stroke(ch, fg=None, bg=None):
    renderer.is_stroke_enabled = True
    c = Color(ch, fg, bg)
    renderer.stroke_color = c
    return c


@_add_on_return
def fill(ch, fg=None, bg=None):
    renderer.is_fill_enabled = True
    c = Color(ch, fg, bg)
    renderer.fill_color = c
    return c


def no_stroke():
    renderer.is_stroke_enabled = False


def no_fill():
    renderer.is_fill_enabled = False


@_add_on_return
def backgournd(ch, fg=None, bg=None):
    c = Color(ch, fg, bg)
    renderer.set_frame_buffer(c)
    return c


@_add_on_return
def color(ch, fg=None, bg=None):
    return Color(ch, fg, bg)


def ch(color):
    return color.ch


def fg(color):
    return color.fg


def bg(color):
    return color.bg
