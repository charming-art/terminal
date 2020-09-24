import charming as app


@app.setup
def setup():
    app.size(10, 10)


@app.draw
def draw():
    pass


app.run()
