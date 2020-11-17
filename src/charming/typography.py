from pyfiglet import FigletFont
from . import constants
from .app import renderer
from .common import add_on_return
from .core import Text


def text_font(font_family):
    renderer.text_font = font_family


def get_font_list():
    return FigletFont().getFonts()


@add_on_return
def text(text, x, y):
    return Text(text, x, y)


def text_width(text):
    return Text.text_width(text, renderer.text_size, renderer.text_font)


def text_height(text):
    return Text.text_height(text, renderer.text_size, renderer.text_font)


def text_align(align_x=None, align_y=None):
    if align_x != None:
        renderer.text_align_x = align_x

    if align_y != None:
        renderer.text_align_y = align_y


def text_size(size=constants.NORMAL):
    renderer.text_size = size
