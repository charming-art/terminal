import charming as app


@app.setup
def setup():
    # app.full_screen()
    app.size(50, 20)
    # app.size()
    app.begin_log_frame_buffer()
    # app.background('*')

    # app.frame_rate(1)
    # app.no_cursor()


x = 0

# theta = 0

@app.draw
def draw():
    global x
    x += 0.5
    app.background(" ")
    # color = app.color(('🧚‍♀️')) # not display
    # color = app.color(('⏰', 2))  # wrong display
    # color = app.color('爱', app.YELLOW, app.BLUE)
    color = app.color('🌈')
    # color = app.color('@')
    app.stroke(color)
    # app.fill('+')
    # app.fill(' ', app.WHITE)
    # app.stroke(color)
    # app.fill(color)
    # app.ellipse(20, 10, 5, 5)

    # app.fill(' ')
    # app.point(0, 0)

    # x = app.get_width() / 2
    y = app.get_height() / 2
    # app.translate(x, y)
    # app.rotate(theta)
    # app.rect(x, 0, 8, 4)
    # app.log_frame_buffer()
    # app.rect(x, 5, 10, 4)
    # app.rect(10, 10, 5, 4)
    size = 5
    # app.fill('*')
    # app.point(10, 0)
    app.begin_shape()
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y - size)
    app.vertex(x + size * 2, y)
    app.vertex(x, y + size * 2)
    app.end_shape(app.CLOSE)
    # app.no_loop()


app.run()
