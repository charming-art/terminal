import charming as app


@app.setup
def setup():
    app.full_screen()


@app.draw
def draw():
    app.fill('+', app.BLUE)
    app.stroke_weight(0)
    app.translate(app.get_width() / 2, app.get_height() / 2)
    # app.circle(0, 0, 20)
    # app.line(0, 0, 10, 0)
    app.point(0, 0)
    app.no_loop()


app.run()
