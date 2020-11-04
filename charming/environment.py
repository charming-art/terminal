from .app import sketch


def frame_rate(frame_rate):
    sketch.frame_rate = frame_rate


def size(width, height):
    sketch.size = (int(width), int(height))


def full_screen():
    size(sketch.context.window_width,
         sketch.context.window_height)


def get_window_width():
    return sketch.context.window_width


def get_window_height():
    return sketch.context.window_height


def get_width():
    return sketch.size[0]


def get_height():
    return sketch.size[1]


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
