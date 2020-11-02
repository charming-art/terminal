import charming as app


@app.setup
def setup():
    app.full_screen()
    # app.ellipse_mode(app.CHORD)
    # app.rect_mode(app.CENTER)


theta = 0


@app.draw
def draw():
    global theta
    # theta += 1 / 10

    app.fill('e')
    app.no_fill()
    # app.fill('o')
    start_angle = 0
    end_angle = app.PI / 2
    with app.open_context():
        app.translate(app.get_width() / 2, app.get_height() / 2)
        # app.rotate(app.PI / 6)
        app.stroke('+')
        # app.rect(0, 0, 20, 10)
        # app.arc(0, 0, 20, 10, start_angle, end_angle, app.PIE)
        # app.stroke('-')
        # app.arc(0, 0, 10, 20, start_angle, end_angle)
        # app.ellipse(0, 0, 2, 2)
        app.circle(0, 0, 4)

    app.no_loop()


app.run()
