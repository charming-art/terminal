import charming as cm
from scales import scale_linear, scale_band, scale_ordinal

# mock data
data = [
    {
        'name': 'curve',
        'value': 10,
    },
    {
        'name': 'confirm',
        'value': 30,
    },
    {
        'name': 'suspect',
        'value': 15,
    },
    {
        'name': 'dead',
        'value': 5,
    },
]

# open canvas
cm.full_screen(cm.DOUBLE)
cm.no_cursor()

# chart options
margin = {
    'top': 5,
    'right': 5,
    'bottom': 5,
    'left': 5
}
width = cm.get_width() - margin['left'] - margin['right']
height = cm.get_height() - margin['top'] - margin['bottom']

# scales
max_data = cm.max(data, key=lambda d: d['value'])
names = [d['name'] for d in data]
colors = [
    ('🌈', cm.GREEN),
    ('🦠', cm.RED),
    (('⚠️', 2), cm.YELLOW),
    (('☠️', 2), cm.WHITE)
]
x_scale = scale_band(names, [0, width], padding=2)
y_scale = scale_linear([0, max_data['value']], [height, 0])
color_scale = scale_ordinal(names, colors)

# draw
cm.translate(margin['left'], margin['top'])

# bars
for d in data:
    name, value = d['name'], d['value']
    x = x_scale(name)
    y = y_scale(value)
    bw = x_scale.band_width()
    ch, bg = color_scale(name)

    # bars
    cm.no_stroke()
    cm.fill(ch, bg=bg)
    cm.rect(x, y, int(bw), height - y)

    # value
    cm.stroke()
    cm.text_align(cm.CENTER)
    cm.text(str(value), x + bw / 2 + 1, y - 2)

# bottom axes
cm.stroke('-')
cm.line(0, height, width, height)
for name in x_scale.domain():
    x = x_scale(name)
    bw = x_scale.band_width()
    cm.stroke()
    cm.text_align(cm.CENTER)
    cm.text(name, x + bw / 2 + 1, height + 1)

if __name__ == "__main__":
    cm.run()
