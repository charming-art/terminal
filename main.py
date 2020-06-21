from charming import charming as cm


@cm.setup
def setup():
    cm.size(10, 10)


@cm.draw
def draw():
    cm.background(' ')
    cm.corner('@')
    cm.stroke('¥')
    cm.fill('')
    cm.rect(10, 10, 10, 10)


cm.run()
