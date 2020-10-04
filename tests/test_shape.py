import charming as app


@app.setup
def setup():
    app.full_screen()


@app.draw
def draw():
    mouse_x = app.get_mouse_x()
    mouse_y = app.get_mouse_y()
    app.line(20, 10, mouse_x, mouse_y)
    # app.line(10, 10, 10 - offset, 15)


app.run()
