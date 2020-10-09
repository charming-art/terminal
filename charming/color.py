from .app import renderer
from .core import Color


def stroke(ch, fg=0, bg=0):
    renderer.is_stroke_enabled = True
    renderer.stroke_color = Color(ch, fg, bg)


def fill(ch, fg=0, bg=0):
    renderer.is_fill_enabled = True
    renderer.fill_color = Color(ch, fg, bg)


def no_stroke():
    renderer.is_stroke_enabled = False


def no_fill():
    renderer.is_fill_enabled = False


def backgournd(ch, fg=0, bg=0):
    renderer.set_frame_buffer(Color(ch, fg, bg))


def color(ch, fg=0, bg=0):
    return Color(ch, fg, bg)


def ch(color):
    return color.ch


def fg(color):
    return color.fg


def bg(color):
    return color.bg
