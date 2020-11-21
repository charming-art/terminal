import charming as app

app.full_screen()
app.no_cursor()

# basic colors
colors = [
    app.RED,
    app.BLACK,
    app.CYAN,
    app.YELLOW,
    app.GREEN,
    app.BLUE,
    app.WHITE,
    app.MAGENTA
]

with app.open_context():
    x = (app.get_width() - 5 * len(colors)) / 2
    y = app.get_height() / 4
    app.translate(x, y)
    app.stroke_weight(1)

    for i, c in enumerate(colors):
        app.stroke("@", c, c)
        app.point(i * 5, 0)

# all ansi colors: 256
with app.open_context():
    w = 32
    h = 256 / w
    app.translate((app.get_width() - w) / 2, (app.get_height() - h) / 2)
    for i in range(256):
        x = i % 32
        y = i // 32
        app.stroke(' ', i, i)
        app.point(x, y)

# lerp ansi colors
with app.open_context():
    start = app.CColor('a', app.RED, app.RED)  # start color
    end = app.CColor('z', app.YELLOW, app.YELLOW)  # end color

    x = (app.get_width() - 5 * len(colors)) / 2
    y = app.get_height() / 4 * 3
    app.translate(x, y)
    app.stroke_weight(1)

    for i in range(len(colors)):
        t = i / len(colors)
        # linear interpolation all the channels
        # incloude ch
        c = app.lerp_color(start, end, t)
        app.stroke(c)
        app.point(i * 5, 0)


app.run()
