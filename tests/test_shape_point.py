import charming as app


@app.setup
def setup():
    app.full_screen()

@app.draw
def draw():
    app.stroke('@')
    app.translate(app.get_width() / 2, app.get_height() / 2)
    app.circle(0, 0, 10)
    app.no_loop()


app.run()