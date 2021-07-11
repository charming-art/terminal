import charming as cm

# CODED, ESCAPE, LEFT, UP, RIGHT, DOWN, BACKSPACE, TAB, ENTER, SPACE

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


@cm.key_pressed
def key_pressed():
    global char
    if cm.get_key() == cm.CODED:
        if cm.get_key_code() == cm.UP:
            char = 'O'
        else:
            char = '+'


cm.run()
