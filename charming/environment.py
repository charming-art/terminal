from . import sketch

def frame_rate(_frame_rate):
    sketch.frame_rate = _frame_rate


def size(_width, _height):
    sketch.renderer.size = (int(_width), int(_height))


def full_screen():
    size(sketch.renderer.window_width,
         sketch.renderer.window_height)


def get_window_width():
    return sketch.renderer.window_width


def get_window_height():
    return sketch.renderer.window_height


def get_width():
    return sketch.renderer.size[0]


def get_height():
    return sketch.renderer.size[1]
