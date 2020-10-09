import charming as app


@app.setup
def setup():
    app.full_screen()
    # app.ellipse_mode(app.CHORD)


theta = 0


@app.draw
def draw():
    global theta
    # theta += 1 / 10
    app.stroke('+')
    app.fill('e')
    # app.fill('o')
    with app.save():
        app.translate(app.get_width() / 2, app.get_height() / 2,)
        app.rotate(theta)
        app.arc(0, 0, 10, 5, 0, app.TAU / 4, app.CHORD)
    app.no_loop()


app.run()
