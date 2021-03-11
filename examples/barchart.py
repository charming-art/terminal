import charming as app
from _utils import scale_linear, scale_band, scale_ordinal
from _data import covid_mock as data

# open canvas
app.full_screen(app.DOUBLE)
app.no_cursor()

# chart options
margin = {
    'top': 5,
    'right': 5,
    'bottom': 5,
    'left': 5
}
width = app.get_width() - margin['left'] - margin['right']
height = app.get_height() - margin['top'] - margin['bottom']

# scales
max_data = app.max(data, key=lambda d: d['value'])
names = [d['name'] for d in data]
colors = [
    ('🌈', app.GREEN),
    ('🦠', app.RED),
    (('⚠️', 2), app.YELLOW),
    (('☠️', 2), app.WHITE)
]
x_scale = scale_band(names, [0, width], padding=2)
y_scale = scale_linear([0, max_data['value']], [height, 0])
color_scale = scale_ordinal(names, colors)

# draw
app.translate(margin['left'], margin['top'])

# bars
for d in data:
    name, value = d['name'], d['value']
    x = x_scale(name)
    y = y_scale(value)
    bw = x_scale.band_width()
    ch, bg = color_scale(name)

    # bars
    app.no_stroke()
    app.fill(ch, bg=bg)
    app.rect(x, y, int(bw), height - y)

    # value
    app.stroke()
    app.text_align(app.CENTER)
    app.text(str(value), x + bw / 2 + 1, y - 2)

# bottom axes
app.stroke('-')
app.line(0, height, width, height)
for name in x_scale.domain():
    x = x_scale(name)
    bw = x_scale.band_width()
    app.stroke()
    app.text_align(app.CENTER)
    app.text(name, x + bw / 2 + 1, height + 1)

if __name__ == "__main__":
    app.run()
