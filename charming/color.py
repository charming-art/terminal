from .app import renderer
from .core import Color


def stroke(ch, fg=None, bg=None):
    renderer.is_stroke_enabled = True
    c = Color(ch, fg, bg)
    renderer.stroke_color = c


def fill(ch, fg=None, bg=None):
    renderer.is_fill_enabled = True
    c = Color(ch, fg, bg)
    renderer.fill_color = c


def no_stroke():
    renderer.is_stroke_enabled = False


def no_fill():
    renderer.is_fill_enabled = False


def background(ch, fg=None, bg=None):
    c = Color(ch, fg, bg)
    renderer.set_frame_buffer(c)


def color(ch, fg=None, bg=None):
    return Color(ch, fg, bg)


def ch(color):
    return color.ch


def fg(color):
    return color.fg


def bg(color):
    return color.bg
