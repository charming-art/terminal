from .app import sketch

# mouse


def get_mouse_x():
    return sketch.mouse_x


def get_mouse_y():
    return sketch.mouse_y


def get_mouse_pressed():
    return sketch.is_mouse_pressed


def get_mouse_button():
    return sketch.mouse_button


def mouse_pressed(hook):
    sketch.add_hook('mouse_pressed', hook)


def mouse_released(hook):
    sketch.add_hook('mouse_released', hook)


def mouse_clicked(hook):
    sketch.add_hook('mouse_clicked', hook)

# keyboard


def get_key():
    return sketch.key


def get_key_code():
    return sketch.key_code


def get_key_pressed():
    return sketch.context.key_pressed


def key_pressed(hook):
    sketch.add_hook('key_pressed', hook)


def key_typed(hook):
    sketch.add_hook('key_typed', hook)


def key_released(hook):
    sketch.add_hook('key_released', hook)

# cursor


def get_cursor_x():
    return sketch.context.cursor_x


def get_cursor_y():
    return sketch.context.cursor_y


def get_pcursor_x():
    return sketch.context.pcursor_x


def get_pcursor_y():
    return sketch.context.pcursor_y


def cursor_moved(hook):
    sketch.add_hook('cursor_moved', hook)


def get_cursor_moved():
    return sketch.cursor_moved
