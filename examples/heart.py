import charming as app


@app.setup
def setup():
    app.full_screen(app.DOUBLIE)
    app.rect_mode(app.RADIUS)
    app.ellipse_mode(app.RADIUS)
    app.no_cursor()
    app.frame_rate(10)


@app.draw
def draw():
    size = 8
    t1 = custom_foo(app.get_frame_count() / 2)
    t2 = custom_foo(app.get_frame_count() / 2 + app.PI)
    n1 = app.map(t1, -1, 1, -size, size)
    n2 = app.map(t2, -1, 1, -size, size)

    app.background(" ")
    app.no_stroke()
    app.translate(app.get_width() / 2, app.get_height() / 2)
    app.rotate(app.QUARTER_PI)

    app.fill("💘", 1, 9)
    app.square(0, 0, size)    
    app.circle(0, -n1, size)
    app.circle(n2, 0, size)


def custom_foo(x):
    while x >= app.TAU * 2:
        x -= app.TAU * 2
    if x < app.PI:
        return app.cos(x)
    elif x < app.PI * 2:
        return - 1 
    elif x < app.PI * 3:
        return app.cos(x + app.PI)
    else:
        return 1


app.run()
