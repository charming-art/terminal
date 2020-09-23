from . import sketch

width = 0
height = 0


def frame_rate(_frame_rate):
    sketch.frame_rate = _frame_rate


def size(_width, _height):
    global width, height
    width = int(_width)
    height = int(_height)
    sketch.renderer.size = (int(_width), int(_height))


def get_width():
    return width


def get_height():
    return height
