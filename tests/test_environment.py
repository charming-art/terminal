import charming as app

@app.setup
def setup():
    app.full_screen()
    app.frame_rate(1)


@app.draw
def draw():
    print(app.get_width(), app.get_height())

app.run()

