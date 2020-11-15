import charming as app


@app.setup
def setup():
    app.full_screen()


@app.draw
def draw():
    c = app.CColor('@', 200)
    app.stroke('*')
    app.fill(c)

    app.rect(0, 0, 5, 5)
    # app.point(1, 1)

    if app.get_frame_count() > 2:
        app.no_loop()


app.run()
