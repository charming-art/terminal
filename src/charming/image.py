import sys
import copy
from .app import renderer
from .core import Color
from .core import Image
from .common import get_bounding_rect_by_mode
from .common import add_on_return
from .common import color_check
from .common import params_check
from .utils import logger
from .globals import BROWSER


#### Loading & Displaying

class CImage(object):

    def __init__(self, data, width, height):
        self._pixels = data
        self.pixels = []
        self.width = width
        self.height = height

    def load_pixels(self):
        self.pixels = [p for p in self._pixels]

    def update_pixels(self):
        self._pixels = [p for p in self.pixels]

    def copy(self):
        return copy.deepcopy(self)

    def __getitem__(self, index):
        return self._pixels[index]

    def __setitem__(self, key, value):
        self._pixels[key] = value

    def __repr__(self):
        attrs = {
            'pixels': self._pixels,
            'width': self.width,
            'height': self.height
        }
        return attrs.__repr__()

    __str__ = __repr__


@params_check(
    CImage,
    (int, float),
    (int, float),
    c=(int, float),
    d=(int, float)
)
@add_on_return
def image(img, a, b, c=None, d=None):
    c = img.width if c == None else c
    d = img.height if d == None else d
    x1, y1, x2, y2, _, y3, _, _ = get_bounding_rect_by_mode(
        a, b, c, d, renderer.image_mode)

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    y3 = int(y3)
    w = x2 - x1 + 1
    h = y3 - y2 + 1

    return Image(img, x1, y1, w, h)


@params_check(int)
def image_mode(mode):
    renderer.image_mode = mode


def no_tint():
    renderer.is_tint_enabled = False


@color_check
def tint(ch=" ", fg=None, bg=None):
    renderer.is_tint_enabled = True
    c = Color(ch, fg, bg)
    renderer.tint_color = c


if sys.platform == BROWSER:
    def load_image(src):
        return CImage([], 0, 0)

else:
    from PIL import Image as PImage

    @params_check(str)
    def load_image(src):
        image = PImage.open(src)
        w, h = image.size
        data = image.getdata()
        return CImage(data, w, h)
