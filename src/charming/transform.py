import functools
from math import sin
from math import cos
from math import tan
from .app import renderer
from .common import params_check
from .utils import Matrix


def _push_on_return(foo):
    @functools.wraps(foo)
    def wrapped(*args, **kw):
        matrix = foo(*args, **kw)
        renderer.transform_matrix_stack.append(matrix)
    return wrapped


@_push_on_return
@params_check(
    (float, int),
    (float, int)
)
def translate(tx, ty):
    '''
    x'    1 0 tx   x
    y' =  0 1 ty * y
    1     0 0  1   1
    '''
    matrix = Matrix([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1],
    ])
    return matrix


@_push_on_return
@params_check(
    (float, int),
    sy=(float, int)
)
def scale(sx, sy=None):
    '''
    x'   sx 0  0   x
    y' = 0  sy 0 * y
    1    0  0  1   1
    '''
    sy = sx if sy == None else sy
    matrix = Matrix([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1],
    ], "scale")
    return matrix


@_push_on_return
@params_check((float, int))
def rotate(x):
    '''
    x'   cosx -sinx 0   x
    y' = sinx cosx  0 * y
    1    0    0     1   1
    '''
    matrix = Matrix([
        [cos(x), -sin(x), 0],
        [sin(x), cos(x), 0],
        [0, 0, 1]
    ], "rotate", x)
    return matrix


@_push_on_return
@params_check((float, int))
def shear_x(x):
    '''
    x'   1 cotx 0   x
    y' = 0 1    0 * y
    1    0 0    1   1
    '''
    matrix = Matrix([
        [1, 1 / tan(x), 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    return matrix


@_push_on_return
@params_check((float, int))
def shear_y(x):
    '''
    x'   1    0 0   x
    y' = cotx 1 0 * y
    1    0    0 1   1
    '''
    matrix = Matrix([
        [1, 0, 0],
        [1 / tan(x), 1, 0],
        [0, 0, 1]
    ])
    return matrix
