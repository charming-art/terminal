from .app import renderer
from .core import Color


def stroke(ch, fg=0, bg=0):
    renderer.stroke_color = Color(ch, fg, bg)


def fill(ch, fg=0, bg=0):
    renderer.fill_color = Color(ch, fg, bg)


def ch(color):
    return color.ch


def fg(color):
    return color.fg


def bg(color):
    return color.bg
