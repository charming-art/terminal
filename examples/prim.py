import charming as cm
from random import shuffle

vertices = None
width = None
height = None
max_depth = 0
i = 0


def generate_graph(width, height):
    size = width * height
    graph = []
    for i in range(size):
        x = i % width
        around = [
            i + width,
            i - width,
            -1 if x == width - 1 else i + 1,
            -1 if x == 0 else i - 1
        ]
        shuffle(around)
        edges = filter(lambda x: x >= 0 and x < size, around)
        edges = map(lambda x: (x, cm.random(0, 1)), edges)
        vertex = (i, list(edges))
        graph.append(vertex)
    return graph


def prim(graph, start):
    size = len(graph)
    visited = [0 for _ in range(size)]
    depth = [0 for _ in range(size)]
    frontier = [(start, 0)]
    depth[start] = 0
    visited[start] = 1
    collected = []
    while len(collected) < size:
        index, _ = pop_min(frontier)
        v, e = graph[index]
        collected.append((v, depth[v]))
        for n, w in e:
            if visited[n] == 0:
                depth[n] = depth[index] + 1
                visited[n] = 1
                frontier.append((n, w))
    return collected


def pop_min(list):
    mi = 0
    mv = 1
    for i, e in enumerate(list):
        if e[1] < mv:
            mv, mi = e[1], i
    swap(list, mi, -1)
    return list.pop()


def swap(list, i, j):
    t = list[i]
    list[i] = list[j]
    list[j] = t


@cm.setup
def setup():
    # init environment
    cm.full_screen()
    cm.no_cursor()
    cm.color_mode(cm.HSB)

    # init vars
    global vertices, max_depth, width, height
    width, height = cm.get_width(), cm.get_height()
    graph = generate_graph(width, height)
    vertices = prim(graph, int(cm.random(width * height)))
    max_depth = cm.max(map(lambda x: x[1], vertices))


@cm.draw
def draw():
    global i
    cnt = 10
    while i < len(vertices) and cnt >= 0:
        fill(vertices[i])
        cnt -= 1
        i += 1


def fill(vertex):
    index, depth = vertex
    hue = cm.map(depth, 0, max_depth, 0, 360)
    c = (int(hue), 100, 100)
    x, y = index % width, int(index / width)
    cm.stroke(" ", c, c)
    cm.point(x, y)


cm.run()
