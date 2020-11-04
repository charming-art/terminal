from .app import sketch
from .app import renderer
from contextlib import contextmanager

state_stack = []


def setup(hook):
    sketch.has_setup_hook = True
    sketch.add_hook('setup', hook)


def draw(hook):
    sketch.has_draw_hook = True
    sketch.add_hook('draw', hook)


def run():
    sketch.run()


def no_loop():
    sketch.is_loop = False


def loop():
    sketch.is_loop = True


def preload():
    pass


def redraw():
    draw_hook = sketch.hooks_map['draw']
    draw_hook()


def push():
    global state_stack
    state_stack.append({
        "transform_pointer": len(renderer.transform_matrix_stack),
        "stroke_color": renderer.stroke_color,
        "fill_color": renderer.fill_color,
        "tint_color": renderer.tint_color,
        "stroke_weight": renderer.stroke_weight,
        "is_stroke_enabled": renderer.is_stroke_enabled,
        "is_fill_enabled": renderer.is_fill_enabled,
        "is_tint_enabled": renderer.is_tint_enabled,
        "rect_mode": renderer.rect_mode,
        "ellipse_mode": renderer.ellipse_mode,
        "text_align_x": renderer.text_align_x,
        "text_align_y": renderer.text_align_y,
        "text_leading": renderer.text_leading,
        "text_size": renderer.text_size,
        "image_mode": renderer.image_mode
    })


def pop():
    global state_stack
    state = state_stack.pop()
    while len(renderer.transform_matrix_stack) > state['transform_pointer']:
        renderer.transform_matrix_stack.pop()
    renderer.stroke_color = state['stroke_color']
    renderer.fill_color = state['fill_color']
    renderer.is_stroke_enabled = state['is_stroke_enabled']
    renderer.is_fill_enabled = state['is_fill_enabled']
    renderer.stroke_weight = state['stroke_weight']
    renderer.rect_mode = state["rect_mode"]
    renderer.ellipse_mode = state["ellipse_mode"]
    renderer.text_align_x = state["text_align_x"]
    renderer.text_align_y = state["text_align_y"]
    renderer.text_leading = state["text_leading"]
    renderer.text_size = state["text_size"]
    renderer.tint_color = state["tint_color"]
    renderer.is_tint_enabled = state["is_tint_enabled"]
    renderer.image_mode = state["image_mode"]


@contextmanager
def open_context():
    push()
    yield
    pop()
