import charming as app

img = None


@app.setup
def setup():
    global img
    app.no_cursor()
    # Set double mode to draw image better
    app.full_screen(app.DOUBLE)

    # Load image in setup() only once
    img = app.load_image('./images/test.png')


@app.draw
def draw():
    size = 8

    app.translate(size, size)
    with app.open_context():
        app.image_mode(app.CORNER)  # default
        app.image(img, 0, 0, size, size)

    with app.open_context():
        app.translate(size * 2, 0)
        app.image_mode(app.CENTER)
        app.image(img, 0, 0, size, size)

    with app.open_context():
        app.translate(size * 4, 0)
        app.image_mode(app.RADIUS)
        app.image(img, 0, 0, size, size)

    with app.open_context():
        app.translate(size * 6, 0)
        app.image_mode(app.CORNERS)
        app.image(img, 2, 2, size, size)

    app.translate(0, size * 2 + 2)
    with app.open_context():
        app.image_mode(app.CORNER)  # default
        app.translate(size, 0)
        app.rotate(app.PI / 3)
        app.tint(' ')
        app.image(img, 0, 0, size, size)

    with app.open_context():
        app.translate(size * 3, 0)
        app.image_mode(app.CENTER)
        app.scale(1.5)
        app.tint('@', app.MAGENTA)
        app.image(img, 0, 0, size, size)

    with app.open_context():
        app.translate(size * 5, 0)
        app.shear_x(app.QUARTER_PI)
        app.image_mode(app.CORNERS)
        app.tint('Q', app.RED)
        app.image(img, 2, 2, size, size)

    app.no_loop()


app.run()
