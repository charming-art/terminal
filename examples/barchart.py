import charming as app

data = [{
    'name': 'curve',
    'value': 10,
    'color': app.CColor('🌈', bg=app.GREEN)
},
    {
    'name': 'confirm',
    'value': 20,
    'color': app.CColor('🦠', bg=app.RED)
},
    {
    'name': 'dead',
    'value': 5,
    'color': app.CColor(('☠️', 2), bg=app.WHITE)
}]

margin = {
    'top': 5,
    'right': 5,
    'bottom': 5,
    'left': 5
}

# init state
app.full_screen(app.DOUBLE)
app.no_cursor()

# attrs
width = app.get_width() - margin['left'] - margin['right']
height = app.get_height() - margin['top'] - margin['bottom']

# transform
app.translate(margin['left'], margin['top'])


# draw data
for i, d in enumerate(data):
    w = int(width / (len(data)))
    bw = w - 3
    bh = app.map(d['value'], 0, 20, 0, height)
    x = i * w + 2
    y = height - bh

    # bar
    app.no_stroke()
    app.fill(d['color'])
    app.rect(x, y, bw, bh)

    # name
    app.stroke()
    app.text_align(app.LEFT)
    app.text(d['name'], x, height + 2)

    # value
    app.text_align(app.CENTER)
    app.text(str(d['value']), x + bw / 2 + 1, y - 2)

# draw axes
app.stroke('-')
app.line(0, height + 1, width, height + 1)



app.run()
