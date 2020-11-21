import charming as app

msg = ""


@app.setup
def setup():
    global msg
    # Make the canvas size be half of the terminal
    win_width, win_height = app.get_window_size()
    app.size(win_width / 2, win_height / 2)
    app.frame_rate(10)

    msg = f'( {win_width} ,  {win_height} )'


@app.draw
def draw():
    app.background(' ')
    t = app.get_frame_count() % 2

    if t == 0:
        app.cursor()
        app.stroke(fg=app.RED)
    else:
        app.no_cursor()
        app.stroke(fg=app.BLUE)

    app.translate(app.get_width() / 2, app.get_height() / 2)
    app.text_size(app.BIG)
    app.text_align(app.CENTER, app.MIDDLE)
    app.text(msg, 0, 0)


@app.window_resized
def window_resized():
    global msg
    # update text
    win_width, win_height = app.get_window_size()
    msg = f'( {win_width} ,  {win_height}) '

    # update cursor
    x = app.random(app.get_width())
    y = app.random(app.get_height())
    app.set_cursor(x, y)


app.run()
