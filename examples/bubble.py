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


def swap(list, i, j):
    t = list[i]
    list[i] = list[j]
    list[j] = t


def bubble_sort(data):
    sorted = [[d for d in data]]
    for j in range(len(data)):
        for i in range(1, len(data) - j):
            d0 = data[i - 1]
            d1 = data[i]
            if d0 > d1:
                swap(data, i - 1, i)
        sorted.append([d for d in data])
    return sorted


@cm.setup
def setup():
    cm.full_screen(cm.DOUBLE)
    cm.no_cursor()

    global sorted
    data = generate_data()
    sorted = bubble_sort(data)


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
