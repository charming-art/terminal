import charming as app


@app.setup
def setup():
    app.full_screen()

@app.draw
def draw():
    # app.fill('+')
    # app.translate(20, 10)
    # app.no_stroke()
    # with app.open_context():
    #     app.scale(3)
    #     app.point(0, 0)
    app.stroke('@')
    # app.stroke_weight(1)
    app.translate(app.get_width() / 2, app.get_height() / 2)
    app.scale(21, 15)
    # app.rotate(app.PI / 3)
    app.point(0, 0)
    # app.no_stroke()
    # app.scale(2)
    # app.circle(0, 0, 5)
    # app.stroke_weight(1)
    # app.rect(0, 0, 1, 1)
    app.no_loop()


app.run()