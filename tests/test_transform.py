import charming as app

app.full_screen()
app.stroke('@', app.YELLOW, app.RED)
app.fill('+', app.GREEN, app.BLUE)

with app.open_context():
    app.translate(10, 5)
    app.square(0, 0, 8)

with app.open_context():
    app.translate(40, 5)
    app.rotate(app.PI / 3)
    app.square(0, 0, 8)

with app.open_context():
    app.translate(70, 2)
    app.scale(3, 2)
    app.square(0, 0, 8)

with app.open_context():
    app.translate(10, 20)
    app.shear_x(app.QUARTER_PI)
    app.square(0, 0, 8)

with app.open_context():
    app.translate(40, 20)
    app.shear_y(app.QUARTER_PI)
    app.square(0, 0, 8)

with app.open_context():
    app.translate(70, 22)
    app.shear_x(app.QUARTER_PI)
    app.shear_y(app.QUARTER_PI)
    app.square(0, 0, 8)

app.run()
