import charming as app


@app.setup
def setup():
    app.full_screen()
    app.frame_rate(1)
    # app.no_cursor()


x = 0


@app.draw
def draw():
    global x
    x += 1
    app.background(" ")
    # color = app.color(('🧚‍♀️')) # not display
    # color = app.color(('⏰', 2))  # wrong display
    color = app.color('🚀')
    app.stroke(color)
    # app.fill(' ', app.WHITE)
    # app.stroke(color)
    # app.fill(color)
    # app.ellipse(20, 10, 5, 5)

    app.fill('@')

    # x = app.get_width() / 2 - 10
    # y = app.get_height() / 2
    app.rect(x, 5, 8, 4)
    # app.rect(10, 5, 5, 4)
    # app.rect(10, 10, 5, 4)
    # size = 5
    # app.fill('*')

    # app.begin_shape()
    # app.vertex(x, y)
    # app.vertex(x + size, y)
    # app.vertex(x + size, y - size)
    # app.vertex(x + size * 2, y)
    # app.vertex(x, y + size * 2)
    # app.end_shape(app.CLOSE)
    # app.no_loop()


app.run()
