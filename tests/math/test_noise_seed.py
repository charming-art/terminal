import charming as cm


xoff = 0.0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.noise_seed(99)


@cm.draw
def draw():
    cm.background(' ')
    global xoff
    xoff += .01
    n = cm.noise(xoff) * cm.get_width()
    cm.line(n, 0, n, cm.get_height())


cm.run()
