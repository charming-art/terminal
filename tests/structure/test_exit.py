import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.color_mode(cm.RGB)


@cm.draw
def draw():
    b = cm.get_frame_count() % 255
    color = (0, 0, b)
    cm.background(' ', color, color)


@cm.mouse_clicked
def mouse_clicked():
    cm.exit()


cm.run()
