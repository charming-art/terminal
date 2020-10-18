import charming as app


@app.setup
def setup():
    app.full_screen()


@app.draw
def draw():
    size = 5
    x = 1
    y = 10
    app.fill('*', app.YELLOW, app.RED)
    app.stroke('@', app.GREEN, app.BLUE)

    # polygon without close
    app.begin_shape()
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y + size)
    app.vertex(x, y + size)
    app.end_shape()

    # polygon with close
    x += 10
    app.begin_shape()
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y + size)
    app.vertex(x, y + size)
    app.end_shape(app.CLOSE)

    # LINES
    x += 10
    app.begin_shape(app.LINES)
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y + size)
    app.vertex(x, y + size)
    app.end_shape()

    # TRIANGLES
    x += 10
    y = 15
    app.begin_shape(app.TRIANGLES)
    app.vertex(x, y)
    app.vertex(x + size, y - size)
    app.vertex(x + size * 2, y)
    app.vertex(x + size * 3, y - size)
    app.vertex(x + size * 4, y)
    app.vertex(x + size * 5, y - size)
    app.end_shape()

    # TRIANGLE_STRIP
    x += 30
    app.begin_shape(app.TRIANGLE_STRIP)
    app.vertex(x, y)
    app.vertex(x + size, y - size)
    app.vertex(x + size * 2, y)
    app.vertex(x + size * 3, y - size)
    app.vertex(x + size * 4, y)
    app.vertex(x + size * 5, y - size)
    app.vertex(x + size * 6, y)
    app.end_shape()

    # TRIANGLE_FAN
    x += 40
    app.begin_shape(app.TRIANGLE_FAN)
    app.vertex(x, y)
    app.vertex(x, y - size)
    app.vertex(x + size, y)
    app.vertex(x, y + size)
    app.vertex(x - size, y)
    app.vertex(x, y - size)
    app.end_shape()

    # QUADS
    y += 10
    x = 1
    app.begin_shape(app.QUADS)
    app.vertex(x, y)
    app.vertex(x, y + size)
    app.vertex(x + size, y + size)
    app.vertex(x + size, y)
    app.vertex(x + size * 2, y)
    app.vertex(x + size * 2, y + size)
    app.vertex(x + size * 3, y + size)
    app.vertex(x + size * 3, y)
    app.end_shape()

    # QUAD_STRIP
    x = 30
    app.begin_shape(app.QUAD_STRIP)

    app.vertex(x, y)
    app.vertex(x, y + size)
    app.vertex(x + size, y)
    app.vertex(x + size, y + size)

    app.vertex(x + size * 2, y)
    app.vertex(x + size * 2, y + size)
    app.vertex(x + size * 3, y)
    app.vertex(x + size * 3, y + size)

    app.end_shape()

    app.no_loop()


app.run()
