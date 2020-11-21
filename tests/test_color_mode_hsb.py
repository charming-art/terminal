import charming as app

app.full_screen()
app.color_mode(app.HSB)


# rainbows
w = 30
h = 360 / w
with app.open_context():
    x = (app.get_width() - w) / 2
    y = (app.get_height() - h) / 2
    app.translate(x, y)
    app.stroke_weight(1)

    for hue in range(360):
        i = hue % w
        j = hue // w
        app.stroke(" ", (hue, 100, 100), (hue, 100, 100))
        app.point(i, j)

app.run()
