import charming as app


@app.setup
def setup():
    app.full_screen()
    app.frame_rate(2)
    app.no_cursor()


x = 0


@app.draw
def draw():
    global x
    x += 1
    t = app.get_frame_count() % 2

    if t == 0:
        app.background('@')
    else:
        app.background('+')

    app.fill('0', app.YELLOW, app.RED)
    app.stroke('1', app.GREEN, app.BLUE)
    app.rect(0, 0, 5, 5)

    app.push()
    app.no_fill()
    app.translate(10, 0)
    app.rect(0, 0, 5, 5)
    app.pop()

    app.push()
    app.no_stroke()
    app.translate(x, 8)
    app.rect(0, 0, 5, 5)
    app.pop()

    app.push()
    app.no_stroke()
    app.no_fill()
    app.translate(30, 0)
    app.rect(0, 0, 5, 5)
    app.pop()


app.run()
