import functools
from .app import renderer
from .cmath import sin
from .cmath import cos
from .cmath import Matrix


def _push_on_return(foo):

    @functools.wraps(foo)
    def wrapped(*args, **kw):
        matrix = foo(*args, **kw)
        renderer.transform_matrix_stack.append(matrix)

    return wrapped


@_push_on_return
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
    ])
    return matrix


@_push_on_return
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
    ])
    return matrix
