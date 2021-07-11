import charming as cm

x = 0


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    global x
    cm.background(' ')
    cm.rect(x, 0, 10, 10)
    x += 1


cm.run()
