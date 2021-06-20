import charming as cm


xoff = 0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    global xoff
    cm.background(' ')
    xoff += 0.01
    n = cm.noise(xoff) * cm.get_width()
    cm.line(n, 0, n, cm.get_height())


cm.run()
