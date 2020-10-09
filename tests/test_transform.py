import charming as app


@app.setup
def setup():
    app.full_screen()


theta = app.PI / 4

@app.draw
def draw():

    app.fill(' ')
    app.no_stroke()
    rect(0, 0, app.get_width(), app.get_height())

    with app.save():
        global theta
        app.translate(app.get_width() / 2, app.get_height() / 2)
        app.rotate(theta)
        app.scale(1.5)
        app.stroke('@')
        app.fill('a')
        rect(0, 0, 5, 5)
        theta += 1 / 10

    rect(0, 0, 5, 5)
    # app.no_loop()


def rect(x, y, width, height):
    width = width - 1
    height = height - 1
    app.begin_shape()
    app.vertex(x, y)
    app.vertex(x + width, y)
    app.vertex(x + width, y + height)
    app.vertex(x, y + height)
    app.end_shape(app.CLOSE)


app.run()
