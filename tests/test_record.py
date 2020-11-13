import charming as app


@app.setup
def setup():
    # app.full_screen()
    app.size(30, 20)


x = 0
@app.draw
def draw():
    global x
    app.background(' ')
    # x += 1
    app.rect(x, 0, 10, 10)


app.run()
