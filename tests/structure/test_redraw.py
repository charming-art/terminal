import charming as cm

x = 0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.no_loop()


@cm.draw
def draw():
    global x
    cm.background(' ')
    cm.line(x, 0, x, cm.get_height())
    x = (x + 1) % cm.get_width()


@cm.mouse_clicked
def mouse_clicked():
    cm.redraw()


cm.run()
