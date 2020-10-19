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


class Matrix(object):

    def __init__(self, matrix, type="normal"):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = 0 if self.row == 0 else len(matrix[0])
        self.type = type

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
