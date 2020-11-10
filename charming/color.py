from . import constants
from .core import CColor
from .app import renderer


def stroke(ch=" ", fg=None, bg=None):
    renderer.is_stroke_enabled = True
    c = CColor(ch, fg, bg)
    renderer.stroke_color = c


def fill(ch=" ", fg=None, bg=None):
    renderer.is_fill_enabled = True
    if ch == " ":
        c = CColor.blank_fill()
    else:
        c = CColor(ch, fg, bg)
    renderer.fill_color = c


def no_stroke():
    renderer.is_stroke_enabled = False


def no_fill():
    renderer.is_fill_enabled = False


def background(ch=" ", fg=None, bg=None):
    c = CColor(ch, fg, bg)
    renderer.has_background_called = True
    renderer.background_color = c.bg
    renderer.set_frame_buffer(c)


def color(ch=" ", fg=None, bg=None):
    return CColor(ch, fg, bg)


def ch(color):
    return color.ch


def fg(color):
    return color.fg


def bg(color):
    return color.bg


def color_mode(mode=constants.ANSI, max1=None, max2=None, max3=None):
    CColor.color_mode = mode
    if mode == constants.ANSI:
        if max1 != None:
            CColor.color_channels = (max1,)
    else:
        if max1 != None and (max2 == None and max3 == None):
            CColor.color_channels = (max1, max1, max1)
        elif max1 != None and max2 != None and max3 != None:
            CColor.color_channels = (max1, max2, max3)
        else:
            if mode == constants.RGB:
                CColor.color_channels = (255, 255, 255)
            else:
                CColor.color_channels = (360, 100, 100)
