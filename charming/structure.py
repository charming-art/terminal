from .app import sketch
from .app import renderer

pointer_stack = []


def setup(hook):
    sketch.add_hook('setup', hook)


def draw(hook):
    sketch.add_hook('draw', hook)


def run():
    sketch.run()


def no_loop():
    sketch.is_loop = False


def loop():
    sketch.is_loop = True


def redraw():
    draw_hook = sketch.hooks_map['draw']
    draw_hook()


def push():
    global pointer_stack
    pointer_stack.append(len(renderer.transform_matrix_stack))


def pop():
    global pointer_stack
    pointer = pointer_stack.pop()
    while len(renderer.transform_matrix_stack) > pointer:
        renderer.transform_matrix_stack.pop()
