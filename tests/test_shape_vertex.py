import charming as app


@app.setup
def setup():
    app.size(30, 25)


@app.draw
def draw():
    x = app.get_width() / 2
    y = app.get_height() / 2
    size = 5
    app.fill('*')
    app.stroke('@')
    app.begin_shape()
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y - size)
    app.vertex(x + size * 2, y)
    app.vertex(x, y + size * 2)
    app.end_shape()
    app.no_loop()


app.run()
