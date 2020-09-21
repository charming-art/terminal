from .globals import renderer

hooks_map = {}


def add_hook(name, hook):
    global hooks_map
    # Todo: params check
    hooks_map[name] = hook


def setup(hook):
    add_hook('setup', hook)


def draw(hook):
    add_hook('draw', hook)


def run():
    renderer.config(hooks_map)
    renderer.run()
