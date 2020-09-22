import time

hooks_map = {}
frame_rate = 30
is_loop = True


def add_hook(name, hook):
    hooks_map[name] = hook


def run():
    setup_hook = hooks_map['setup']
    draw_hook = hooks_map['draw']

    if not setup_hook or not draw_hook:
        return

    setup_hook()
    while True:
        if is_loop:
            draw_hook()
        time.sleep(1 / frame_rate)
