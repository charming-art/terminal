import charming as cm

y = 0

@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.frame_rate(10)


@cm.draw
def draw():
    global y
    cm.background(' ')
    cm.line(0, y, cm.get_width(), y)
    y = (y + 1) % cm.get_height()


@cm.mouse_clicked
def mouse_clicked():
    if cm.get_is_looping():
        cm.no_loop()
    else:
        cm.loop()


cm.run()
