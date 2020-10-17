import charming as app


@app.setup
def setup():
    app.size(10, 10)


@app.draw
def draw():
    pass


@app.mouse_clicked
def mouse_clicked():
    app.point(app.get_mouse_x(), app.get_mouse_y())


@app.window_resized
def window_resized():
    print(app.get_window_width(), app.get_window_height())


app.run()
