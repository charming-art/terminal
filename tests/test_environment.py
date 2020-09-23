import charming as app
import builtins


@app.setup
def setup():
    app.size(100, 100)
    app.frame_rate(1)


@app.draw
def draw():
    print(app.get_width(), app.get_height())

app.run()

