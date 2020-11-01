import charming as app


@app.setup
def setup():
    app.size(30, 25)


@app.draw
def draw():
    x = app.get_width() / 2
    y = app.get_height() / 2
    # size = 5
    # app.stroke_weight(1)
    # app.fill('*')
    # app.stroke('@')
    # app.begin_shape()
    # app.vertex(x, y)
    # app.vertex(x + size, y)
    # app.vertex(x + size, y - size)
    # app.vertex(x + size * 2, y)
    # app.vertex(x, y + size * 2)
    # app.end_shape(app.CLOSE)
    app.fill('0')
    app.translate(x, y)
    app.begin_shape()
    app.vertex(0, 0)
    app.vertex(10, 10)
    app.vertex(5, 10)
    app.vertex(5, 12)
    app.vertex(-5, 12)
    app.vertex(-5, 10)
    app.vertex(-10, 10)
    app.end_shape(app.CLOSE)
    app.no_loop()


app.run()
