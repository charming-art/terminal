import string
import logging
from . import constants
from .core import Color
from .app import renderer
from .color import Color
from .color import no_fill
from .color import stroke
from .shape import point
from .shape import stroke_weight
from .structure import open_context


def text(text, x, y):
    matrix = _get_char_matrix(text)
    height = len(matrix)
    width = len(matrix[0]) if height > 0 else 0

    if renderer.text_align_x == constants.RIGHT:
        x -= width
    elif renderer.text_align_x == constants.CENTER:
        x -= width / 2

    if renderer.text_align_y == constants.BOTTOM:
        y -= height
    elif renderer.text_align_y == constants.MIDDLE:
        y -= height / 2

    with open_context():
        _, fg, bg = renderer.fill_color
        no_fill()
        for i, chars in enumerate(matrix):
            for j, ch in enumerate(chars):
                ch_size = _get_char_size()
                text_space_x = _get_space_x()
                text_space_y = _get_space_y()
                x0 = x + j * (ch_size + text_space_x)
                y0 = y + i * (ch_size + text_space_y)

                stroke(ch, fg, bg)
                stroke_weight(renderer.text_size - 1)
                point(x0, y0)


def text_width(text):
    matrix = _get_char_matrix(text)
    if len(matrix) > 0:
        ch_size = _get_char_size()
        text_space_x = _get_space_x()
        return ch_size + (len(matrix[0]) - 1) * (ch_size + text_space_x)
    return 0


def text_height(text):
    matrix = _get_char_matrix(text)
    ch_size = _get_char_size()
    text_space_y = _get_space_y()
    return ch_size + (len(matrix) - 1) * (ch_size + text_space_y)


def text_align(align_x=None, align_y=None):
    if align_x != None:
        renderer.text_align_x = align_x

    if align_y != None:
        renderer.text_align_y = align_y


def text_leading(leading):
    renderer.text_leading = leading


def text_size(size):
    renderer.text_size = size
    renderer.text_leading = size - 1


def text_space(space):
    renderer.text_space = space


def _get_char_matrix(text):
    lines = [line for line in text.split(
        '\n') if not line in string.whitespace]
    max_width = max([len(line) for line in lines])
    matrix = [[line[i] if i < len(line) else ' ' for i in range(
        max_width)] for line in lines]
    return matrix


def _get_char_size():
    return (renderer.text_size - 1) * 2 + 1


def _get_space_x():
    return renderer.text_size - 1 + renderer.text_space


def _get_space_y():
    return renderer.text_leading
