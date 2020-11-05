import charming as app


@app.setup
def setup():
    app.size(30, 30)
    # app.rect_mode(app.CENTER)
    app.ellipse_mode(app.CORNER)

x = 0
@app.draw
def draw():
    app.background(' ')
    global x
    x += 1
    app.square(x, 1, 3)
    # app.circle(1, 1, 1)
    app.circle(x, 10, 4)
    # app.point(5, 5)
    app.no_loop()

app.run()
