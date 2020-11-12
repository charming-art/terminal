import string
import functools
from pyfiglet import Figlet
from pyfiglet import FigletFont
from . import constants
from .app import renderer
from .common import add_on_return
from .core import CShape
from .core import CColor
from .core import Point
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
            matrix = _matrixlize(text)
            max_width_list = [-1 for _ in range(matrix.col)]
            max_height = -1
            total_width = 0
            steps = []

            for j in range(matrix.col):
                for i in range(matrix.row):
                    ftext = f.renderText(matrix[i][j])
                    m = _matrixlize(ftext, False)
                    max_width_list[j] = max(max_width_list[j], m.col)
                    max_height = max(max_height, m.row)
                    matrix[i][j] = m
                start = total_width
                end = start + max_width_list[j]
                total_width = end
                steps.append((start, end))

            def get_info(n):
                for i, (start, end) in enumerate(steps):
                    if n >= start and n < end:
                        return [i, start, end]
                return -1

            text = ""
            for i in range(matrix.row * max_height):
                for j in range(total_width):
                    y0 = int(i / max_height)
                    x0, start, _ = get_info(j)
                    y = i % max_height
                    x = j - start

                    width = max_width_list[x0]
                    m = matrix[y0][x0]
                    mx1 = int((width - m.col) / 2)
                    mx2 = mx1 + m.col
                    my1 = int((max_height - m.row) / 2)
                    my2 = my1 + m.row

                    if x < mx1 or x >= mx2 or y < my1 or y >= my2:
                        text += " "
                    else:
                        text += m[y - my1][x - mx1]
                text += "\n"

        matrix = _matrixlize(text)
        return foo(matrix, *args, **kw)

    return wrapped


def text_font(font_family):
    renderer.text_font = font_family


def get_font_list():
    return _font_list


@add_on_return
@_preprocess_text
def text(matrix, x, y):
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
def text_width(matrix):
    return matrix.col


@_preprocess_text
def text_height(matrix):
    return matrix.row


def text_align(align_x=None, align_y=None):
    if align_x != None:
        renderer.text_align_x = align_x

    if align_y != None:
        renderer.text_align_y = align_y


def text_size(size=constants.NORMAL):
    renderer.text_size = size


def _matrixlize(text, no_empty_line=True):

    if no_empty_line:
        lines = [
            line for line in text.split('\n')
            if not line in string.whitespace or len(line) == 1
        ]
    else:
        lines = [line for line in text.split('\n')]

    if len(lines) == 0:
        return Matrix([[]])

    max_width = max([len(line) for line in lines])
    matrix = [
        [line[i] if i < len(line) else ' '
         for i in range(max_width)]
        for line in lines
    ]
    return Matrix(matrix)
