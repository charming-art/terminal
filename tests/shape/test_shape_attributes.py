import charming as app

app.full_screen()

size = 8
app.stroke('@', app.YELLOW, app.RED)
app.fill('+', app.GREEN, app.BLUE)

# rect_mode and rects
app.push()
app.translate(4, 2)
with app.open_context():
    app.translate(0, size)
    app.rect_mode(app.CORNER)  # Default
    app.rect(2, 2, size, size)

with app.open_context():
    app.translate(size * 2, size)
    app.rect_mode(app.CORNERS)
    app.rect(2, 2, size, size)

with app.open_context():
    app.translate(size * 5, size)
    app.rect_mode(app.RADIUS)
    app.rect(2, 2, size, size)

with app.open_context():
    app.translate(size * 7, size)
    app.rect_mode(app.CENTER)
    app.rect(2, 2, size, size)


# ellipse_mode and ellipses

app.translate(size * 9, 0)
with app.open_context():
    app.translate(0, size)
    app.ellipse_mode(app.CORNER)
    app.ellipse(2, 2, size, size)

with app.open_context():
    app.translate(size * 2, size)
    app.ellipse_mode(app.CORNERS)
    app.ellipse(2, 2, size, size)

with app.open_context():
    app.translate(size * 5, size)
    app.ellipse_mode(app.RADIUS)
    app.ellipse(2, 2, size, size)

with app.open_context():
    app.translate(size * 7, size)
    app.ellipse_mode(app.CENTER)  # Default
    app.ellipse(2, 2, size, size)
app.pop()

# stroke weight

with app.open_context():
    # default stroke_weight = 0
    app.translate(size, size * 3)
    app.point(0, 0)
    app.line(size, 0, size * 3, size)
    app.square(size * 4, 0, size)

with app.open_context():
    # set stroke_weight
    app.stroke_weight(1)
    app.translate(size * 8, size * 3)
    app.point(0, 0)
    app.line(size, 0, size * 3, size)
    app.square(size * 4, 0, size)

app.run()
