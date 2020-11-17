import charming as app


@app.setup
def setup():
    app.size(30, 20)


@app.draw
def draw():
    # pass
    app.background(' ')
    # if app.get_key_pressed():
    #     app.stroke(app.get_key())
    #     app.point(app.get_width() / 2, app.get_height() / 2)


@app.key_pressed
def key_pressed():
    if app.get_key() == app.CODED:
        if app.get_key_code() == app.UP:
            app.stroke('+')
            app.point(app.get_width() / 2 + 1, app.get_height() / 2)



app.run()
