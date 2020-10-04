from .app import sketch


def get_mouse_x():
    return sketch.mouse_x


def get_mouse_y():
    return sketch.mouse_y


def get_pmouse_y():
    return sketch.pmouse_y


def get_pmouse_x():
    return sketch.pmouse_x


def get_key():
    return sketch.key


def key_typed(hook):
    sketch.add_hook('key_typed', hook)


def mouse_clicked(hook):
    sketch.add_hook('mouse_clicked', hook)
