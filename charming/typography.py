import string
import functools
from pyfiglet import Figlet
from pyfiglet import FigletFont
from . import constants
from .app import renderer
from .color import no_fill
from .color import stroke
from .shape import point
from .shape import stroke_weight
from .structure import open_context
from .common import add_on_return
from .core import CShape
from .core import CColor
from .core import Point
from .core import logger
from .utils import Matrix

_font_list = FigletFont().getFonts()


def _preprocess_text(foo):
    @functools.wraps(foo)
    def wrapped(text, *args, **kw):
        if renderer.text_size == constants.BIG:
            f = Figlet(font=renderer.text_font)
            text = f.renderText(text)
        elif renderer.text_size == constants.LARGE:
            f = Figlet(font=renderer.text_font)
        return foo(text, *args, **kw)
    return wrapped


def text_font(font_family):
    renderer.text_font = font_family


def get_font_list():
    return _font_list


@add_on_return
@_preprocess_text
def text(text, x, y):
    matrix = _matrixlize(text)
    height = matrix.row
    width = matrix.col

    if renderer.text_align_x == constants.RIGHT:
        x -= width
    elif renderer.text_align_x == constants.CENTER:
        x -= width / 2

    if renderer.text_align_y == constants.BOTTOM:
        y -= height
    elif renderer.text_align_y == constants.MIDDLE:
        y -= height / 2

    points = []
    for i, chars in enumerate(matrix):
        for j, ch in enumerate(chars):
            x0 = x + j
            y0 = y + i
            color = CColor(ch)
            points.append(Point(x0, y0, color=color))

    return CShape(points=points, primitive_type=constants.TEXT)


@_preprocess_text
def text_width(text):
    matrix = _matrixlize(text)
    return matrix.col


@_preprocess_text
def text_height(text):
    matrix = _matrixlize(text)
    return matrix.row


def text_align(align_x=None, align_y=None):
    if align_x != None:
        renderer.text_align_x = align_x

    if align_y != None:
        renderer.text_align_y = align_y


def text_size(size=constants.NORMAL):
    renderer.text_size = size


def _matrixlize(text):
    lines = [
        line for line in text.split('\n')
        if not line in string.whitespace
    ]
    if len(lines) == 0:
        return [[]]

    max_width = max([len(line) for line in lines])
    matrix = [
        [line[i] if i < len(line) else ' '
         for i in range(max_width)]
        for line in lines
    ]
    return Matrix(matrix)
