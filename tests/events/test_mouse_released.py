import charming as cm

char = 'O'


@cm.setup
def setup():
    cm.full_screen()
    cm.no_cursor()


@cm.draw
def draw():
    cm.background(' ')
    cm.fill(char)
    cm.rect(0, 0, 10, 10)


@cm.mouse_released
def mouse_released():
    global char
    if char == 'O':
        char = '+'
    else:
        char = 'O'


cm.run()
