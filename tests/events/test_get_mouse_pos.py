import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    mouse_x = cm.get_mouse_x()
    mouse_y = cm.get_mouse_y()
    cm.line(mouse_x, 0, mouse_x, cm.get_height())
    cm.line(0, mouse_y, cm.get_width(), mouse_y)


cm.run()
