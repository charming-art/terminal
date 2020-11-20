import charming as app

app.full_screen()

size = 5
x = 1
y = 5
app.fill('*', app.YELLOW, app.RED)
app.stroke('@', app.GREEN, app.BLUE)
# app.no_stroke()
app.translate(size, 0)

# polygon without close
app.begin_shape()
app.vertex(x, y)
app.vertex(x + size, y)
app.vertex(x + size, y + size)
app.vertex(x, y + size)
app.end_shape()

# polygon with close
x += 15
with app.open_shape(close_mode=app.CLOSE):
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y + size)
    app.vertex(x, y + size)

# LINES
x += 15
with app.open_shape(app.LINES):
    app.vertex(x, y)
    app.vertex(x + size, y)
    app.vertex(x + size, y + size)
    app.vertex(x, y + size)

# TRIANGLES
x += 15
y = 10
app.begin_shape(app.TRIANGLES)
app.vertex(x, y)
app.vertex(x + size, y - size)
app.vertex(x + size * 2, y)
app.vertex(x + size * 3, y - size)
app.vertex(x + size * 4, y)
app.vertex(x + size * 5, y - size)
app.end_shape()

# TRIANGLE_STRIP
x += 35
app.begin_shape(app.TRIANGLE_STRIP)
app.vertex(x, y)
app.vertex(x + size, y - size)
app.vertex(x + size * 2, y)
app.vertex(x + size * 3, y - size)
app.vertex(x + size * 4, y)
app.vertex(x + size * 5, y - size)
app.vertex(x + size * 6, y)
app.end_shape()

# TRIANGLE_FAN
x += 45
app.begin_shape(app.TRIANGLE_FAN)
app.vertex(x, y)
app.vertex(x, y - size)
app.vertex(x + size, y)
app.vertex(x, y + size)
app.vertex(x - size, y)
app.vertex(x, y - size)
app.end_shape()

# QUADS
y += 8
x = 1
app.begin_shape(app.QUADS)
app.vertex(x, y)
app.vertex(x, y + size)
app.vertex(x + size, y + size)
app.vertex(x + size, y)
app.vertex(x + size * 2, y)
app.vertex(x + size * 2, y + size)
app.vertex(x + size * 3, y + size)
app.vertex(x + size * 3, y)
app.end_shape()

# QUAD_STRIP
x = 25
app.begin_shape(app.QUAD_STRIP)

app.vertex(x, y)
app.vertex(x, y + size)
app.vertex(x + size, y)
app.vertex(x + size, y + size)

app.vertex(x + size * 2, y)
app.vertex(x + size * 2, y + size)
app.vertex(x + size * 3, y)
app.vertex(x + size * 3, y + size)

app.end_shape()

app.translate(50, y)
with app.open_shape(app.POLYGON, app.CLOSE):
    app.vertex(0, 0)
    app.vertex(15, 0)
    app.vertex(15, 15)
    app.vertex(0, 15)
    with app.open_contour():
        app.vertex(5, 5)
        app.vertex(5, 10)
        app.vertex(10, 10)
        app.vertex(10, 5)

app.translate(30, 5)
app.begin_shape()
app.vertex(0, 0)
app.vertex(5, 0)
app.vertex(5, -5)
app.vertex(10, 0)
app.vertex(0, 10)
app.end_shape(app.CLOSE)

app.translate(25, 0)
app.begin_shape()
app.vertex(0, 0)
app.vertex(10, 10)
app.vertex(5, 10)
app.vertex(5, 8)
app.vertex(-5, 8)
app.vertex(-5, 10)
app.vertex(-10, 10)
app.end_shape(app.CLOSE)

app.translate(25, -2)
app.begin_shape()
app.vertex(0, 0)
app.vertex(10, 10)
app.vertex(5, 10)
app.vertex(5, 12)
app.vertex(-5, 12)
app.vertex(-5, 10)
app.vertex(-10, 10)
app.end_shape(app.CLOSE)

app.run()
