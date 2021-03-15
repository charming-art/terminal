import types
from .app import sketch
from .common import params_check

# mouse


def get_mouse_x():
    return sketch.mouse_x


def get_mouse_y():
    return sketch.mouse_y


def get_mouse_pressed():
    return sketch.is_mouse_pressed


def get_mouse_button():
    return sketch.mouse_button


@params_check(types.FunctionType)
def mouse_pressed(hook):
    sketch.add_hook('mouse_pressed', hook)


@params_check(types.FunctionType)
def mouse_released(hook):
    sketch.add_hook('mouse_released', hook)


@params_check(types.FunctionType)
def mouse_clicked(hook):
    sketch.add_hook('mouse_clicked', hook)

# keyboard


def get_key():
    return sketch.key


def get_key_code():
    return sketch.key_code


def get_key_pressed():
    return sketch.context.key_pressed


@params_check(types.FunctionType)
def key_pressed(hook):
    sketch.add_hook('key_pressed', hook)


@params_check(types.FunctionType)
def key_typed(hook):
    sketch.add_hook('key_typed', hook)


@params_check(types.FunctionType)
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


@params_check(types.FunctionType)
def cursor_moved(hook):
    sketch.add_hook('cursor_moved', hook)


@params_check(types.FunctionType)
def cursor_pressed(hook):
    sketch.add_hook('cursor_pressed', hook)


def get_cursor_moved():
    return sketch.cursor_moved
