import time
from .renderer import Renderer

hooks_map = {
    'setup': lambda: None,
    'draw': lambda: None,
    'mouse_clicked': lambda: None,
    'key_typed': lambda: None,
    'window_resized': lambda: None,
}

frame_rate = 30
is_loop = True
renderer = Renderer()
frame_count = 0

key = 0
key_code = 0
mouse_x = 0
mouse_y = 0
pmouse_x = 0
pmouse_y = 0


def run():
    try:
        global frame_count
        setup_hook = hooks_map['setup']
        draw_hook = hooks_map['draw']

        if not setup_hook or not draw_hook:
            return

        setup_hook()
        renderer.setup()
        while True:
            events = renderer.get_events()
            for e in events:
                handle_event(e)

            if is_loop:
                draw_hook()
                renderer.draw()

            frame_count += 1
            time.sleep(1 / frame_rate)
    except Exception as e:
        print(e)
    finally:
        renderer.close()


def add_hook(name, hook):
    hooks_map[name] = hook


def handle_event(e):
    if e.type == 'mouse':
        global pmouse_x, pmouse_y, mouse_x, mouse_y
        pmouse_x = mouse_x
        pmouse_y = mouse_y
        mouse_x = e.x
        mouse_y = e.y
        mouse_hook = hooks_map['mouse_clicked']
        mouse_hook()
    elif e.type == "window":
        renderer.resize()
        window_hook = hooks_map['window_resized']
        window_hook()
    elif e.type == "keyboard":
        global key
        key = e.key
        keytyped_hook = hooks_map['key_typed']
        keytyped_hook()
