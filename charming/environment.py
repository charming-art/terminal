from .app import sketch


def frame_rate(_frame_rate):
    sketch.frame_rate = _frame_rate


def size(_width, _height):
    sketch.size = (int(_width), int(_height))


def full_screen():
    size(sketch.context.window_width,
         sketch.context.window_height)


def get_window_width():
    return sketch.context.window_width


def get_window_height():
    return sketch.context.window_height


def get_width():
    return sketch.context.size[0]


def get_height():
    return sketch.context.size[1]


def get_frame_rate():
    return sketch.frame_rate


def get_frame_count():
    return sketch.frame_count


def no_cursor():
    sketch.context.no_cursor()


def cursor():
    sketch.context.cursor()


def window_resized(hook):
    sketch.add_hook('window_resized', hook)
