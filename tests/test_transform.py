import charming as app


@app.setup
def setup():
    app.size(30, 20)


@app.draw
def draw():

    with app.save():
        app.translate(10, 10)
        app.stroke('A')
        rect(0, 0, 5, 5)

        with app.save():
            app.rotate(app.PI / 3)
            app.scale(0.5)
            app.stroke('B')
            rect(0, 0, 5, 5)

    app.stroke('Q')
    app.shear_y(app.PI / 4)
    rect(0, 0, 5, 5)
    app.no_loop()


def rect(x, y, width, height):
    app.begin_shape()
    app.vertex(x, y)
    app.vertex(x + width, y)
    app.vertex(x + width, y + height)
    app.vertex(x, y + height)
    app.end_shape(app.CLOSE)


app.run()
