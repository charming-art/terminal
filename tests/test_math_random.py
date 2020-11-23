import charming as app

xoff = app.random(10)
yoff = app.random(10)


@app.setup
def setup():
    # app.noise_seed(0)
    app.full_screen()
    app.no_cursor()
    width = app.get_width()
    height = app.get_height()
    app.no_stroke()

    # unifom random area
    app.fill(bg=app.YELLOW)
    app.rect(0, 0, width / 2, height / 2)

    # gaussian random area
    app.fill(bg=app.RED)
    app.rect(width / 2, 0, width / 2, height / 2)

    # noise random area
    app.fill(bg=app.BLUE)
    app.rect(0, height / 2, width, height / 2)


@app.draw
def draw():
    global xoff, yoff

    width = app.get_width()
    height = app.get_height()

    # random position
    app.stroke('+', bg=app.YELLOW)
    x = app.random(0, width / 2 - 1)
    y = app.random(0, height / 2 - 1)
    app.point(x, y)

    # gaussian position
    with app.open_context():
        app.translate(width / 4 * 3, height / 4)
        app.stroke('*', bg=app.RED)
        x = app.random_gaussian() * 8
        y = app.random_gaussian() * 3
        app.point(x, y)

    # noise position
    with app.open_context():
        app.noise_detail(1, 0.5)
        app.translate(0, height / 2)
        app.stroke('@', bg=app.BLUE)
        x = app.noise(xoff) * width
        y = app.noise(yoff) * height / 2
        app.point(x, y)
        xoff += 0.1
        yoff += 0.1


app.run()
