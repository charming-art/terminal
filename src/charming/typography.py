from pyfiglet import FigletFont
from . import constants
from .app import renderer
from .common import add_on_return
from .core import Text
from .common import params_check


@params_check(str)
def text_font(font_family):
    renderer.text_font = font_family


def get_font_list():
    return FigletFont().getFonts()


@add_on_return
@params_check(
    (str, int, float),
    (int, float),
    (int, float)
)
def text(text, x, y):
    if isinstance(text, int) or isinstance(text, float):
        text = str(text)
    return Text(text, x, y, renderer.mode)


@params_check(str)
def text_width(text):
    return Text.text_width(text, renderer.text_size, renderer.text_font)


@params_check(str)
def text_height(text):
    return Text.text_height(text, renderer.text_size, renderer.text_font)


@params_check(
    align_x=int,
    align_y=int
)
def text_align(align_x=None, align_y=None):
    if align_x != None:
        renderer.text_align_x = align_x

    if align_y != None:
        renderer.text_align_y = align_y


@params_check(size=int)
def text_size(size=constants.NORMAL):
    renderer.text_size = size
