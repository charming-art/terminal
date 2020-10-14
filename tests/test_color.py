import charming as app


@app.setup
def setup():
    app.full_screen()


@app.draw
def draw():
    c = app.color('*', 200)
    # app.log(c)
    app.stroke(c)
    app.fill(c)
    app.rect(0, 0, 5, 5)
    if app.get_frame_count() > 2:
        app.no_loop()


app.run()
