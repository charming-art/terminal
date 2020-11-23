import charming as app


@app.setup
def setup():
    app.size(30, 20)
    app.frame_rate(2)
    app.no_cursor()


@app.draw
def draw():
    if app.get_mouse_pressed():
        app.background(bg=app.GREEN)
    else:
        app.background(bg=app.YELLOW)


@app.mouse_pressed
def mouse_pressed():
    if app.get_mouse_button() == app.RIGHT:
        app.stroke('P')
    else:
        app.stroke('p')
    app.point(app.get_mouse_x(), app.get_mouse_y())


@app.mouse_clicked
def mouse_clicked():
    if app.get_mouse_button() == app.RIGHT:
        app.stroke('C')
    else:
        app.stroke('c')
    app.point(app.get_mouse_x() + 1, app.get_mouse_y())


@app.mouse_released
def mouse_released():
    if app.get_mouse_button() == app.RIGHT:
        app.stroke('R')
    else:
        app.stroke('r')
    app.point(app.get_mouse_x() + 2, app.get_mouse_y())


app.run()
