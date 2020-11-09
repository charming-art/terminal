import math
import colorsys
import logging
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


def get_char_width(ch):
    """Return the screen column width for unicode ordinal o."""
    if isinstance(ch, tuple):
        _, width = ch
        return width

    if len(ch) >= 2:
        return 2

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
    theta = math.acos(dot / dist)

    if to_left(0, 0, x1, y1, x2, y2):
        theta = math.pi * 2 - theta
    return theta


def to_left(x1, y1, x2, y2, px, py):
    v1 = [x2 - x1, y2 - y1]
    v2 = [px - x1, py - y1]
    return v1[0] * v2[1] - v1[1] * v2[0] <= 0


def map(value, start1, stop1, start2, stop2):
    if start1 == stop1:
        return stop2
    t = (value - start1) / (stop1 - start1)
    return start2 * (1 - t) + stop2 * t


def dist(x1, y1, x2, y2):
    p = [x1, y1]
    q = [x2, y2]
    return math.sqrt(sum((px - qx) ** 2 for px, qx in zip(p, q)))


def generate_color_palette():
    def normalize(r, g, b):
        return {
            'rgb': (r / 255, g / 255, b / 255),
            'hls': colorsys.rgb_to_hls(r / 255, g / 255, b / 255),
            'hsv': colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        }

    def sort_color(c):
        h, s, v = c[0]['hsv']
        return (s, v, h)

    def sort_color_2(c):
        h, s, v = c[0]['hsv']
        return (h, s, v)

    colors = [
        normalize(0x2e, 0x34, 0x36),
        normalize(0xcc, 0x00, 0x00),
        normalize(0x4e, 0x9a, 0x06),
        normalize(0xc4, 0xa0, 0x00),
        normalize(0x34, 0x65, 0xa4),
        normalize(0x75, 0x50, 0x7b),
        normalize(0x06, 0x98, 0x9a),
        normalize(0xd3, 0xd7, 0xcf),
        normalize(0x55, 0x57, 0x53),
        normalize(0xef, 0x29, 0x29),
        normalize(0x8a, 0xe2, 0x34),
        normalize(0xfc, 0xe9, 0x4f),
        normalize(0x72, 0x9f, 0xcf),
        normalize(0xad, 0x7f, 0xa8),
        normalize(0x34, 0xe2, 0xe2),
        normalize(0xee, 0xee, 0xec)
    ]

    # Fill in the remaining 240 ANSI colors.
    # Generate colors (16-231)
    v = [0x00, 0x5f, 0x87, 0xaf, 0xd7, 0xff]
    for i in range(216):
        r = v[int((i / 36) % 6)]
        g = v[int((i / 6) % 6)]
        b = v[int(i % 6)]
        colors.append(normalize(r, g, b))

    # Generate greys (232-255)
    for i in range(24):
        c = 8 + i * 10
        colors.append(normalize(c, c, c))

    colors_palette = [(c, i) for i, c in enumerate(colors)]
    s = sorted(colors_palette[16:], key=sort_color_2)
    # colors_palette = sorted(
    #     colors_palette, key=sort_color
    # )
    # logging.debug([c[0]['hls'][1] for c in colors_palette[:16] + s])

    return colors_palette[:16] + s


# class CSSColor(object):

#     def __init__(self, a, b, c, index):
#         self.index = index
#         self.rgb = (r / 255, b / 255, g / 255)
#         self.hls = colorsys.rgb_to_hls(r / 255, b / 255, g / 255)

#     def __


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
                    [self[i][k] * other[k][j] for k in range(self.col)])
        return new_matrix

    def __getitem__(self, n):
        return self.matrix[n]

    def __str__(self):
        return self.matrix.__str__()

    __repr__ = __str__
