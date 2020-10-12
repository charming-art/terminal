import string
from .app import renderer
from .core import Color
from .shape import rect
from .shape import _rect_mode
from .shape import rect_mode
from .color import no_stroke
from .color import fill
from .structure import open_context
from .constants import LEFT
from .constants import CENTER
from .constants import RIGHT
from .constants import BOTTOM
from .constants import MIDDLE
from .constants import TOP
from .constants import CORNER


_text_size = 1
_text_leading = 1
_text_align_x = LEFT
_text_align_y = TOP


class CText(object):

    def __init__(self, x, y, chars):
        self.x = x
        self.y = y
        self.chars = chars
        self.fill_color = Color('', 0, 0)


def text(text, x, y):
    matrix = _get_char_matrix(text)
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0

    if _text_align_x == RIGHT:
        x -= width
    elif _text_align_x == CENTER:
        x -= width / 2

    if _text_align_y == BOTTOM:
        y -= height
    elif _text_align_y == MIDDLE:
        y -= height / 2

    old_rect_mode = _rect_mode
    rect_mode(CORNER)
    with open_context():
        _, fg, bg = renderer.fill_color
        no_stroke()
        for i, chars in enumerate(matrix):
            for j, ch in enumerate(chars):
                fill(ch, fg, bg)
                x0 = x + j * _text_size
                y0 = y + i * (_text_size + _text_leading - 1)
                rect(x0, y0, _text_size, _text_size)
    rect_mode(old_rect_mode)


def text_width(text):
    matrix = _get_char_matrix(text)
    if len(matrix) > 0:
        return len(matrix[0]) * _text_size
    return 0


def text_height(text):
    matrix = _get_char_matrix(text)
    return len(matrix) * _text_size


def text_align(align_x=None, align_y=None):
    global _text_align_x
    global _text_align_y

    if align_x != None:
        _text_align_x = align_x

    if align_y != None:
        _text_align_y = align_y


def text_leading(leading):
    global _text_leading
    _text_leading = leading


def text_size(size):
    global _text_size
    _text_size = size


def _get_char_matrix(text):
    lines = [line for line in text.split(
        '\n') if not line in string.whitespace]
    max_width = max([len(line) for line in lines])
    matrix = [[line[i] if i < len(line) else ' ' for i in range(
        max_width)] for line in lines]
    return matrix


# face = """
#     ______
#   .`      `.
#  /   -  -   \\
# |     __     |
# |            |
#  \\          /
#   '.______.'
# """

# print(_get_char_matrix(face))
