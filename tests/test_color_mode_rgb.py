import charming as app

app.full_screen()
app.color_mode(app.RGB)

n = 7
# grays
with app.open_context():
    x = (app.get_width() - 5 * 7) / 2
    y = app.get_height() / 4
    app.translate(x, y)
    app.stroke_weight(1)

    for i in range(n):
        c = app.map(i, 0, n, 0, 255)
        app.stroke("@", (c,), (c,))
        app.point(i * 5, 0)

# red channels
# grays
with app.open_context():
    x = (app.get_width() - 5 * 7) / 2
    y = app.get_height() / 2
    app.translate(x, y)
    app.stroke_weight(1)

    for i in range(n):
        c = app.map(i, 0, n, 0, 255)
        app.stroke(" ", (c, 0, 0), (c, 0, 0))
        app.point(i * 5, 0)

# yellows
with app.open_context():
    start = app.CColor('a', (0,), (0,))
    end = app.CColor('z', (255, 255, 0), (255, 255, 0))
    x = (app.get_width() - 5 * 7) / 2
    y = app.get_height() / 4 * 3

    app.translate(x, y)
    app.stroke_weight(1)
    for i in range(n):
        t = i / n
        c = app.lerp_color(start, end, t)
        app.stroke(c)
        app.point(i * 5, 0)

app.run()
