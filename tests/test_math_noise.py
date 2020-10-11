import charming as app

xoff = 0


@app.setup
def setup():
    app.noise_seed(0)
    app.full_screen()


@app.draw
def draw():
    global xoff
    app.noise_detail(1, 0.5)
    app.backgournd(' ')
    xoff += 0.1
    x = app.noise(xoff) * app.get_width()
    app.line(x, 0, x, app.get_height())


app.run()
