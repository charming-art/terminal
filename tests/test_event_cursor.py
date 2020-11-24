import charming as app


@app.setup
def setup():
    app.full_screen()
    app.set_cursor(app.get_width() / 2, app.get_height() / 2)


@app.draw
def draw():
    app.background(' ')
    # check if cursor is moving, otherwise draw hint message
    if not app.get_cursor_moved():
        app.translate(app.get_width() / 2, app.get_height() / 2)
        app.text_align(app.CENTER)
        app.stroke(' ', app.WHITE, app.BLACK)
        app.text('Pressed up/right/down/left arrow.', 0, 0)


# You can use cursor_pressed hooks instead of
# mouse_moved or mouse_dragged to do some effects.

@app.cursor_pressed
def cursor_pressed():
    x = app.get_cursor_x()
    y = app.get_cursor_y()
    px = app.get_pcursor_x()
    py = app.get_pcursor_y()

    app.stroke('@', app.YELLOW, app.RED)
    app.fill('+', app.GREEN, app.BLUE)
    app.ellipse(x, y, 10, 10)

    app.stroke('+', app.CYAN, app.MAGENTA)
    app.point(px, py)


app.run()
