import charming as app


@app.setup
def setup():
    app.size(10, 10)


@app.draw
def draw():
    pass
    # app.background(' ')
    # if app.get_mouse_pressed():
    #     app.point(0, 0)


@app.mouse_pressed
def mouse_pressed():
    if app.get_mouse_button() == app.RIGHT:
        app.stroke('@')
    else:
        app.stroke('+')
    app.point(app.get_mouse_x(), app.get_mouse_y())


@app.mouse_clicked
def mouse_clicked():
    if app.get_mouse_button() == app.RIGHT:
        app.stroke('@')
    else:
        app.stroke('+')
    app.point(app.get_mouse_x() + 1, app.get_mouse_y())


@app.mouse_released
def mouse_released():
    if app.get_mouse_button() == app.RIGHT:
        app.stroke('@')
    else:
        app.stroke('+')
    app.point(app.get_mouse_x() + 2, app.get_mouse_y())


app.run()
