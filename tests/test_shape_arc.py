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

    app.fill('e')
    app.no_fill()
    # app.fill('o')
    start_angle = 0
    end_angle = app.PI
    with app.open_context():
        app.translate(app.get_width() / 2, app.get_height() / 2,)
        app.rotate(theta)
        app.stroke('+')
        app.arc(0, 0, 20, 10, start_angle, end_angle, app.CHORD)
        # app.stroke('-')
        # app.arc(0, 0, 10, 20, start_angle, end_angle)
        # app.ellipse(0, 0, 40 ,20)

    app.no_loop()


app.run()
