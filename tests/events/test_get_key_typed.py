import charming as cm

char = ''


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    cm.fill(char)
    cm.no_stroke()
    cm.rect(0, 0, 10, 10)


@cm.key_typed
def key_typed():
    global char
    if cm.get_key() == cm.CODED:
        if cm.get_key_code() == cm.UP:
            char = 'O'
        else:
            char = '+'


cm.run()
