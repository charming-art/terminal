from PIL import ImageSequence
from PIL import Image as PImage
from .app import renderer
from .core import Color
from .core import Image
from .common import get_bounding_rect_by_mode
from .common import add_on_return
from .common import color_check
from .common import params_check


#### Loading & Displaying

class CImage(object):

    def __init__(self, width=10, height=10, data=None):
        self._pixels = data if data else [[0, 0, 0, 1]] * width * height
        self.pixels = []
        self.width = width
        self.height = height

    def load_pixels(self):
        self.pixels = [p for p in self._pixels]

    def update_pixels(self):
        self._pixels = [p for p in self.pixels]

    def set(self, x, y, color):
        index = x + y * self.width
        self.pixels[index] = color

    def get(self, x, y):
        index = x + y * self.width
        return self.pixels[index]

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
    (int, float),
    (int, float)
)
@add_on_return
def image(img, a, b, c, d):
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


@params_check(str)
def load_image(src):
    image = PImage.open(src)
    images = []
    for frame in ImageSequence.Iterator(image):
        rgb_frame = frame.convert('RGBA')
        w, h = rgb_frame.size
        data = rgb_frame.getdata()
        images.append(CImage(w, h, data))
    return images[0] if len(images) == 1 else images
