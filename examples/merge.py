from random import shuffle
import charming as cm

sorted = None
j = 0
cards = [
    '🀇', '🀈', '🀉', '🀊', '🀋', '🀌', '🀍', '🀎', '🀏',
    '🀐', '🀑', '🀒', '🀓', '🀔', '🀕', '🀖', '🀗', '🀘',
    '🀙', '🀚', '🀛', '🀜', '🀝', '🀞', '🀟', '🀠', '🀡',
]


def generate_data():
    data = []
    for i in range(len(cards)):
        data += [i]
    shuffle(data)
    return data


def merge_sort(data):
    sorted = [[d for d in data]]
    n = len(data)
    m = 1
    b0 = [d for d in data]
    b1 = [0 for _ in data]

    def merge(left, right, end):
        i0, i1, j = left, right, left
        while j < end:
            if i0 < right and (i1 >= end or b0[i0] <= b0[i1]):
                i = i0
                i0 += 1
            else:
                i = i1
                i1 += 1
            b1[j] = b0[i]
            j += 1

    while m < n:
        i = 0
        while i < n:
            merge(i, cm.min(n, i + m), cm.min(n, i + m * 2))
            i += m * 2
        m *= 2
        sorted.append([d for d in b0])
        [b0, b1] = [b1, b0]

    sorted.append([d for d in b0])
    return sorted


@cm.setup
def setup():
    cm.full_screen(cm.DOUBLE)
    cm.no_cursor()

    global sorted
    data = generate_data()
    sorted = merge_sort(data)


@cm.draw
def draw():
    global j
    x = (cm.get_width() - len(sorted[0])) / 2
    y = (cm.get_height() - len(sorted)) / 2
    cm.translate(x, y)
    if j < len(sorted):
        numbers = sorted[j]
        for i, n in enumerate(numbers):
            cm.stroke(cards[n])
            cm.point(i, j)
        j += 1


cm.run()
