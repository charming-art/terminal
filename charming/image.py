from .core import CImage
from .core import ImageLoader
from .app import renderer

_pixels = None

#### Loading & Displaying


def image():
    pass


def image_mode():
    pass


def load_image():
    pass


def no_tint():
    pass


def tint():
    pass

# Pixels


def load_pixels():
    global _pixels
    _pixels = [p for p in renderer.frame_buffer]


def get_pixels():
    return _pixels


def update_pixels():
    renderer.frame_buffer = [p for p in _pixels]
