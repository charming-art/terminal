import math
import sys
from abc import ABCMeta, abstractclassmethod
import logging
import time
from .globals import WINDOWS
from .globals import POSIX
from .globals import DEBUG_MODE

widths = [
    (126,    1), (159,    0), (687,     1), (710,   0), (711,   1),
    (727,    0), (733,    1), (879,     0), (1154,  1), (1161,  0),
    (4347,   1), (4447,   2), (7467,    1), (7521,  0), (8369,  1),
    (8426,   0), (9000,   1), (9002,    2), (11021, 1), (12350, 2),
    (12351,  1), (12438,  2), (12442,   0), (19893, 2), (19967, 1),
    (55203,  2), (63743,  1), (64106,   2), (65039, 1), (65059, 0),
    (65131,  2), (65279,  1), (65376,   2), (65500, 1), (65510, 2),
    (120831, 1), (262141, 2), (1114109, 1),
]


def list_find(list, cb):
    for i, e in enumerate(list):
        if cb(e):
            return i
    return -1


def get_char_width(ch):
    """Return the screen column width for unicode ordinal o."""
    if isinstance(ch, tuple):
        return ch[1]

    if len(ch) >= 2:
        return 2
    
    if ch == '':
        return 0

    o = ord(ch)
    if o == 0xe or o == 0xf:
        return 0
    for num, wid in widths:
        if o <= num:
            return wid
    return 1


def angle_between(x1, y1, x2, y2):
    '''angle from (x1, y1) to (x2, y2)'''
    dot = x1 * x2 + y1 * y2
    dist = math.sqrt(x1 ** 2 + y1 ** 2) * math.sqrt(x2 ** 2 + y2 ** 2)
    if dist == 0:
        return 0
    theta = math.acos(dot / dist)

    if to_left(0, 0, x1, y1, x2, y2):
        theta = math.pi * 2 - theta
    return theta


def lerp_color(colors, amt=None):
    '''
    :param colors: RGB
    '''

    def get_step(amt):
        if len(colors) == 2:
            return (0, 1, amt)
        step = 1 / (len(colors) - 1)
        start = math.floor(amt / step)
        end = math.ceil(amt / step)
        return [start, end, (amt - start * step) / step]

    def lerp(amt):
        if len(colors) == 1:
            return colors[1]
        start, end, t = get_step(amt)
        c1 = colors[start]
        c2 = colors[end]
        return [c1[i] * (1 - t) + t * c2[i] for i in range(3)]

    if amt == None:
        return lerp
    else:
        return lerp(amt)


def to_left(x1, y1, x2, y2, px, py):
    v1 = [x2 - x1, y2 - y1]
    v2 = [px - x1, py - y1]
    return v1[0] * v2[1] - v1[1] * v2[0] <= 0


def map(value, start1, stop1, start2, stop2):
    if start1 == stop1:
        return stop2
    t = (value - start1) / (stop1 - start1)
    return start2 * (1 - t) + stop2 * t


def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def dist(x1, y1, x2, y2):
    p = [x1, y1]
    q = [x2, y2]
    return math.sqrt(sum((px - qx) ** 2 for px, qx in zip(p, q)))


class Matrix(object):

    def __init__(self, matrix, type="normal", value=0):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = 0 if self.row == 0 else len(matrix[0])
        self.type = type
        self.value = value

    def __mul__(self, other):
        new_matrix = Matrix([[0 for _ in range(other.col)]
                             for _ in range(self.row)])
        for i in range(self.row):
            for j in range(other.col):
                new_matrix[i][j] = sum(
                    [self[i][k] * other[k][j] for k in range(self.col)]
                )
        return new_matrix

    def __getitem__(self, n):
        return self.matrix[n]

    def __str__(self):
        return self.matrix.__str__()

    __repr__ = __str__


class Logger(metaclass=ABCMeta):

    def __init__(self, should_record=False):
        self.time_by_key = {}
        self.should_record = should_record
        self.inclues = [
            # 'loop',
            # 'setup',
            'flush screen',
            'render shape',
            # 'vertex processing',
            # 'primitive assembly',
            # 'rasterizatioin',
            # 'clipping',
            # 'fragment processing',
            # 'polygon filling',
            # 'draw line',
        ]

    @abstractclassmethod
    def debug(self, *kw, **args):
        pass

    @abstractclassmethod
    def time(self):
        pass

    @abstractclassmethod
    def plot(self, records):
        pass

    def record(self, key):
        def decorator(foo):
            def wrapped(*args, **kw):
                if self.should_record and key in self.inclues:
                    t1 = self.time()
                    ret = foo(*args, **kw)
                    t2 = self.time()
                    d = t2 - t1
                    if key in self.time_by_key:
                        self.time_by_key[key] += d
                    else:
                        self.time_by_key[key] = d
                    return ret
                else:
                    return foo(*args, **kw)
            return wrapped
        return decorator

    def log_record(self):
        if self.should_record:
            records = [(key, value) for key, value in self.time_by_key.items()]
            records.sort(key=lambda x: x[1])
            self.plot(records)

if DEBUG_MODE:
    import matplotlib.pyplot as plt

logging.basicConfig(filename='charming.log', level=logging.DEBUG)

class LocalLogger(Logger):

    def __init__(self, should_record):
        super(LocalLogger, self).__init__(should_record)

    def debug(self, *args, **kw):
        logging.debug(*args, **kw)

    def time(self):
        return time.time()

    def plot(self, records):
        total = 0
        for _, value in records:
            total += value
        keys = [r[0] for r in records]
        values = [r[1] for r in records]
        proportions = [r[1] / total for r in records]

        plt.figure(dpi=70, figsize=(24, 12))

        # pie chart
        plt.subplot(121)
        plt.pie(
            proportions,
            labels=keys,
            autopct='%1.1f%%',
        )

        plt.subplot(122)
        # bar chart
        plt.bar(
            keys,
            values,
            color="steelblue"
        )

        plt.show()

logger = LocalLogger(DEBUG_MODE)
