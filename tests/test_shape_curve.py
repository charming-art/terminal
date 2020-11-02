import charming as app

app.full_screen()
app.stroke('o', app.BLUE, app.GREEN)
app.fill('@')
# app.no_stroke()
# app.curve_tightness(1)
# app.curve(5, 26, 73, 24, 73, 11, 15, 25)
# t = 0
# cnt = 3
# app.stroke('p', app.CYAN, app.RED)
# app.stroke_weight(1)
# while t <= 1:
#     x = app.curve_point(5, 73, 73, 15, t)
#     y = app.curve_point(26, 24, 11, 25, t)
#     app.point(x, y)
#     t += 1 / cnt
# app.no_fill()
# app.curve_tightness(0.5)
# app.fill('@')
app.translate(0, 1)
with app.open_shape():
    app.curve_vertex(84,  91)
    app.curve_vertex(84,  91)
    app.curve_vertex(68,  19)
    app.curve_vertex(21,  17)
    app.curve_vertex(32, 100)
    app.curve_vertex(32, 100)

app.run()
