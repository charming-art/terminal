import charming as cm

x = 0


@cm.setup
def setup():
    cm.size(30, 20)
    cm.no_cursor()


@cm.draw
def draw():
    global x
    cm.background(' ')
    cm.rect(x, 0, 10, 10)
    x += 1


cm.run()
