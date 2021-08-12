import charming as cm


a = 0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()
    cm.background('O')
    cm.fill('+', cm.YELLOW, cm.CYAN)
    cm.no_stroke()


@cm.draw
def draw():
    global a
    cm.rect(a % cm.get_width(), 2, 2, cm.get_height() - 4)
    a += 1


cm.run()
