import charming as app


@app.setup
def setup():
    app.full_screen()

@app.draw
def draw():
    app.fill('+')
    app.stroke_weight(1)
    app.rect(0, 0, 1, 1)
    app.no_loop()


app.run()