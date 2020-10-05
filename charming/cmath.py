import math

##### Calculation #####

builtin_abs = abs
builtin_min = min
builtin_max = max
builtin_round = round


def abs(n):
    '''
    Calculates the absolute value of a number. The absolute value of a number is always positive.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return builtin_abs(n)


def ceil(n):
    '''
    Calculates the closest int value that is greater than or equal to the value of the parameter.

    Example:

    >>> ceil(1.2)
    2
    >>> ceil(-1.2)
    -1
    >>> ceil(1)
    1
    >>> ceil(-1)
    -1
    '''
    return math.ceil(n)


def constrain(amt, low, high):
    '''
    Constrains a value to not exceed.

    Example:

    >>> constrain(-1, 2, 3)
    2
    >>> constrain(4, 2, 3)
    3
    >>> constrain(2.5, 2, 3)
    2.5
    '''
    return min(high, max(amt, low))


def dist(x1, y1, x2, y2):
    '''
    Calculates the distance between two points.

    Example:

    >>> dist(0, 0, 1, 0)
    1.0
    >>> dist(-1, -1, 2, 3)
    5.0
    '''
    p = [x1, y1]
    q = [x2, y2]
    return math.sqrt(sum((px - qx) ** 2 for px, qx in zip(p, q)))


def exp(n):
    '''
    Return Euler's number raised to the power of the n parameter.

    Example

    >>> exp(1)
    2.718281828459045
    '''
    return math.exp(n)


def floor(n):
    '''
    Calculates the closest int value that is less then or equal to the value of the parameter.

    Example:

    >>> floor(1.2)
    1
    >>> floor(-1.2)
    -2
    >>> floor(0)
    0
    '''
    return math.floor(n)


def lerp(start, stop, amt):
    '''
    Calculates a number between two numbers at a specific increment.

    :amt: The amount to interpolate between the two values where 0 equal to the first point.

    Example:

    >>> lerp(1, 2, 0)
    1
    >>> lerp(1, 2, 1)
    2
    >>> lerp(10, 20, 0.2)
    12.0
    '''
    return start * (1 - amt) + stop * amt


def log(x):
    '''
    Calculates the naturail logarithm of a number. This function expects the n parameter to be a value greater than 0.0.

    Example:

    >>> log(math.e)
    1.0
    '''
    return math.log(x)


def mag(a, b, c=0):
    '''
    Calculates the magnitude(or length) of a vector. Therefore, mag() is a shortcut for writing dist(0, 0, x, y).

    Example:

    >>> mag(3, 4)
    5.0
    >>> mag(3, 4, 12)
    13.0
    '''
    return math.sqrt(sum([a ** 2, b ** 2, c ** 2]))


def map(value, start1, stop1, start2, stop2):
    '''
    Re-maps a number from one range to another.

    Example:

    >>> map(1.5, 1, 2, 10, 20)
    15.0
    '''
    if start1 == stop1:
        return value
    t = (value - start1) / (stop1 - start1)
    return start2 * (1 - t) + stop2 * t


def max(*args, **kw):
    '''
    Determines the largest value in a sequence of numbers.

    Example:

    >>> max(0, 1)
    1
    >>> max(0, 1, 2)
    2
    >>> max([0, 1, 2, 3])
    3
    '''
    return builtin_max(*args, **kw)


def min(*args, **kw):
    '''
    Determines the smallest value in a sequence of numbers.

    Example:

    >>> min(0, 1)
    0
    >>> min(0, 1, 2)
    0
    >>> min([0, 1, 2, 3])
    0
    '''
    return builtin_min(*args, **kw)


def norm(value, start, stop):
    '''
    Normalizes a number from another range into a value between 0 and 1. Identical to map(value, low, high, 0, 1).

    Example:

    >>> norm(20, 0, 50)
    0.4
    '''
    return map(value, start, stop, 0, 1)


def pow(n, e):
    '''
    Facilitates exponential expressions. The pow() function is an efficient way of multiplying numbers by themselves (or their reciprocals) in large quantities.

    Example:

    >>> pow(3, 2)
    9.0
    >>> pow(4, 0.5)
    2.0
    '''
    return math.pow(n, e)


def round(n):
    '''
    Calculate the int closest to the n parameter.

    Example:

    >>> round(9.2)
    9
    >>> round(9.4)
    9
    >>> round(9.5)
    10
    >>> round(-1.4)
    -1
    >>> round(-1.5)
    -2
    '''
    return builtin_round(n)


def sq(n):
    '''
    Squares a number (multiplies a number by itself).

    Example:

    >>> sq(5)
    25
    '''
    return n ** 2


def sqrt(n):
    '''
    Calculates the square root of a number.

    Example:

    >>> sqrt(25)
    5.0
    '''
    return math.sqrt(n)


##### Trigonometry #####

def acos(n):
    return math.acos(n)


def asin(n):
    return math.asin(n)


def atan(n):
    return math.atan(n)


def atan2(n):
    return math.atan2(n)


def cos(n):
    return math.cos(n)


def degrees(n):
    return math.degrees(n)


def radians(n):
    return math.radians(n)


def sin(n):
    return math.sin(n)


def tan(n):
    return math.tan(n)


##### Matrix #####

class Matrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = 0 if self.row == 0 else len(matrix[0])

    def __mul__(self, other):
        new_matrix = Matrix([[0 for _ in range(other.col)] for _ in range(self.row)])
        for i in range(self.row):
            for j in range(other.col):
                new_matrix[i][j] = sum(
                    [self[i][k] * other[k][j] for k in range(self.col)])
        return new_matrix

    def __getitem__(self, n):
        return self.matrix[n]

    def __str__(self):
        return self.matrix.__str__()
    
    __repr__ = __str__
