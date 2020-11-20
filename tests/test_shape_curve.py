import charming as app

app.full_screen()
app.no_cursor()

app.stroke('@', app.YELLOW, app.RED)
app.fill('+', app.GREEN, app.BLUE)

# A curve with tightness of 1
with app.open_context():
    app.curve_tightness(1)
    app.no_fill()
    app.curve(-55, 26, 13, 24, 13, 11, -45, 25)

# A curve with tightness of 0
with app.open_context():
    app.translate(20, 0)
    app.curve_tightness(0)  # default
    app.no_fill()
    app.curve(-55, 26, 13, 24, 13, 11, -45, 25)


# A curve with some points
with app.open_context():
    app.translate(50, 0)
    app.no_fill()
    app.curve(-55, 26, 13, 24, 13, 11, -45, 25)

    t = 0
    cnt = 3
    app.stroke('p', app.CYAN, app.RED)
    app.stroke_weight(1)
    while t <= 1:
        x = app.curve_point(-55, 13, 13, -45, t)
        y = app.curve_point(26, 24, 11, 25, t)
        app.point(x, y)
        t += 1 / cnt

# curve_vertex
app.translate(90, 0)
with app.open_shape():
    app.curve_vertex(44, 21)
    app.curve_vertex(44, 21)
    app.curve_vertex(48, 9)
    app.curve_vertex(21, 7)
    app.curve_vertex(2, 30)
    app.curve_vertex(2, 30)

app.run()
