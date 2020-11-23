import charming as app

# In some case, cant not get the right width for
# chars, you can use a tuple (ch, width) to
# represent the char to avoid mess.

chars = ['💘', '🌈', ('⏰', 2), '🧚', '爱']

x = 0


@app.setup
def setup():
    app.size(40, 30, app.DOUBLE)
    app.frame_rate(2)
    app.no_cursor()


@app.draw
def draw():
    global x
    size = 5
    ch = chars[app.get_frame_count() % len(chars)]
    y = 10
    x += 2

    app.background(" ")
    app.no_stroke()
    app.fill(ch)

    # polygan
    app.begin_shape()
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y - size)
    app.vertex(x + size * 2, y)
    app.vertex(x, y + size * 2)
    app.end_shape(app.CLOSE)

    # text
    app.stroke()
    app.text('hello world', 0, 0)


app.run()
