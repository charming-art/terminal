import charming as app


@app.setup
def setup():
    app.size(30, 30)
    app.rect_mode(app.RADIUS)


@app.draw
def draw():
    app.rect(5, 5, 5, 5)
    app.point(5, 5)
    app.no_loop()


app.run()
