import charming as app

# setup
app.full_screen()
app.no_cursor()

# styles
app.stroke('@', app.YELLOW, app.RED)
app.fill('+', app.GREEN, app.BLUE)

# transforms
size = 12
app.translate(size, size / 2)
# app.no_stroke()

# first row
app.point(0, 0)

app.line(size, 0, size * 2, 0)

app.triangle(
    size * 3, 0,  # point1
    size * 4, 0,  # point2
    size * 3, size / 2  # point3
)
app.rect(size * 5, 0, size, size / 2)

app.square(size * 7, 0, size)

app.quad(
    size * 9, 0,  # point1
    size * 10 + 5, 2,  # point2
    size * 10 - 5, size,  # point3
    size * 9, size - 5  # point4
)

# second row

app.ellipse(0, size * 2, size, size / 2)
app.circle(size * 2, size * 2, size)
app.arc(
    size * 4, size * 2,
    size, size, 0,
    app.QUARTER_PI * 5
)

app.arc(
    size * 6, size * 2,
    size, size, 0,
    app.QUARTER_PI * 5,
    app.CHORD
)

app.arc(
    size * 8, size * 2,
    size, size, 0,
    app.QUARTER_PI * 5,
    app.PIE
)


app.run()
