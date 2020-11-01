import charming as app

app.full_screen()
app.stroke('1', app.RED, app.YELLOW)
# app.no_stroke()
app.fill('0', app.BLUE, app.GREEN)
with app.open_shape(app.POLYGON, app.CLOSE):
    app.vertex(0, 0)
    app.vertex(20, 0)
    app.vertex(20, 20)
    app.vertex(0, 20)
    with app.open_contour():
        app.vertex(5, 5)
        app.vertex(5, 15)
        app.vertex(15, 15)
        app.vertex(15, 5)
app.run()
