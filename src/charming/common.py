import functools
from inspect import signature
from . import constants
from .core import Color
from .app import renderer
from .app import sketch
from .utils import sign


class CColor(object):

    def __init__(self, ch=" ", fg=None, bg=None):
        # check params
        _check_ch(ch)
        _check_color(fg, 'fg')
        _check_color(bg, 'bg')

        self.ch = ch
        fg, bg = Color._preprocess_channels(fg, bg)
        self.fg = fg
        self.bg = bg

    def __repr__(self):
        attrs = {
            'ch': self.ch,
            'bg': self.bg,
            'fg': self.fg
        }
        return attrs.__str__()

    __str__ = __repr__


def params_check(*check_args, **check_kw):

    def decorator(foo):
        sig = signature(foo)
        bound_checks = sig.bind_partial(*check_args, **check_kw).arguments

        @functools.wraps(foo)
        def wrapped(*args, **kw):
            if not sketch._check_params:
                return foo(*args, **kw)

            bound_values = sig.bind(*args, **kw)
            for name, value in bound_values.arguments.items():
                if name in bound_checks:
                    check = bound_checks[name]
                    is_more = True

                    # check params
                    if not isinstance(check, tuple):
                        check = (check,)
                        is_more = False

                    result = False
                    for c in check:
                        if isinstance(value, c):
                            result = True
                            break

                    # raise exception
                    if not result:
                        if is_more:
                            msg = f'be one of {check}'
                        else:
                            msg = f'be {check[0]}'
                        raise TypeError(
                            f'Argument {name} must {msg}, but get {type(value)}.'
                        )

            return foo(*args, **kw)

        return wrapped

    return decorator


def color_check(foo):
    @functools.wraps(foo)
    def wrapped(ch=" ", fg=None, bg=None):
        _check_ch(ch)
        _check_color(fg, 'fg')
        _check_color(bg, 'bg')
        if isinstance(ch, CColor):
            fg = ch.fg
            bg = ch.bg
            ch = ch.ch
        else:
            fg, bg = Color._preprocess_channels(fg, bg)
        return foo(ch, fg, bg)
    return wrapped


def _check_ch(ch):
    if not sketch._check_params:
        return

    if isinstance(ch, tuple):
        if len(ch) != 2:
            raise TypeError(
                'Argument ch must be <class "tuple"> with length equals to 2'
            )
    elif not isinstance(ch, str) and not isinstance(ch, CColor):
        raise TypeError(
            'Argument ch must be one of (<class "str">, <class "CColor">).'
        )


def _check_color(color, name):
    if not sketch._check_params:
        return

    if color == None:
        return

    if Color.color_mode == constants.ANSI:
        if not isinstance(color, int) and not isinstance(color, float):
            raise TypeError(
                f'Argument {name} must be one of (<class "int">, <class "float">).')
    else:
        if not isinstance(color, tuple):
            raise TypeError(f'Argument {name} must be <class "tuple">.')
        else:
            if len(color) != 1 and len(color) != 3:
                raise TypeError(
                    f'Argument {name} must be <class "tuple"> with length equals to 1 or 3.'
                )


def add_on_return(foo):
    @functools.wraps(foo)
    def wrapped(*args, **kw):
        element = foo(*args, **kw)
        renderer.add_element(element)
    return wrapped


def get_bounding_rect_by_mode(a, b, c, d, mode):
    if mode == constants.RADIUS:
        x1 = a - c
        y1 = b - d
        x2 = a + c
        y2 = b - d
        x3 = a + c
        y3 = b + d
        x4 = a - c
        y4 = b + d
    elif mode == constants.CORNERS:
        x1 = a
        y1 = b
        x2 = c
        y2 = b
        x3 = c
        y3 = d
        x4 = a
        y4 = d
    elif mode == constants.CENTER:
        x1 = a - c / 2
        y1 = b - d / 2
        x2 = a + c / 2
        y2 = b - d / 2
        x3 = a + c / 2
        y3 = b + d / 2
        x4 = a - c / 2
        y4 = b + d / 2
    else:
        x1 = a
        y1 = b
        x2 = a + c - sign(c)
        y2 = b
        x3 = x2
        y3 = b + d - sign(d)
        x4 = a
        y4 = y3
    return (x1, y1, x2, y2, x3, y3, x4, y4)
