from . import sketch


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
