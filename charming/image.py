from .core import CColor
from .core import CShape
from .core import Point
from .app import renderer
from .app import image_loader
from . import constants
from .cmath import map
from .common import get_bounding_rect_by_mode
from .common import add_on_return


#### Loading & Displaying

_pixels = []


@add_on_return
def image(img, a, b, c=None, d=None):
    c = img.width if c == None else c
    d = img.height if d == None else d
    x1, _, x2, y2, _, y3, _, _ = get_bounding_rect_by_mode(
        a, b, c, d, renderer.image_mode)

    x1 = int(x1)
    x2 = int(x2)
    y2 = int(y2)
    y3 = int(y3)
    w = x2 - x1 + 1
    h = y3 - y2 + 1

    points = []
    for y in range(y2, y3 + 1):
        for x in range(x1, x2 + 1):
            y0 = int(map(y, y2, y3 + 1, 0, img.height))
            x0 = int(map(x, x1, x2 + 1, 0, img.width))
            index = y0 * img.width + x0
            color = img[index]
            points.append(Point(x, y, color=color))

    options = {
        'width': w,
        'height': h
    }

    return CShape(points=points, primitive_type=constants.IMAGE, options=options)


def image_mode(mode):
    renderer.image_mode = mode


def load_image(src):
    return image_loader.load(src)


def no_tint():
    renderer.is_tint_enabled = False


def tint(ch=" ", fg=None, bg=None):
    renderer.is_tint_enabled = True
    c = CColor(ch, fg, bg)
    renderer.tint_color = c

# Pixels


def load_pixels():
    global _pixels
    _pixels = renderer.get_pixels()


def get_pixels():
    return _pixels


@add_on_return
def update_pixels():
    options = {
        'width': renderer.width,
        'height': renderer.height
    }
    return CShape(points=_pixels, primitive_type=constants.IMAGE, options=options, is_auto=False)
