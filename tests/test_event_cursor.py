import charming as app


@app.setup
def setup():
    app.full_screen()
    app.set_cursor(app.get_width() / 2, app.get_height() / 2)


@app.draw
def draw():
    app.background(' ')
    if not app.get_cursor_moved():
        app.translate(app.get_width() / 2, app.get_height() / 2)
        app.text_align(app.CENTER)
        app.stroke(' ', app.WHITE, app.BLACK)
        app.text('Pressed up/right/down/left arrow.', 0, 0)


@app.cursor_moved
def cursor_moved():
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
