import charming as cm


@cm.setup
def setup():
    cm.full_screen()
    cm.set_cursor(cm.get_width() / 2, cm.get_height() / 2)


@cm.draw
def draw():
    cm.background(' ')
    # check if cursor is moving, otherwise draw hint message
    if not cm.get_cursor_moved():
        cm.translate(cm.get_width() / 2, cm.get_height() / 2)
        cm.text_align(cm.CENTER)
        cm.stroke(' ', cm.WHITE, cm.BLACK)
        cm.text('Pressed up/right/down/left arrow.', 0, 0)


# You can use cursor_pressed hooks instead of
# mouse_moved or mouse_dragged to do some effects.

@cm.cursor_pressed
def cursor_pressed():
    x = cm.get_cursor_x()
    y = cm.get_cursor_y()
    px = cm.get_pcursor_x()
    py = cm.get_pcursor_y()

    cm.stroke('@', cm.YELLOW, cm.RED)
    cm.fill('+', cm.GREEN, cm.BLUE)
    cm.ellipse(x, y, 10, 10)

    cm.stroke('+', cm.CYAN, cm.MAGENTA)
    cm.point(px, py)


cm.run()
