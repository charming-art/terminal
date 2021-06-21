import math
import random as rd
from .utils import map as utils_map
from .utils import dist as utils_dist

##### Calculation #####

builtin_abs = abs
builtin_min = min
builtin_max = max
builtin_round = round


def abs(n):
    '''
    Calculates the absolute value of a number.

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
    return utils_dist(x1, y1, x2, y2)


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
    return utils_map(value, start1, stop1, start2, stop2)


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


def atan2(y, x):
    return math.atan2(y, x)


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

##### CVector #####


class CVector(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set(self, a, b=0):
        '''
        Set the components of the vector.

        Example:

            >>> v = CVector()
            >>> v.set(1, 2)
            (1, 2)
            >>> v1 = CVector()
            >>> v1.set(v)
            (1, 2)
            >>> v1.set([2, 3])
            (2, 3)
        '''
        if isinstance(a, self.__class__):
            self.x = a.x
            self.y = a.y
        elif isinstance(a, list):
            self.x = a[0]
            self.y = a[1]
        else:
            self.x = a
            self.y = b
        return self

    @classmethod
    def random_2D(cls):
        '''
        Make a new random 2D unit vector with a random direction.

        Example:

            >>> from math import isclose
            >>> v = CVector.random_2D()
            >>> isclose(v.mag, 1.0)
            True
        '''
        theta = random(math.pi * 2)
        return cls.from_angle(theta)

    @classmethod
    def from_angle(cls, angle):
        '''
        Make a new 2D unit vector from an angle.

        Example:

            >>> from math import pi, isclose
            >>> v = CVector.from_angle(math.pi / 3)
            >>> isclose(v.mag, 1.0)
            True
        '''
        x = cos(angle)
        y = sin(angle)
        return cls(x, y)

    def copy(self):
        '''
        Get a copy of the vector.

        Example:

            >>> v = CVector(1, 2)
            >>> v.copy()
            (1, 2)
        '''
        return self.__class__(self.x, self.y)

    @property
    def mag(self):
        '''
        Calculate the magnitude of the vector.

        Example:

            >>> v = CVector(3, 4)
            >>> v.mag
            5.0
        '''
        return sqrt(self.mag_sq())

    def mag_sq(self):
        '''
        Calculate the magnitude of the vector, squared.

        Example:

            >>> v = CVector(3, 4)
            >>> v.mag_sq()
            25
        '''
        return self.x ** 2 + self.y ** 2

    def __add__(self, other):
        '''
        Adds x and z components to a vector.

        Example:

            >>> v1 = CVector(1, 2)
            >>> v2 = CVector(3, 4)
            >>> v1 + v2
            (4, 6)
            >>> v1 += v2
            >>> v1
            (4, 6)
        '''
        x = self.x + other.x
        y = self.y + other.y
        return self.__class__(x, y)

    def __sub__(self, other):
        '''
        Subtract x and y components from a vector.

        Example:

            >>> v1 = CVector(4, 2)
            >>> v2 = CVector(2, 1)
            >>> v1 - v2
            (2, 1)
            >>> v1 -= v2
            >>> v1
            (2, 1)
        '''
        x = self.x - other.x
        y = self.y - other.y
        return self.__class__(x, y)

    def __mul__(self, k):
        '''
        Multiply a vector by a scalar.

        Example:

            >>> v = CVector(2, 3)
            >>> v * 2
            (4, 6)
            >>> 2 * v
            (4, 6)
            >>> -v
            (-2, -3)
            >>> v *= 2
            >>> v
            (4, 6)
        '''
        x = self.x * k
        y = self.y * k
        return self.__class__(x, y)

    def __truediv__(self, k):
        '''
        Divide a vector by a scalar.

        Example:

            >>> v = CVector(2, 4)
            >>> v / 2
            (1.0, 2.0)
            >>> v /= 2
            >>> v
            (1.0, 2.0)
        '''
        x = self.x / k
        y = self.y / k
        return self.__class__(x, y)

    def __rmul__(self, k):
        '''
        Multiply a vector by a scalar.
        '''
        return self * k

    def __neg__(self):
        '''
        Negate the vector.
        '''
        return self * (-1)

    def dist(self, other):
        '''
        Calculate the distance between two vectors

        Example:

            >>> v1 = CVector(1, 2)
            >>> v2 = CVector(4, 6)
            >>> v1.dist(v2)
            5.0
        '''
        return dist(self.x, self.y, other.x, other.y)

    def dot(self, other):
        '''
        Calculate the dot product of two vectors.

        Example:

            >>> v1 = CVector(1, 2)
            >>> v2 = CVector(2, 3)
            >>> v1.dot(v2)
            8
        '''
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        '''
        Calculate and return the cross product.

        Example:

            >>> v1 = CVector(1, 2)
            >>> v2 = CVector(2, 3)
            >>> v1.cross(v2)
            -1
        '''
        return self.x * other.y - self.y * other.x

    def normalize(self):
        '''
        Normalize the vector to a length of 1.

        Example:

            >>> from math import isclose
            >>> v = CVector(3, 4)
            >>> isclose(v.normalize().mag, 1.0)
            True
        '''
        if self.mag == 0.0:
            raise ValueError(
                "Vector which has 0 magnitude can't be normalized")
        self.mag = 1
        return self

    def limit(self, max_len):
        '''
        Limit the magnitude of the vector.

        Example:

            >>> v = CVector(3, 4)
            >>> v.limit(6).mag
            5.0
            >>> v.limit(4).mag
            4.0

        '''
        self.mag = min(max_len, self.mag)
        return self

    @mag.setter
    def mag(self, len):
        '''
        Set the magnitude of the vector.

        Example:

            >>> v = CVector(3, 4)
            >>> v.mag = 2
            >>> isclose(v.mag, 2)
            True
        '''
        t = len / self.mag
        self.x *= t
        self.y *= t

    def heading(self):
        '''
        Calculate the angle of rotation for this vector.

        Example:

            >>> from math import pi, isclose
            >>> v = CVector(1, 1)
            >>> isclose(v.heading(), pi / 4)
            True
        '''
        return atan2(self.y, self.x)

    def rotate(self, theta):
        '''
        Rotate the vector by an angle (2D only).

        Example:

            >>> from math import pi, isclose
            >>> v = CVector(1, 1)
            >>> isclose(v.rotate(pi / 2).heading(), pi / 4 + pi / 2)
            True
        '''
        x = self.x * cos(theta) - self.y * sin(theta)
        y = self.x * sin(theta) + self.y * cos(theta)
        self.x = x
        self.y = y
        return self

    def lerp(self, other, amt):
        '''
        Linear interpolate the vector to another vector.

        Example:

            >>> from math import isclose
            >>> v1 = CVector(1, 2)
            >>> v2 = CVector(2, 3)
            >>> v3 = v1.lerp(v2, 0.4)
            >>> isclose(v3.x, 1.4)
            True
            >>> isclose(v3.y, 2.4)
            True
        '''
        x = lerp(self.x, other.x, amt)
        y = lerp(self.y, other.y, amt)
        return self.__class__(x, y)

    def angle_between(self, other):
        '''
        Calculate and return the angle between two vectors.

        Example:

            >>> from math import pi, isclose
            >>> v1 = CVector.from_angle(pi / 4)
            >>> v2 = CVector.from_angle(pi / 3)
            >>> angle = v1.angle_between(v2)
            >>> isclose(angle, pi / 3 - pi / 4)
            True
        '''
        return acos(self.dot(other) / (self.mag * other.mag))

    def array(self):
        '''
        Return a representation of the vector as a array

        Example:

            >>> v = CVector(1, 2)
            >>> v.array()
            [1, 2]
        '''
        return [self.x, self.y]

    def __str__(self):
        return (self.x, self.y).__str__()

    __repr__ = __str__

##### Random #####


SINCOS_PRECISION = 0.5
SINCOS_LENGTH = int(360 / SINCOS_PRECISION)
PRE_COS = [cos(radians(d) * SINCOS_PRECISION) for d in range(SINCOS_LENGTH)]
PERLIN_OCTAVES = 4
PERLIN_FALLOFF = 0.5
PERLIN_YWRAPB = 4
PERLIN_YWRAP = 1 << PERLIN_YWRAPB
PERLIN_ZWRAPB = 8
PERLIN_ZWRAP = 1 << PERLIN_ZWRAPB
PERLIN_SIZE = 4095
PERLIN_COS_TABLE = PRE_COS
PERLIN_TWO_PI = SINCOS_LENGTH
PERLIN_PI = PERLIN_TWO_PI
PERLIN_PI >>= 1
PERLIN = None


def noise(x, y=0, z=0):
    """
    Returns the Perlin noise value at specified coordinates.

    https://github.com/p5py/p5/blob/master/p5/pmath/rand.py
    """

    global PERLIN

    def noise_fsc(i):
        return 0.5 * (1 - PERLIN_COS_TABLE[int(i * PERLIN_PI) % PERLIN_TWO_PI])

    if PERLIN is None:
        PERLIN = [rd.random() for _ in range(PERLIN_SIZE + 1)]

    x = (-1 * x) if x < 0 else x
    xi = int(x)
    xf = x - xi

    y = (-1 * y) if y < 0 else y
    yi = int(y)
    yf = y - yi

    z = (-1 * z) if z < 0 else z
    zi = int(z)
    zf = z - zi

    r = 0
    ampl = 0.5

    for _ in range(PERLIN_OCTAVES):
        rxf = noise_fsc(xf)
        ryf = noise_fsc(yf)

        of = int(xi + (yi << PERLIN_YWRAPB) + (zi << PERLIN_ZWRAPB))
        n1 = PERLIN[of % PERLIN_SIZE]
        n1 += rxf * (PERLIN[(of + 1) % PERLIN_SIZE] - n1)
        n2 = PERLIN[(of + PERLIN_YWRAP) % PERLIN_SIZE]
        n2 += rxf * (PERLIN[(of + PERLIN_YWRAP + 1) & PERLIN_SIZE] - n2)
        n1 += ryf * (n2 - n1)

        of += PERLIN_ZWRAP
        n2 = PERLIN[of & PERLIN_SIZE]
        n2 += rxf * (PERLIN[(of + 1) % PERLIN_SIZE] - n2)
        n3 = PERLIN[(of + PERLIN_YWRAP) % PERLIN_SIZE]
        n3 += rxf * (PERLIN[(of + PERLIN_YWRAP + 1) % PERLIN_SIZE] - n3)

        n2 += ryf * (n3 - n2)
        n1 += noise_fsc(zf) * (n2 - n1)

        r += n1 * ampl
        ampl *= PERLIN_FALLOFF

        xi *= 2
        xf *= 2

        yi *= 2
        yf *= 2

        zi *= 2
        zf *= 2

        if xf >= 1:
            xi = xi + 1
            xf = xf - 1

        if yf >= 1:
            yi = yi + 1
            yf = yf - 1

        if zf >= 1:
            zi = zi + 1
            zf = zf - 1

    return r


def noise_detail(octaves=4, falloff=0.5):
    """
    Adjusts the character and level of detail produced by the Perlin noise function.
    """
    global PERLIN_OCTAVES
    global PERLIN_FALLOFF

    if octaves > 0:
        PERLIN_OCTAVES = octaves
    PERLIN_FALLOFF = constrain(falloff, 0, 1)


def noise_seed(seed):
    """
    Sets the seed value for noise()
    """
    global PERLIN
    random_seed(seed)
    PERLIN = None


def random(a=None, b=None):
    '''
    Returns uniform random numbers.
    '''
    if a == None and b == None:
        low = 0
        high = 1
    if b == None:
        low = 0
        high = a
    else:
        low = a
        high = b
    return rd.uniform(low, high)


def random_seed(seed):
    '''
    Sets the seed value for random().
    '''
    rd.seed(seed)


def random_gaussian(mean=0, sd=1):
    '''
    Returns a float from a random series of numbers having a mean of 0 and standard deviation of 1.
    '''
    return mean + rd.gauss(0, 1) * sd


if __name__ == '__main__':
    import doctest
    doctest.testmod()
