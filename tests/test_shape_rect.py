import charming as app


@app.setup
def setup():
    app.size(30, 30, app.DOUBLE)
    # app.rect_mode(app.CENTER)
    # app.ellipse_mode(app.CORNER)
    app.frame_rate(5)

x = 0
@app.draw
def draw():
    global x
    x += 1
    app.background(' ')
    app.fill(('❤️', 2), 2)
    app.square(x, 0, 3)
    # app.circle(1, 1, 1)
    # app.circle(x, 10, 4)
    # app.point(5, 5)
    # app.no_loop()

app.run()
