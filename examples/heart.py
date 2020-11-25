import charming as app


@app.setup
def setup():
    app.full_screen(app.DOUBLE)
    app.rect_mode(app.RADIUS)
    app.ellipse_mode(app.RADIUS)
    app.no_cursor()
    app.frame_rate(10)


@app.draw
def draw():
    size = 8
    x = app.get_frame_count() / 2
    n1 = easing(x, size)
    n2 = easing(x + app.PI, size)

    app.background(" ")
    app.no_stroke()
    app.translate(app.get_width() / 2, app.get_height() / 2)
    app.rotate(app.QUARTER_PI)

    app.fill('💘')
    app.square(0, 0, size)
    app.circle(0, -n1, size)
    app.circle(n2, 0, size)


def easing(x, scale=1):
    p = app.TAU * 2
    x = x - (x // p) * p
    if x < app.PI:
        return app.cos(x) * scale
    elif x < app.PI * 2:
        return - scale
    elif x < app.PI * 3:
        return app.cos(x + app.PI) * scale
    else:
        return scale


app.run()
