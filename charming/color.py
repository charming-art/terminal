from . import constants
from .core import CColor
from .app import renderer
from .utils import lerp_color as utils_lerp_color
from .utils import map


def stroke(ch=" ", fg=None, bg=None):
    renderer.is_stroke_enabled = True
    c = CColor(ch, fg, bg)
    renderer.stroke_color = c


def fill(ch=" ", fg=None, bg=None):
    renderer.is_fill_enabled = True
    if ch == " ":
        c = CColor.empty()
    else:
        c = CColor(ch, fg, bg)
    renderer.fill_color = c


def no_stroke():
    renderer.is_stroke_enabled = False


def no_fill():
    renderer.is_fill_enabled = False


def background(ch=" ", fg=None, bg=None):
    c = CColor(ch, fg, bg)
    renderer.background(c)


def color(ch=" ", fg=None, bg=None):
    return CColor(ch, fg, bg)


def ch(color):
    return color.ch


def fg(color):
    return color.fg


def bg(color):
    return color.bg


def lerp_color(start, stop, amt):
    if CColor.color_mode == constants.ANSI:
        start = map(start, 0, CColor.color_channels[0], 0, 255)
        stop = map(stop, 0, CColor.color_channels[0], 0, 255)

        start = CColor.ansi256_to_rgb(round(start))
        stop = CColor.ansi256_to_rgb(round(stop))

        r, g, b = utils_lerp_color([start, stop], amt)

        v = CColor.rgb_to_ansi256(r, g, b)
        v = map(v, 0, 255, 0, CColor.color_channels[0])
        return v
    else:
        start = (
            start[0] / CColor.color_channels[0],
            start[1] / CColor.color_channels[1],
            start[2] / CColor.color_channels[2],
        )
        stop = (
            stop[0] / CColor.color_channels[0],
            stop[1] / CColor.color_channels[1],
            stop[2] / CColor.color_channels[2],
        )

        if CColor.color_mode == constants.HSB:
            start = CColor.hsb_to_rgb(start[0], start[1], start[2])
            stop = CColor.hsb_to_rgb(stop[0], stop[1], stop[2])

        v1, v2, v3 = utils_lerp_color([start, stop], amt)

        if CColor.color_mode == constants.HSB:
            v1, v2, v3 = CColor.rgb_to_hsb(v1, v2, v3)

        v1, v2, v3 = [
            map(v, 0, 1, 0, CColor.color_channels[i])
            for i, v in enumerate([v1, v2, v3])
        ]
        return (v1, v2, v3)


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
