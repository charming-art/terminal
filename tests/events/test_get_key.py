import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    if cm.get_key_pressed():
        key = cm.get_key()
        if key == 'b' or key == 'B':
            cm.fill('O')
        else:
            cm.fill('+')
    cm.no_stroke()
    cm.rect(0, 0, 10, 10)


cm.run()
