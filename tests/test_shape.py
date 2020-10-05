import charming as app


@app.setup
def setup():
    app.size(30, 25)
    # app.full_screen()


@app.draw
def draw():
    # mouse_x = app.get_mouse_x()
    # mouse_y = app.get_mouse_y()
    x = app.get_width() / 2
    y = app.get_height() / 2
    size = 10

    app.stroke('o')
    # app.line(width / 2, height / 2, mouse_x, mouse_y)
    app.begin_shape()
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y + size)
    app.vertex(x, y + size)
    app.end_shape(app.CLOSE)
    app.no_loop()


app.run()
