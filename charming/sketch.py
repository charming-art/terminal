import time
from .renderer import Renderer

hooks_map = {}
frame_rate = 30
is_loop = True
renderer = Renderer()


def add_hook(name, hook):
    hooks_map[name] = hook


def run():
    try:
        setup_hook = hooks_map['setup']
        draw_hook = hooks_map['draw']

        if not setup_hook or not draw_hook:
            return

        setup_hook()
        renderer.setup()
        while True:
            if is_loop:
                draw_hook()
                renderer.draw()
            renderer.listen()
            time.sleep(1 / frame_rate)
    except:
        renderer.close()
