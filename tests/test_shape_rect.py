import charming as app


@app.setup
def setup():
    app.size(30, 30)
    app.rect_mode(app.RADIUS)


@app.draw
def draw():
    app.rect(2, 2, 2, 2)
    # app.point(5, 5)
    app.no_loop()


app.run()
