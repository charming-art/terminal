import charming as app


@app.setup
def setup():
    app.size(30, 20)
    app.cursor(10, 10)


@app.draw
def draw():
    app.background(' ')


@app.cursor_moved
def cursor_moved():
    x = app.get_cursor_x()
    y = app.get_cursor_y()
    app.point(x, y)


app.run()
