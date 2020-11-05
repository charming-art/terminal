from .app import sketch


def frame_rate(frame_rate):
    sketch.frame_rate = frame_rate


def size(width, height):
    sketch.is_full_screen = False
    sketch.size = (int(width), int(height))


def terminal_size(width, height, options=None):
    sketch.context.terminal_width = width
    sketch.context.terminal_height = height
    sketch.context.options = options


def full_terminal(options=None):
    terminal_size(sketch.context.inner_width,
                  sketch.context.inner_height,
                  options)


def full_screen():
    sketch.is_full_screen = True


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
