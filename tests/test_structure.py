import charming as app


@app.setup
def setup():
    app.frame_rate(1)
    print('setup')


@app.draw
def draw():
    print('draw')

app.run()
