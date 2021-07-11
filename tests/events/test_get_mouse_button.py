import charming as cm


@cm.setup
def setup():
    cm.full_screen()


@cm.draw
def draw():
    cm.no_stroke()
    if cm.get_mouse_pressed() and cm.get_mouse_button() == cm.LEFT:
        cm.fill('O')
    elif (cm.get_mouse_pressed() and cm.get_mouse_button() == cm.RIGHT):
        cm.fill('+')
    else:
        cm.fill('-')
    cm.rect(0, 0, 10, 10)


cm.run()
